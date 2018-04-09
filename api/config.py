import os

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
EVENTS_COLLECTION = os.getenv('EVENTS_COLLECTION', 'events')
