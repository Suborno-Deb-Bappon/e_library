# e_library

## Overview

e_library is a Python-based e-library application that allows users to search, borrow, and return e-books. It provides features such as a book catalog with filters, user accounts, borrowing limits, and book reviews.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/e_library.git
    cd e_library
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    While the provided data lacks specific dependencies, a typical Django project requires installing dependencies using pip. If a `requirements.txt` file exists (not mentioned in given data), use it. Otherwise install Django.

    ```bash
    pip install django
    ```

    If a `requirements.txt` file is present, use this instead:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/` in your web browser.

## Usage

1.  **Access the application:** Open your web browser and navigate to `http://127.0.0.1:8000/`.

2.  **Explore the book catalog:** Browse available e-books. Use the provided filters to narrow down your search.

3.  **User accounts:** Create a new user account or log in with an existing one.

4.  **Borrow books:** Borrow available books, subject to borrowing limits.

5.  **Return books:** Return borrowed books.

6.  **Book reviews:** Read and submit reviews for books.

7.  **Admin interface:** Access the admin interface at `http://127.0.0.1:8000/admin/` to manage books, users, and other application settings. Use the superuser credentials created during installation.

## Features

*   **Book catalog:** Browse a wide selection of e-books.
*   **Book filters:** Filter books by title, author, genre, etc.
*   **User accounts:** User registration, login, and profile management.
*   **Borrowing limits:** Manage the number of books a user can borrow.
*   **Book reviews:** Users can submit and view book reviews.
*   **Admin interface:** Manage books, users, and other application settings.
*   **Search Functionality:** Users can easily search for books by keywords.

## Directory Structure

```
e_library/              # Core application logic
e_library_project/      # Project-level settings and configurations
media/                  # Stores uploaded media files (e.g., book covers)
static/                 # Stores static files (e.g., CSS, JavaScript)
venv/                   # Virtual environment directory (if created)
db.sqlite3              # The SQLite database file
manage.py               # Django's management script for running commands
```