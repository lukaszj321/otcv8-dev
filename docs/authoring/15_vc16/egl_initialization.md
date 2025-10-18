# EGL Initialization Reference

## Quick Start

Basic EGL setup for OTClient v8:

```cpp
#include <EGL/egl.h>
#include <GLES2/gl2.h>

// 1. Get display
EGLDisplay display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
eglInitialize(display, nullptr, nullptr);

// 2. Choose config
EGLint configAttribs[] = {
    EGL_RED_SIZE, 8,
    EGL_GREEN_SIZE, 8,
    EGL_BLUE_SIZE, 8,
    EGL_ALPHA_SIZE, 8,
    EGL_DEPTH_SIZE, 16,
    EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
    EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
    EGL_NONE
};

EGLConfig config;
EGLint numConfigs;
eglChooseConfig(display, configAttribs, &config, 1, &numConfigs);

// 3. Create surface
EGLSurface surface = eglCreateWindowSurface(display, config, hwnd, nullptr);

// 4. Create context
EGLint contextAttribs[] = {
    EGL_CONTEXT_CLIENT_VERSION, 2,
    EGL_NONE
};
EGLContext context = eglCreateContext(display, config, EGL_NO_CONTEXT, contextAttribs);

// 5. Make current
eglMakeCurrent(display, surface, surface, context);
```

## Complete Example

See [ANGLE Integration Guide](./angle_integration.md) for detailed implementation with error handling.

## Configuration Options

### Anti-Aliasing (MSAA)

```cpp
EGL_SAMPLE_BUFFERS, 1,
EGL_SAMPLES, 4,  // 4x MSAA
```

### Double Buffering

```cpp
EGL_RENDER_BUFFER, EGL_BACK_BUFFER,  // Default
```

### VSync Control

```cpp
eglSwapInterval(display, 1);  // Enable VSync
eglSwapInterval(display, 0);  // Disable VSync
```

## See Also

- [ANGLE Integration](./angle_integration.md)
- [DLL Deployment](./dll_deployment.md)
