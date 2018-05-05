import os


# API envvars

APP_PORT = int(os.getenv('DITO_APP_PORT', 5000))

MONGO_URI = os.getenv('DITO_MONGO_URI', 'mongodb://localhost:27017')
MONGO_TIMEOUT = int(os.getenv('DITO_MONGO_TIMEOUT', 2))
MONGO_MAX_POOL_SIZE = int(os.getenv('DITO_MONGO_MAX_POOL_SIZE', 200))
MONGO_MIN_POOL_SIZE = int(os.getenv('DITO_MONGO_MIN_POOL_SIZE', 50))

MONGO_PARAMS = dict(
    host=MONGO_URI,
    serverSelectionTimeoutMS=MONGO_TIMEOUT,
    maxPoolSize=MONGO_MAX_POOL_SIZE,
    minPoolSize=MONGO_MIN_POOL_SIZE
)

MONGO_DB_NAME = os.getenv('DITO_MONGO_DB_NAME', 'backend_dito')
EVENTS_COLLECTION = os.getenv('DITO_EVENTS_COLLECTION', 'events')

DATETIME_FORMAT = os.getenv('DITO_DATETIME_FORMAT', "%Y-%m-%dT%H:%M:%S.%f")


# script envvars

INSERT_DOCS_QTY = int(os.getenv('DITO_INSERT_DOCS_QTY', 100))
BULK_INSERTION_QTY = int(os.getenv('DITO_BULK_INSERTION_QTY', 20))
