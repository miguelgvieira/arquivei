import logging

from flask_smorest import Api

def configure_routes(app):
    """
    Configurando as rotas (Manualmente :-( )

    - app: Flask: Aplicação Flask.
    """
    logging.debug('Configurando as rotas')

    import project.api.nfe.nfe_rest as nfe_rest

    # Adicione aqui suas rotas...
    routes = [nfe_rest.nfe_api]

    api = Api(app)
    for blp in routes:
        api.register_blueprint(blp)

def configure_openapi(app):
    app.config['OPENAPI_VERSION'] = '3.0.2'

def configure_middlewares(app):
    """
    Ponto central para realizar as configurações do Flask.

    - app: Flask - Aplicação Flask.

    """
    logging.debug('Configurando aplicacao FLASK')

    configure_openapi(app)

    configure_routes(app)