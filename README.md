# First Fast API Project

This repository is a small example FastAPI backend with a React frontend for managing products (simple inventory UI).

Overview
 - Backend: FastAPI app exposing a `/products/` CRUD API (see `main.py`, `database.py`, `database_models.py`, `models.py`).
 - Frontend: React app in the `frontend/` folder providing a product management UI.

Quick links
 - Backend entry: `main.py`
 - Frontend: `frontend/src/App.js`

Prerequisites
 - Python 3.10+ (virtualenv/venv recommended)
 - Node.js 16+ (for the frontend)
 - Recommended: create and activate a virtual environment before installing Python deps

Clone the repo
```bash
git clone <your-repo-url>
cd first_fast_api_project
```

Backend: setup and run
1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
# Windows (Powershell)
.\.venv\Scripts\Activate.ps1
# Windows (cmd)
.\.venv\Scripts\activate.bat
# macOS / Linux
source .venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend (development):

```bash
uvicorn main:app --reload
```

Notes:
 - Use `uvicorn main:app --reload` for automatic reloads while developing the backend.
 - The backend listens on `http://127.0.0.1:8000` by default.
 - Swagger UI is available at `http://127.0.0.1:8000/docs` and the ReDoc UI at `/redoc`.

Frontend: setup and run
1. Change into the frontend folder and install dependencies:

```bash
cd frontend
npm install
```

2. Start the React dev server:

```bash
npm start
```

3. The app will open at `http://localhost:3000` (or the port reported by the dev server). The frontend expects the backend API at `http://localhost:8000` by default (see `frontend/src/App.js`).

Key differences: `npm start` vs `uvicorn`
 - `npm start` runs the React development server (hot reload, serves the UI).
 - `uvicorn main:app --reload` runs the FastAPI backend (API server).

Pydantic and data validation
 - The project uses Pydantic models to validate and serialize request/response data in the FastAPI backend.
 - See `models.py` (or `database_models.py`) for the model definitions and how requests are validated.

Testing and linting
 - There are no automated tests included by default. To add tests, create a `tests/` folder and use `pytest`.
 - You can run linters like `flake8` / `pylint` and formatters like `black` to keep code consistent.

Contributing
 - Fork the repository and open a pull request with a clear description of your change.
 - Add tests for any bugfixes or features when possible.

Troubleshooting
 - If the frontend can't reach the backend, ensure the backend is running and that CORS is configured (FastAPI includes CORS middleware when needed).
 - If package installation fails on Windows, ensure you have build tools installed (for binary dependencies like `psycopg2` consider using the `psycopg2-binary` wheel).

License & contact
 - Add a LICENSE file if you wish to make this project public with a specific license.
 - For questions, include contact information or open an issue in the repository.

More improvements (suggested)
 - Add an environment configuration (`.env`) and a simple `Makefile` or npm scripts to streamline start/build steps.
 - Add tests and CI configuration (GitHub Actions) to run linting and tests on push.
 - Add a CONTRIBUTING.md with contributor guidelines and a code of conduct.
