class Config:
    SECRET_KEY = 'secretkey123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/allergy_diner'
