# 🧠 Cloud IDE (MVP)

A WebSocket-powered cloud IDE backend built using **Django + Channels + Docker**, inspired by platforms like [Replit](https://replit.com/).
Each user/project has an isolated terminal running in its own Docker container.

---

## ✅ Features

- 🔌 Real-time terminal over WebSocket using Django Channels
- 🐳 Containerized per-user shell using Docker
- 🧼 Clean bash shell (no zsh/macOS junk)
- ⚙️ Configurable project workspaces
- 📦 Fully Dockerized with Pipenv

---

## 🚀 Project Structure

```
cloud_ide/
├── core/              # Django app
│   ├── consumers/     # WebSocket logic
│   └── terminal/      # Terminal process + utils
├── config/            # Django settings + ASGI
├── runner/            # Dockerfile for per-project containers
├── user_projects/     # Project-specific workspaces
├── Pipfile            # Python dependencies (Pipenv)
├── docker-compose.yml
├── Makefile           # Easy build/run commands
```

---

## 📦 Setup

> **Requires:** Docker, Docker Compose, Pipenv

### 1. Clone & Build

```bash
git clone https://github.com/your-username/cloud-ide.git
cd cloud-ide
make build
```

### 2. Start the App

```bash
make up
```

### 3. Connect to Terminal

Use Postman or a frontend client to connect:

```
ws://localhost:8000/ws/terminal/<project_id>/
```

Send commands like: `ls`, `pwd`, `touch file.py`, etc.

---

## 🧪 Testing a Container

To test a project-specific container directly:

```bash
docker run -it -v $(pwd)/user_projects/project123:/workspace cloudide-runner
```

---

## 🔧 Commands

| Command      | Description                           |
| ------------ | ------------------------------------- |
| `make build` | Build Docker image                    |
| `make up`    | Start Django + Daphne                 |
| `make down`  | Stop services                         |
| `make logs`  | Stream container logs                 |
| `make bash`  | Open a shell inside the app container |

---

## 📈 Roadmap

- [x] Terminal WebSocket MVP
- [x] Clean bash prompt in Docker
- [ ] Editor WebSocket sync
- [ ] Container-per-project orchestration
- [ ] File save/persistence API
- [ ] User authentication + JWT
- [ ] Deployment on ECS / Railway / DO App

---

## 🧠 Inspiration

- [Replit](https://replit.com/)
- [Node-PTY](https://github.com/microsoft/node-pty)
- [Django Channels](https://channels.readthedocs.io/)

---

## 📄 License

MIT – do whatever you want.

---

Let me know if you'd like a version with GitHub badges or want to publish this as a template repo.
Shall we move on to building the `ContainerManager` Python class now?
