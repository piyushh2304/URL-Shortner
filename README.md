# 🔗 Scalable URL Shortener with React & FastAPI

A modern, full-stack URL shortener application featuring a sleek React frontend powered by Vite and a highly efficient, asynchronous-capable FastAPI backend with SQLite database persistence and SQLAlchemy ORM.

---

## 🚀 Features

- **Instant URL Shortening**: Paste any valid URL and receive a compact, shareable short link instantly.
- **Custom Aliases**: Choose a custom, memorable word/slug for your short links (validated to ensure alphanumeric characters only).
- **Click Tracking & Analytics**: Automatically tracks the number of times each shortened URL is accessed.
- **Automatic Redirection**: Accessing the short link seamlessly redirects users to their original destination.
- **Responsive Web Interface**: Sleek, distraction-free modern UI styled for a seamless user experience.

---

## 🛠️ Tech Stack

### Frontend
- **React 19**: Modern declarative UI library.
- **Vite**: Ultra-fast frontend build tool and dev server.
- **Axios**: Promised-based HTTP client for seamless API requests.
- **Vanilla CSS**: Clean, responsive styles with curated typography.

### Backend
- **FastAPI**: Modern, high-performance web framework for building APIs with Python 3.8+.
- **SQLAlchemy**: Feature-rich SQL toolkit and Object Relational Mapper (ORM).
- **Pydantic**: Robust data validation and settings management using Python type annotations.
- **SQLite**: Lightweight, serverless SQL database engine.

---

## 📂 Project Structure

```text
urlshortner/
├── backend/                  # FastAPI Backend Services
│   ├── main.py               # FastAPI Application entry point & routes
│   ├── models.py             # Pydantic schemas and request/response models
│   ├── database.py           # SQLAlchemy database configuration and models
│   ├── crud.py               # Database CRUD (Create, Read, Update, Delete) operations
│   ├── requirements.txt      # Python dependency list
│   ├── urls.db               # SQLite Database File (auto-generated)
│   └── venv/                 # Python Virtual Environment
│
└── frontend/                 # React Frontend Client
    ├── public/               # Static public assets
    ├── src/                  # React source files
    │   ├── assets/           # Client-side image assets
    │   ├── App.css           # Custom styling rules
    │   ├── App.jsx           # Main React component
    │   ├── index.css         # Global styles
    │   └── main.jsx          # React app entry point
    ├── index.html            # Vite entry HTML page
    ├── package.json          # Node project dependencies & scripts
    └── vite.config.js        # Vite compilation configuration
```

---

## 🔌 API Documentation

The backend service runs by default on `http://localhost:8000`.

### 1. Shorten a URL
- **Endpoint**: `POST /shorten`
- **Request Body**:
  ```json
  {
    "long_url": "https://www.google.com",
    "custom_alias": "google-search" // Optional
  }
  ```
- **Response**:
  ```json
  {
    "short_code": "google-search",
    "long_url": "https://www.google.com/",
    "short_url": "http://localhost:8000/google-search",
    "created_at": "2026-07-11T12:00:00.000000",
    "click_count": 0
  }
  ```

### 2. Redirect Short URL
- **Endpoint**: `GET /{short_code}`
- **Description**: Redirects the client to the matching long URL and increments the click counter by `1`.
- **Response**: `307 Temporary Redirect` (redirects to the original `long_url`).

### 3. Retrieve URL Statistics
- **Endpoint**: `GET /api/stats/{short_code}`
- **Description**: Returns analytics and metadata for a specific shortened code.
- **Response**:
  ```json
  {
    "short_code": "google-search",
    "long_url": "https://www.google.com/",
    "short_url": "http://localhost:8000/google-search",
    "created_at": "2026-07-11T12:00:00.000000",
    "click_count": 15
  }
  ```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher installed on your system.
- Node.js (v18+) and npm/pnpm installed.

---

### Backend Setup (FastAPI)

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Activate the Virtual Environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **macOS / Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Ensure you install FastAPI, Uvicorn, SQLAlchemy, and Pydantic:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

4. **Run the FastAPI server**:
   Start the FastAPI development server using Uvicorn:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   *The API will be available at `http://localhost:8000`.*

---

### Frontend Setup (React + Vite)

1. **Open a new terminal and navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node packages**:
   ```bash
   npm install
   ```

3. **Run the Vite development server**:
   ```bash
   npm run dev
   ```
   *The React UI will launch, typically at `http://localhost:5173`.*

---

## 🧪 Verification & Development

To test the integration:
1. Ensure both the frontend and backend servers are running.
2. Open `http://localhost:5173` in your browser.
3. Paste a long URL (e.g., `https://news.ycombinator.com`), enter an optional alias, and click **Shorten**.
4. Click on the generated short link to verify redirect and check if the click count increases.
