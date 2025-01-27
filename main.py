#!/usr/bin/env python3

# ---------------------------------------------------------
# Super-Best-Frame: Main flask application entry point
# Run with command: python3 main.py
# ---------------------------------------------------------

# Import all modules for app
import coloredlogs
import logging
from logging.handlers import RotatingFileHandler
import sys

from app import api  # Flask application
from gevent.pywsgi import WSGIServer

# Running flask server
if __name__ == '__main__':
    # Setting up log file handler
    file_handler = logging.handlers.RotatingFileHandler(filename='picture-frame.log', mode='w', maxBytes=10000000, backupCount=0)
    # Also include any sys.stdout in logs
    stdout_handler = logging.StreamHandler(sys.stdout)
    # Defining the logger
    logger = logging.basicConfig(level=logging.INFO,
                        format='[Super-Best-Frame] - [%(asctime)s] - %(levelname)-10s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        handlers=[file_handler, stdout_handler])
    # Applying color to the output logs
    coloredlogs.install(fmt='[Super-Best-Frame] - [%(asctime)s] - %(levelname)-10s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        logger=logger)

    logging.info('Starting flask server application (picture-frame) ...  ')
    logging.info('Web application port:  5555')

    # # NOTE: DEVELOPMENT: Using default flask server
    # logging.info('NOTE: Using default flask server (DEVELOPMENT ONLY)')
    # api.run(host='0.0.0.0', port=5555)

    # NOTE: PRODUCTION: Using gevent standalone Web Server Gateway Interface (WSGI) container
    logging.info('NOTE: Using gevent standalone Web Server Gateway Interface (WSGI) server for production deployment\n\n')
    http_server = WSGIServer(('', 5555), api, log=logging)
    http_server.serve_forever()

# NOTE: Enviromental variables and settings are set in .flaskenv
# NOTE: If it gets stuck use "fuser -k 5555/tcp"