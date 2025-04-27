import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '4b0d4d0a0895e08f6dcd817a164be6fa78bb82d96d6fcd0179180be2e82aa09d')
    SESSION_COOKIE_NAME = 'mood_analyzer_session'
