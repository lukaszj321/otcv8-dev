# ANGLE Integration Guide

## Overview

**ANGLE** (Almost Native Graphics Layer Engine) provides OpenGL ES implementation on Windows using Direct3D 11 as the backend. OTClient v8 uses ANGLE to achieve cross-platform graphics compatibility on Windows without requiring full OpenGL drivers.

## Why ANGLE?

Traditional OpenGL drivers on Windows have several limitations:

1. **Driver Quality**: Inconsistent OpenGL support across GPU vendors
2. **Legacy Support**: Poor support for older integrated GPUs
3. **Performance**: Direct3D often performs better on Windows
4. **Stability**: ANGLE provides more stable and predictable behavior

## Architecture

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[OTClient Application] --> B[EGL API Layer]
    B --> C[ANGLE Implementation]
    C --> D[Direct3D 11]
    D --> E[GPU Driver]
    E --> F[Hardware GPU]
    
    G[OpenGL ES Calls] --> B
    H[Window Management] --> B
    
    style C fill:#6a4,stroke:#8c6,stroke-width:2px
    style D fill:#46a,stroke:#68c,stroke-width:2px
```

## Required Components

### Headers

```cpp
// EGL headers (from ANGLE)
#include <EGL/egl.h>
#include <EGL/eglext.h>

// GLES2 headers
#include <GLES2/gl2.h>
#include <GLES2/gl2ext.h>

// GLES3 headers (if using ES 3.0+)
#include <GLES3/gl3.h>
#include <GLES3/gl3ext.h>
```

### Libraries

Link against ANGLE libraries:

```cmake
# CMakeLists.txt
target_link_libraries(otclient
    libEGL.lib
    libGLESv2.lib
)
```

### Runtime DLLs

Distribute with application:

- `libEGL.dll` (~500 KB)
- `libGLESv2.dll` (~3.5 MB)
- `d3dcompiler_47.dll` (~4 MB, for shader compilation)

## EGL Initialization

### Basic Setup

```cpp
// egl_context.cpp

#include <EGL/egl.h>
#include <GLES2/gl2.h>
#include <Windows.h>

class EGLContext {
private:
    EGLDisplay m_display;
    EGLContext m_context;
    EGLSurface m_surface;
    HWND m_window;

public:
    bool initialize(HWND hwnd) {
        m_window = hwnd;
        
        // Step 1: Get EGL display
        m_display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
        if (m_display == EGL_NO_DISPLAY) {
            logError("eglGetDisplay failed");
            return false;
        }
        
        // Step 2: Initialize EGL
        EGLint major, minor;
        if (!eglInitialize(m_display, &major, &minor)) {
            logError("eglInitialize failed");
            return false;
        }
        
        logInfo("EGL version: %d.%d", major, minor);
        
        // Step 3: Choose config
        EGLConfig config;
        if (!chooseConfig(&config)) {
            return false;
        }
        
        // Step 4: Create window surface
        m_surface = eglCreateWindowSurface(m_display, config, (EGLNativeWindowType)hwnd, nullptr);
        if (m_surface == EGL_NO_SURFACE) {
            logError("eglCreateWindowSurface failed");
            return false;
        }
        
        // Step 5: Create context
        m_context = createContext(config);
        if (m_context == EGL_NO_CONTEXT) {
            return false;
        }
        
        // Step 6: Make current
        if (!eglMakeCurrent(m_display, m_surface, m_surface, m_context)) {
            logError("eglMakeCurrent failed");
            return false;
        }
        
        return true;
    }
    
    bool chooseConfig(EGLConfig* outConfig) {
        const EGLint configAttributes[] = {
            EGL_RED_SIZE, 8,
            EGL_GREEN_SIZE, 8,
            EGL_BLUE_SIZE, 8,
            EGL_ALPHA_SIZE, 8,
            EGL_DEPTH_SIZE, 16,
            EGL_STENCIL_SIZE, 8,
            EGL_SAMPLE_BUFFERS, 1,
            EGL_SAMPLES, 4,  // 4x MSAA
            EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
            EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
            EGL_NONE
        };
        
        EGLint numConfigs;
        if (!eglChooseConfig(m_display, configAttributes, outConfig, 1, &numConfigs)) {
            logError("eglChooseConfig failed");
            return false;
        }
        
        if (numConfigs == 0) {
            logError("No suitable EGL config found");
            return false;
        }
        
        return true;
    }
    
