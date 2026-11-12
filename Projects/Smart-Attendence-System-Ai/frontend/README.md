# Frontend Application

This is the React frontend for the Smart Attendance System, built with Vite.

## Features
- Dashboard with high-level statistics.
- Student listing based on AI model data.
- Full attendance history with search.
- Live camera integration for face recognition.
- Diagnostic settings page.

## Running Locally

1. Install dependencies:
```bash
npm install
```

2. Start the dev server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`.

## Architecture Note
- **`src/services/api.js`**: Contains all Axios calls to the FastAPI backend. Update the `VITE_API_URL` environment variable if your backend runs on a different port.
- **`src/pages/`**: Individual route components.
- **`src/layouts/`**: Contains `MainLayout.jsx` which renders the sidebar and handles routing outlet.
