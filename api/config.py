import os

APP_PORT = int(os.getenv('APP_PORT', 5000))

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
EVENTS_COLLECTION = os.getenv('EVENTS_COLLECTION', 'events')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'backend_dito')