    EGLContext createContext(EGLConfig config) {
        // Try ES 3.0 first
        EGLint es3Attributes[] = {
            EGL_CONTEXT_CLIENT_VERSION, 3,
            EGL_NONE
        };
        
        EGLContext ctx = eglCreateContext(m_display, config, EGL_NO_CONTEXT, es3Attributes);
        if (ctx != EGL_NO_CONTEXT) {
            logInfo("Created OpenGL ES 3.0 context");
            return ctx;
        }
        
        // Fallback to ES 2.0
        EGLint es2Attributes[] = {
            EGL_CONTEXT_CLIENT_VERSION, 2,
            EGL_NONE
        };
        
        ctx = eglCreateContext(m_display, config, EGL_NO_CONTEXT, es2Attributes);
        if (ctx != EGL_NO_CONTEXT) {
            logInfo("Created OpenGL ES 2.0 context");
            return ctx;
        }
        
        logError("Failed to create EGL context");
        return EGL_NO_CONTEXT;
    }
    
    void swapBuffers() {
        eglSwapBuffers(m_display, m_surface);
    }
    
    void cleanup() {
        if (m_display != EGL_NO_DISPLAY) {
            eglMakeCurrent(m_display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
            
            if (m_context != EGL_NO_CONTEXT) {
                eglDestroyContext(m_display, m_context);
            }
            
            if (m_surface != EGL_NO_SURFACE) {
                eglDestroySurface(m_display, m_surface);
            }
            
            eglTerminate(m_display);
        }
    }
};
```

### Error Handling

```text
const char* eglErrorString(EGLint error) {
    switch (error) {
        case EGL_SUCCESS: return "EGL_SUCCESS";
        case EGL_NOT_INITIALIZED: return "EGL_NOT_INITIALIZED";
        case EGL_BAD_ACCESS: return "EGL_BAD_ACCESS";
        case EGL_BAD_ALLOC: return "EGL_BAD_ALLOC";
        case EGL_BAD_ATTRIBUTE: return "EGL_BAD_ATTRIBUTE";
        case EGL_BAD_CONFIG: return "EGL_BAD_CONFIG";
        case EGL_BAD_CONTEXT: return "EGL_BAD_CONTEXT";
        case EGL_BAD_CURRENT_SURFACE: return "EGL_BAD_CURRENT_SURFACE";
        case EGL_BAD_DISPLAY: return "EGL_BAD_DISPLAY";
        case EGL_BAD_MATCH: return "EGL_BAD_MATCH";
        case EGL_BAD_NATIVE_PIXMAP: return "EGL_BAD_NATIVE_PIXMAP";
        case EGL_BAD_NATIVE_WINDOW: return "EGL_BAD_NATIVE_WINDOW";
        case EGL_BAD_PARAMETER: return "EGL_BAD_PARAMETER";
        case EGL_BAD_SURFACE: return "EGL_BAD_SURFACE";
        case EGL_CONTEXT_LOST: return "EGL_CONTEXT_LOST";
        default: return "Unknown EGL error";
    }
}

void logEGLError(const char* function) {
    EGLint error = eglGetError();
    if (error != EGL_SUCCESS) {
        fprintf(stderr, "%s failed: %s (0x%x)\n", 
                function, eglErrorString(error), error);
    }
}
```

## OpenGL ES Usage

### Shader Compilation

```text
GLuint compileShader(GLenum type, const char* source) {
    GLuint shader = glCreateShader(type);
    glShaderSource(shader, 1, &source, nullptr);
    glCompileShader(shader);
    
    // Check compilation status
    GLint compiled;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &compiled);
    
    if (!compiled) {
        GLint logLength;
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &logLength);
        
        std::vector<char> log(logLength);
        glGetShaderInfoLog(shader, logLength, nullptr, log.data());
        
        fprintf(stderr, "Shader compilation failed:\n%s\n", log.data());
        glDeleteShader(shader);
        return 0;
    }
    
    return shader;
}

