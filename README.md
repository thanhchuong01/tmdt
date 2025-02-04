# Milk-tea website (Project E-commere)

How to run ?

1. Clone project: https://github.com/thanhchuong01/tmdt.git
2. [Install Django framework](https://docs.djangoproject.com/en/4.2/topics/install/)
3. Follow: 
  - If use VSCode allow \venv\Scripts\activate 
  - At milk_tea directory 
  ```pip install -r requirements.txt ```
   ***or*** ```python -m pip install -r requirements.txt```  
 4. Config your database in file _settings.py_  at DATABASE
   > I use Postgres, port 5432, local account
 5. Delete all file in ***migrations*** forlders
 6. Run the command: ```python manage.py makemigrations``` <br>
for check the change of database model
 7. Next ```python manage.py migrate``` <br> it will install databse model into database management system ***setting.py***
 8. Next```python manage.py createsuperuser``` <br>
to create admin account of systems, you use that account to login on Admin side of Django 
9. Finally, run ```python manage.py runserver ``` <br>
the server Django will run on localhost and auto open default Web brower, run project! 
=======

