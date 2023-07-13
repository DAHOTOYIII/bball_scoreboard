# bball_scoreboard

## Getting Started
### Follow the steps below for collaboration
1. Clone this repo
2. Open a terminal
3. Setup your dev environment this requires virtual environment
```python -m venv venv```
4. Activate your virtual environment ```venv\Scripts\activate.ps1```
4. Run command ```pip install -r requirements.txt```

### For Developers
#### Run script command
``` python .\pc_scoreboard\main.py ```
### Git reminders
> Create your own branch do not update the main branch


# Getting Started with Web for Developers

1. In terminal run: 
``` cd .\web\bball_scoreboard\ ```
2. Ensure that django is installed. You may check by running ``` django-admin --version ```
3. Run ``` pyton manage.py migrate ```
4. Create superuser by running ``` python manage.py createsuperuser ```
5. Supply the needed information.
6. Run ``` python manage.py runserver ``` > Then the website should be accessible by http://127.0.0.1:8000/

>> django administration should be accessible by http://127.0.0.1:8000/admin/login/?next=/admin/