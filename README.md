# Milk-tea website (Project E-commere)

How to run ?

1. Clone project
2. Install Django framework: 
   https://docs.djangoproject.com/en/4.2/topics/install/ 
4. Follow: 
  - If use VSCode allow \venv\Scripts\activate 
  - At milk_tea directory 
  ```pip install -r requirements.txt ```
   ***or*** ```python -m pip install -r requirements.txt```  
  - Config your database in file _settings.py_  at DATABASE
   > I use Postgres, port 5432, local account
  - Delete all file in ***migrations*** forlders
  - Run the command: ```python manage.py makemigrations``` 
for check the change of database model
  - Next ```python manage.py migrate``` 
Install databse model into database management system ***setting.py***
  - Next```python manage.py createsuperuser``` 
to create admin account of systems, you use that account to login on Admin side of Django 
  - Finally, run ```python manage.py runserver ```
the server Django will run on localhost and auto open default Web brower, run project! 
=======
# tmdt
