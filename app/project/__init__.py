import logging

from flask import Flask

from project.utils.middlewares import configure_middlewares

app = Flask(__name__)

def create_app():
    """
    Cria nossa aplicação Flask
    """
    logging.debug("Iniciando servidor Flask")

    app = Flask(__name__, instance_relative_config=True)

    configure_middlewares(app)

    return app
    