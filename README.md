# 🕸️ Network Programming Toolkit in Python

Welcome to the **Network Programming Toolkit**, a hacker-terminal-inspired collection of essential networking tools and educational projects built using **pure Python**. This repo is a one-stop practical guide to help you understand and implement core networking concepts like TCP/UDP communication, netcat-like functionality, socket proxying, and even SSH tunneling with Paramiko.

> ⚠️ All tools are built to work in restricted or hardened environments — where tools like `netcat`, `wireshark`, or compilers are unavailable — but Python is present.

---

## 📁 Project Structure

```
.
├── SSH with Paramiko/
│   ├── sshrcmd.py        # Reverse SSH client
│   └── sshserver.py      # SSH server using Paramiko
├── Understanding of TCP UDP/
│   ├── tcpClient.py      # Basic TCP client
│   ├── tcpServer.py      # Basic TCP server (multi-threaded)
│   └── udpClient.py      # Basic UDP client
├── netcat.py             # Python replacement for netcat with shell, upload, execute
├── proxy.py              # TCP proxy with hexdump and packet interception
├── sshcmd.py             # Paramiko-based SSH command executor
```

---

## ✨ Features

### ✅ TCP/UDP Fundamentals

* Learn raw socket programming using Python’s `socket` module.
* Build your own **TCP/UDP clients and servers**.
* Multi-threaded TCP server capable of handling multiple clients concurrently.

### 🧰 Netcat Clone (`netcat.py`)

* Upload files, spawn remote command shells, or execute specific commands — just like netcat.
* Works in both **client** and **server** mode.
* Can be used to tunnel basic shell access over TCP using only Python.

### 🔄 TCP Proxy (`proxy.py`)

* Intercept, inspect (via hexdump), and optionally modify traffic between two endpoints.
* Great for debugging, fuzzing, or analyzing unknown protocols.
* Customize requests and responses via intercept handlers.

### 🔐 SSH Toolkit (via Paramiko)

* `sshcmd.py`: Execute commands remotely over SSH (similar to `ssh user@host 'command'`).
* `sshrcmd.py`: Reverse SSH shell — client connects to your Python SSH server and receives commands.
* `sshserver.py`: Minimal custom SSH server (useful on Windows clients without SSH services).

### 🔁 SSH Reverse Tunneling (Coming Soon: `rforward.py`)

* Tunnels internal network traffic to external systems via SSH reverse port forwarding.
* Ideal for situations where direct access is blocked but SSH is allowed.

---

## 🔧 Getting Started

### 🐍 Prerequisites

* Python 3.6+
* Paramiko (for SSH tools)

```bash
pip install paramiko
```

---

## 🚀 Usage Examples

### 🔌 TCP Client

```bash
python Understanding\ of\ TCP\ UDP/tcpClient.py
```

### 🖥️ TCP Server

```bash
python Understanding\ of\ TCP\ UDP/tcpServer.py
```

### 🛰️ UDP Client

```bash
python Understanding\ of\ TCP\ UDP/udpClient.py
```

### 🛠️ Netcat-like Tool

```bash
# Command shell listener
python netcat.py -t 0.0.0.0 -p 5555 -l -c

# Client shell access
python netcat.py -t 127.0.0.1 -p 5555
```

### 📡 TCP Proxy

```bash
# Example: Forward local port 9000 to 10.0.0.1:80
python proxy.py 127.0.0.1 9000 10.0.0.1 80 False
```

### 🔐 Paramiko SSH Command

```bash
python sshcmd.py
# Enter host, port, credentials, and the command to execute
```

### 🔁 Reverse SSH Client & Server

* First, run the server:

```bash
python sshserver.py
```

* Then, on the client machine:

```bash
python sshrcmd.py
```

---

## 🧠 Why This Project Matters

When you're dropped into a hardened environment with no dev tools, no `netcat`, and limited access — **but Python is available** — this toolkit becomes your Swiss Army Knife. It's also a fantastic way to:

* Learn socket programming
* Understand TCP/UDP fundamentals
* Simulate reverse shells and SSH tunneling
* Debug live traffic using your own proxy

---

## 🔒 Disclaimer

> This repository is strictly for educational purposes and ethical cybersecurity training. Any misuse of the content for malicious purposes is against the intent of this project.

---

## 👨‍💻 Author

**Tanishq Arun Ingole**
🎓 BTech CSE @ IIIT Pune | 💻 Ethical Hacker | 🎮 Game Developer
🔗 [LinkedIn](https://www.linkedin.com/in/tanishq-ingole-161a7926b/) | 🌐 [GitHub](https://github.com/imcoder44)

---


