# config.py
class Config:
    SECRET_KEY = 'your-secret-key'#nigga หน้าดำ
    JWT_SECRET_KEY = 'your-jwt-secret'#nigga หน้าเผือก
    MONGODB_SETTINGS = {
        'db': 'mario_notes',
        'host': 'localhost',
        'port': 27017
    }