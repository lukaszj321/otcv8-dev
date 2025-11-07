---
doc_id: "cpp-api-a4dd1d57199e"
source_path: "framework/http/http.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: http.h"
summary: "Dokumentacja API C++ dla framework/http/http.h"
tags: ["cpp", "api", "otclient"]
---

# framework/http/http.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu http.

## Classes/Structs

### Klasa: `WebsocketSession`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `get` |  | `int get(const std::string& url, int timeout = 5)` |
| `post` |  | `int post(const std::string& url, const std::string& data, int timeout = 5, bool isJson = false)` |
| `download` |  | `int download(const std::string& url, std::string path, int timeout = 5)` |
| `ws` |  | `int ws(const std::string& url, int timeout = 5)` |
| `wsSend` |  | `bool wsSend(int operationId, std::string message)` |
| `wsClose` |  | `bool wsClose(int operationId)` |
| `cancel` |  | `bool cancel(int id)` |
| `m_downloads` |  | `return m_downloads` |
| `clearDownloads` |  | `void clearDownloads() {` |
| `getFile` |  | `HttpResult_ptr getFile(std::string path) {` |
| `it` |  | `auto it = m_downloads.find(path)` |
| `nullptr` |  | `return nullptr` |
| `setUserAgent` |  | `void setUserAgent(const std::string& userAgent)` |

### Klasa: `Http`

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `get`

**Sygnatura:** `int get(const std::string& url, int timeout = 5)`

### `post`

**Sygnatura:** `int post(const std::string& url, const std::string& data, int timeout = 5, bool isJson = false)`

### `download`

**Sygnatura:** `int download(const std::string& url, std::string path, int timeout = 5)`

### `ws`

**Sygnatura:** `int ws(const std::string& url, int timeout = 5)`

### `wsSend`

**Sygnatura:** `bool wsSend(int operationId, std::string message)`

### `wsClose`

**Sygnatura:** `bool wsClose(int operationId)`

### `cancel`

**Sygnatura:** `bool cancel(int id)`

### `clearDownloads`

**Sygnatura:** `void clearDownloads() {`

### `getFile`

**Sygnatura:** `HttpResult_ptr getFile(std::string path) {`

### `setUserAgent`

**Sygnatura:** `void setUserAgent(const std::string& userAgent)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    
    Http["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Http</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            <b>HTTP Methods:</b><br/>
            + get(url, timeout)<br/>
            + post(url, data, timeout, isJson)<br/>
            <b>Download:</b><br/>
            + download(url, path, timeout)<br/>
            <b>WebSocket:</b><br/>
            + ws(url, timeout)<br/>
            + wsSend(operationId, message)<br/>
            + wsClose(operationId)<br/>
            <b>Control:</b><br/>
            + cancel(id)<br/>
            + setUserAgent(userAgent)
        </div>
    "]:::netsec;
    
    WebsocketSession["WebsocketSession"]:::netsec
    HttpResult["HttpResult"]:::core
    
    Http --> |"manages"| WebsocketSession
    Http --> |"creates"| HttpResult
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
```
<!-- /mermaid-diagram -->

## Diagram: HTTP Request Flow (Advanced Sequence)

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant App
    participant Http
    participant Session
    participant Server
    participant Callback
    
    Note over App,Callback: HTTP GET Request
    App->>Http: get(url, timeout)
    Http->>Session: Create session
    Session->>Server: HTTP GET request
    alt Request succeeds
        Server-->>Session: HTTP 200 OK + data
        Session->>Session: Parse response
        Session->>Callback: onSuccess(result)
        Callback-->>App: HttpResult
    else Request timeout
        Session->>Session: Timeout occurred
        Session->>Callback: onError(timeout)
        Callback-->>App: Error result
    else Request failed
        Session->>Session: Connection error
        Session->>Callback: onError(error)
        Callback-->>App: Error result
    end
    
    Note over App,Callback: HTTP POST Request
    App->>Http: post(url, data, timeout, isJson)
    Http->>Session: Create session
    opt JSON data
        Session->>Session: Set Content-Type: application/json
    end
    Session->>Server: HTTP POST request + data
    Server-->>Session: HTTP response
    Session->>Callback: onComplete(result)
    Callback-->>App: HttpResult
    
    Note over App,Callback: WebSocket Connection
    App->>Http: ws(url, timeout)
    Http->>Session: Create WebSocket session
    Session->>Server: WebSocket handshake
    alt Handshake succeeds
        Server-->>Session: WebSocket accepted
        Session->>Session: Upgrade to WebSocket
        Session-->>App: operationId
        par WebSocket communication
            loop While connected
                App->>Session: wsSend(operationId, message)
                Session->>Server: Send message
                Server-->>Session: Receive message
                Session->>Callback: onMessage(message)
            end
        and Server messages
            loop While connected
                Server->>Session: Send message
                Session->>Callback: onMessage(message)
            end
        end
        opt Close connection
            App->>Session: wsClose(operationId)
            Session->>Server: Close frame
            Server-->>Session: Close acknowledgment
        end
    else Handshake failed
        Session->>Callback: onError(handshake failed)
        Callback-->>App: Error
    end
```
<!-- /mermaid-diagram -->
