# Django Project

## Overview

This is a Django project designed to manage tasks. It includes CRUD operations for tasks and a simple API.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.10
- You have installed pip (Python package installer)
- You have installed virtualenv

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pbrandl/oped.git
    cd oped
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database:**

    Apply the migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

### CORS Troubleshooting

In combination with Flutter you may need to add your port as `localhost:xxxx` in `opeddjango/settings.py` in `CORS_ALLOWED_ORIGINS` to use the API.  

