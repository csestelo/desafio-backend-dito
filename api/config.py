import logging
import os


# API envvars
from simple_json_logger import JsonLogger

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

REDIS_URI = os.getenv('DITO_REDIS_URI', '127.0.0.1')
REDIS_PORT = int(os.getenv('DITO_REDIS_PORT', 6379))
REDIS_NAMESPACE = os.getenv('DITO_REDIS_NAMESPACE', 'dito')
REDIS_TIMEOUT = int(os.getenv('DITO_REDIS_TIMEOUT', 5))
REDIS_MIN_POOL_SIZE = int(os.getenv('DITO_REDIS_TIMEOUT', 5))
REDIS_MAX_POOL_SIZE = int(os.getenv('DITO_REDIS_MAX_POOL_SIZE', 10))

REDIS_TTL = int(os.getenv('DITO_REDIS_TTL', 60))

REDIS_PARAMS = dict(endpoint=REDIS_URI,
                    port=REDIS_PORT,
                    namespace=REDIS_NAMESPACE,
                    create_connection_timeout=REDIS_TIMEOUT,
                    pool_min_size=REDIS_MIN_POOL_SIZE,
                    pool_max_size=REDIS_MAX_POOL_SIZE
                    )

# script envvars

INSERT_DOCS_QTY = int(os.getenv('DITO_INSERT_DOCS_QTY', 100))
BULK_INSERTION_QTY = int(os.getenv('DITO_BULK_INSERTION_QTY', 20))

# logs
LOG_LEVEL = int(os.getenv('SIEVE_LOG_LEVEL', logging.DEBUG))
logger = JsonLogger(level=LOG_LEVEL)
