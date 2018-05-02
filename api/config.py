import os


# API envvars

APP_PORT = int(os.getenv('APP_PORT', 5000))

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
MONGO_TIMEOUT = int(os.getenv('MONGO_TIMEOUT', 2))
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'backend_dito')
EVENTS_COLLECTION = os.getenv('EVENTS_COLLECTION', 'events')

DATETIME_FORMAT = os.getenv('DATETIME_FORMAT', "%Y-%m-%dT%H:%M:%S.%f")


# script envvars

INSERT_DOCS_QTY = int(os.getenv('INSERT_DOCS_QTY', 100))
BULK_INSERTION_QTY = int(os.getenv('INSERT_DOCS_QTY', 20))
