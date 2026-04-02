# 🛠️ AntiGravity-MCP

A powerful, dual-transport Model Context Protocol (MCP) server that enables your AI agents to securely read and write files within a sandbox environment.

## 🌟 Features

-   **Dual-Transport Support**: Optimized for both local (stdio) and remote (SSE) environments.
-   **Sandboxed Environment**: All file operations are restricted to a defined `/sandbox` directory.
-   **Full CRUD**: Create, read, and delete files remotely.
-   **FastMCP-Powered**: Built using the high-performance Python MCP SDK.

---

## 🚀 Getting Started

### 1. Installation

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

```bash
cd mcp-server
uv sync
```

### 2. Choose Your Mode

#### **A. Local Mode (stdio)**
*Best for use with Antigravity, Claude Desktop, or local MCP clients.*

Run the server directly without any flags:
```bash
uv run mcp_server.py
```

#### **B. Remote Mode (SSE + ngrok)**
*Required for integration with ChatGPT Connectors.*

1.  **Start the SSE Server**:
    ```bash
    uv run mcp_server.py --sse
    ```
    *(Defaults to `0.0.0.0:8080` to avoid common macOS system conflicts.)*

2.  **Start the Tunnel**:
    ```bash
    ngrok http 127.0.0.1:8080
    ```

3.  **Update ChatGPT**:
    Use the public URL provided by ngrok (ending in `/sse`):
    `https://your-domain.ngrok-free.dev/sse`

---

## ⚙️ Configuration Details

-   **Mount Point**: The server listens on `0.0.0.0:8080`.
-   **Transport**: Uses `server-sent-events` (SSE) for remote tunneling.
-   **Sandbox Paths**: `/Users/abhisheks/Desktop/Projects/learndocker/mcp-server/sandbox`

---

## 🛠️ Troubleshooting

-   **Port 8000 Issue**: On macOS, port 8000 is often used by system services like AirPlay. We use **8080** by default for maximum compatibility.
-   **ngrok Domains**: If your ChatGPT connector appears "offline", ensure the domain suffix matches your ngrok status exactly (e.g., `.dev` vs `.app`).
-   **Invalid Character 'I' Error**: This occurs when uvicorn logs are sent to stdout in stdio mode. Ensure you use the `--sse` flag when running via a terminal.

---

## 📜 License

MIT License - 2026 Abhishek Sar
