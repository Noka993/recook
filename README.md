# Recook

**Recook** is a full-stack web application that provides users with personalized recipe recommendations based on available ingredients.

## Features

- Responsive React frontend
- Flask REST API backend

## Project Structure

```
recook/
├── backend/    # Flask API
├── frontend/   # React app
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- Python 3.8+
- pip
- [Optional: virtualenv]

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```
