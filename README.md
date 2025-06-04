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
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- Python 3.8+
- pip
- virtualenv (Optional, but recommended)

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    The application will typically create the `database.db` SQLite file on its first run if it doesn't exist.
    ```bash
    flask run
    ```
    The backend server will usually start on `http://127.0.0.1:5000/`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Start the development server:**
    ```bash
    npm run dev
    ```
    Alternatively, `npm start` might be configured to run the dev server.
    The frontend development server will usually start on `http://localhost:5173/`.

## API Endpoints

The backend exposes several API endpoints for managing users, recipes, ingredients, and favorites. Key blueprints include:

-   `/recipes`: Recipe management (CRUD operations, ingredient listing).
-   `/user`: User management (listing, deletion, password updates, user-specific recipes).
-   `/favorites`: Favorite recipe management for logged-in users.
-   `/login`, `/register`, `/logout`: User authentication.
-   `/ingredients`: Ingredient management (CRUD operations, recipes by ingredient, ingredients by category).

For detailed information on request/response formats and specific routes, please refer to the API route definitions in the `backend/app/api/` directory (e.g., `recipe.py`, `user.py`).

## Database

The backend uses Flask-SQLAlchemy with a SQLite database (`database.db`) by default. The database schema includes tables for:
-   `User`: Stores user information.
-   `Recipe`: Stores recipe details.
-   `FavoriteRecipe`: Maps users to their favorite recipes.
-   `UserRecipe`: Maps users to recipes they have created.
-   `Ingredients`: Stores ingredient details.
-   `RecipeIngredient`: Maps recipes to their ingredients.

## Authentication

User authentication is handled using Flask-JWT-Extended. Access tokens are generated upon login and are required for protected routes. A Redis-based blocklist is implemented for token revocation on logout.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
