# Architecture Overview

The Smart Attendance System is designed to be simple, beginner-friendly, and maintainable.

## Architecture Pattern
**Client-Server Architecture with Layered Backend**

```text
[ React Frontend ] (Vite, Axios, JSX)
       │
       │ HTTP/REST JSON
       ▼
[ FastAPI Backend Routes ] (API Endpoints, Input Validation)
       │
       │ Python Function Calls
       ▼
[ Backend Services ] (Business Logic)
    │           │
    │           └──▶ [ Face Recognition Service ] ──▶ [ models/encodings.pkl ]
    │
    └──▶ [ Attendance Service ] ──▶ [ data/attendance.csv ]
```

## Core Principles
1. **Separation of Concerns**: Frontend handles UI, Backend handles logic, Services handle specific tasks (like CV or Data I/O).
2. **Beginner Friendly**: No microservices, Docker, or complex message queues are required for this iteration.
3. **Plug-and-Play AI**: The Face Recognition model is isolated in its own service. You simply place your `encodings.pkl` in `models/` and the application bridges the gap.
