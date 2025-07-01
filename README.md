# E-Library Application

## Overview

This is an e-library application that allows users to search, borrow, and return e-books. It provides features such as a book catalog with filters, user accounts, borrowing limits, and book reviews.

## Key Features

*   **Book Catalog:** Browse a wide selection of e-books.
*   **Search and Filters:** Easily find books by title, author, or genre.
*   **User Accounts:** Create and manage personal accounts.
*   **Borrowing System:** Borrow and return e-books with defined limits.
*   **Book Reviews:** Read and write reviews for books.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/e_library.git
    cd e_library
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies (if any, specify them here. Assuming standard Django setup):**

    ```bash
    pip install django
    pip install -r requirements.txt #If requirements.txt exist. Otherwise, install dependencies like Pillow if media files processing is needed
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (admin) account:**

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the application in your web browser:**

    Open your web browser and navigate to `http://127.0.0.1:8000/` (or the address shown in your terminal).

3.  **Admin Interface:**

    Access the admin interface at `http://127.0.0.1:8000/admin/` to manage books, users, and other data. Use the superuser credentials created earlier.

## Project Structure

*   `db.sqlite3`: SQLite database file.
*   `manage.py`: Django management script.
*   `elibrary/`: Main application directory. Contains models, views, forms, etc.
*   `elibrary_project/`: Django project settings and configurations.
*   `media/`: Directory for storing uploaded media files (e.g., book covers).
*   `static/`: Directory for storing static files (e.g., CSS, JavaScript).
*   `venv/`: Virtual environment directory (if created).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

[Specify the license here. E.g., MIT License]