GLuint createProgram(const char* vertexSrc, const char* fragmentSrc) {
    GLuint vertexShader = compileShader(GL_VERTEX_SHADER, vertexSrc);
    GLuint fragmentShader = compileShader(GL_FRAGMENT_SHADER, fragmentSrc);
    
    if (vertexShader == 0 || fragmentShader == 0) {
        return 0;
    }
    
    GLuint program = glCreateProgram();
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);
    
    // Check link status
    GLint linked;
    glGetProgramiv(program, GL_LINK_STATUS, &linked);
    
    if (!linked) {
        GLint logLength;
        glGetProgramiv(program, GL_INFO_LOG_LENGTH, &logLength);
        
        std::vector<char> log(logLength);
        glGetProgramInfoLog(program, logLength, nullptr, log.data());
        
        fprintf(stderr, "Program linking failed:\n%s\n", log.data());
        glDeleteProgram(program);
        program = 0;
    }
    
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);
    
    return program;
}
```

### Basic Rendering

```cpp
void render() {
    // Clear
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Use shader program
    glUseProgram(g_program);
    
    // Set uniforms
    GLint mvpLoc = glGetUniformLocation(g_program, "u_mvp");
    glUniformMatrix4fv(mvpLoc, 1, GL_FALSE, g_mvpMatrix);
    
    // Bind texture
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, g_texture);
    GLint texLoc = glGetUniformLocation(g_program, "u_texture");
    glUniform1i(texLoc, 0);
    
    // Draw
    glBindBuffer(GL_ARRAY_BUFFER, g_vbo);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, g_ibo);
    
    GLint posLoc = glGetAttribLocation(g_program, "a_position");
    glEnableVertexAttribArray(posLoc);
    glVertexAttribPointer(posLoc, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*)0);
    
    GLint texCoordLoc = glGetAttribLocation(g_program, "a_texcoord");
    glEnableVertexAttribArray(texCoordLoc);
    glVertexAttribPointer(texCoordLoc, 2, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*)(3 * sizeof(float)));
    
    glDrawElements(GL_TRIANGLES, g_indexCount, GL_UNSIGNED_SHORT, 0);
    
    glDisableVertexAttribArray(posLoc);
    glDisableVertexAttribArray(texCoordLoc);
}
```

## Performance Tips

### 1. Batch Rendering

Minimize draw calls by batching similar geometry:

```cpp
// BAD: Individual draw calls
for (auto& sprite : sprites) {
    bindTexture(sprite.texture);
    draw(sprite);
}

// GOOD: Batch by texture
std::map<Texture*, std::vector<Sprite*>> batches;
for (auto& sprite : sprites) {
    batches[sprite.texture].push_back(&sprite);
}

for (auto& [texture, batch] : batches) {
    bindTexture(texture);
    drawBatch(batch);
}
```

### 2. Minimize State Changes

Cache and only change when necessary:

```cpp
GLuint currentProgram = 0;
void useProgram(GLuint program) {
    if (program != currentProgram) {
        glUseProgram(program);
        currentProgram = program;
    }
}
```

### 3. Use VAOs (ES 3.0+)

Vertex Array Objects reduce setup overhead:

```cpp
GLuint vao;
glGenVertexArrays(1, &vao);
glBindVertexArray(vao);

// Setup vertex attributes once
glBindBuffer(GL_ARRAY_BUFFER, vbo);
glEnableVertexAttribArray(0);
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*)0);

// Later, just bind VAO
glBindVertexArray(vao);
glDrawElements(...);
```

## Troubleshooting

### Issue: Black Screen

```text
// Check EGL errors after each call
if (!eglMakeCurrent(...)) {
    logEGLError("eglMakeCurrent");
}

// Verify context is current
EGLContext current = eglGetCurrentContext();
if (current == EGL_NO_CONTEXT) {
    fprintf(stderr, "No current context\n");
}

// Check GL state
GLenum glError = glGetError();
if (glError != GL_NO_ERROR) {
    fprintf(stderr, "GL Error: 0x%x\n", glError);
}
```

### Issue: Performance Problems

```cpp
// Enable ANGLE performance features
EGLint displayAttributes[] = {
    EGL_PLATFORM_ANGLE_TYPE_ANGLE, EGL_PLATFORM_ANGLE_TYPE_D3D11_ANGLE,
    EGL_PLATFORM_ANGLE_MAX_VERSION_MAJOR_ANGLE, 11,
    EGL_PLATFORM_ANGLE_MAX_VERSION_MINOR_ANGLE, 0,
    EGL_PLATFORM_ANGLE_DEVICE_TYPE_ANGLE, EGL_PLATFORM_ANGLE_DEVICE_TYPE_HARDWARE_ANGLE,
    EGL_NONE
};

m_display = eglGetPlatformDisplayEXT(EGL_PLATFORM_ANGLE_ANGLE, 
                                     EGL_DEFAULT_DISPLAY, 
                                     displayAttributes);
```

### Issue: DLL Not Found

Ensure DLLs are in application directory:

```
otclient.exe
├── libEGL.dll
├── libGLESv2.dll
└── d3dcompiler_47.dll
```

Or add to PATH environment variable.

## See Also

- [EGL Initialization](./egl_initialization.md)
- [DLL Deployment Checklist](./dll_deployment.md)
- [VC16 Build Configuration](../15_vc16/index.md)
- [Graphics Core](../01_core/graphics.md)
