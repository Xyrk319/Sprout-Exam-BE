# Sprout-Exam-BE

This is the backend of the technical exam as part of the recruitment process of Sprout Solutions. 


The frontend is on a separate repository which is built using FastApi: [Backend Repository](https://github.com/Xyrk319/Sprout-Exam)

Additionally, the application is currently hosted which you can access through this [Link](https://sprout-exam.onrender.com/)

## Local Environment


```
Steps in Running the program
1. pip install -r requirements.txt
2. alembic upgrade head
3. python -m app.commands.seed
4. uvicorn app.main:app --reload

Note: The app require an .env file to run

Set the following variables in your own .env

APP_SECRET_KEY=lorem
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=primary_app_db
DB_USERNAME=root
DB_PASSWORD=
SESSION_LIFETIME=120 # this is in minutes

```
## Tech
```
pip 24.0
python 3.9.7
```
