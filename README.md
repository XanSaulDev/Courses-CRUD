# Django Project: Courses-CRUD

This is a simple Django project that includes a  `requirements.txt` file with the necessary dependencies. Follow these steps to set up and run the project.
![image](https://github.com/XanSaulDev/Courses-CRUD/assets/90731443/66375ce2-2f26-4049-86bc-7934058a4c48)

## Steps to Run the Project

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

On Unix-based systems (Linux/macOS):

```bash
source venv/bin/activate
```
On Windows (PowerShell):

```bash
.\venv\Scripts\Activate
```

### 3. Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```
### 4. Perform Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the Development Server

```bash
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/. You can access the application in your web browser.
