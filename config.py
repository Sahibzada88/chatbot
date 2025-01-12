# gunicorn_config.py

import multiprocessing

bind = "0.0.0.0:8001"  # IP and port to bind the server
workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes
worker_class = "uvicorn.workers.UvicornWorker"  # Worker class for handling requests
threads = multiprocessing.cpu_count() * 2  # Number of threads per worker
worker_connections = 1000  # Maximum number of simultaneous clients
timeout = 3000  # Timeout for worker processes
keepalive = 3000  # Time in seconds to keep an idle client connection open
max_requests = 1000  # Maximum number of requests a worker will process before restarting
max_requests_jitter = 50  # Randomize max_requests by this much
graceful_timeout = 300  # Timeout for graceful worker shutdown
loglevel = "debug"