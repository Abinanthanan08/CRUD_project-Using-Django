👤 Django User Management with Stored Procedures

A simple Django app to perform **CRUD** operations on users using **stored procedures** from the database.

## 🔧 Features

- Add new users
- View list of users
- Update user details
- Delete users
- Uses raw SQL and stored procedures for database operations

## 🛠 Tech Stack

- Python 3.x
- Django
- SQL (with stored procedures)
- HTML templates (for forms and views)
  

##🚀 How to Run


## 1.Clone the repository
```bash
git clone https://github.com/Abinanthanan08/CRUD_project-Using-Django.git
cd CRUD_project-Using-Django
```
## 2.Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
## 3.Install dependencies
```bash
pip install -r requirements.txt
```
## 4.Configure the database
In settings.py, update the database configuration:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
## 5.Run migrations
```bash
python manage.py migrate
```
## 6.Start the development server
```bash
python manage.py runserver
```
## 7.Access the app
Open your browser and go to:
http://127.0.0.1:8000/



