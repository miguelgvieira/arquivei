# -*- coding: utf-8 -*-

from http import HTTPStatus
import json

from flask import jsonify
from flask_smorest import Blueprint

from project.api.nfe import nfe_bo

nfe_api = Blueprint(
    'Nfe',
    'nfe_rest',
    url_prefix="/api/v1/nfe",
    description="Nfe checking of the Arquivei API.",
)

@nfe_api.route('/arquivei', methods=['POST'])
@nfe_api.response(
    code=HTTPStatus.CREATED,
    description='Get all nfes from an Endpoint and save'
)
def get_nfe_arquivei():
    """
    Pega as nfes de um endpoint da arquive, e salva no banco de dados
    """

    response = nfe_bo.get_nfe_arquivei_and_save()

    return response

@nfe_api.route('/', methods=['GET'])
@nfe_api.response(
    code=HTTPStatus.OK,
    description='Get all nfes from database'
)
def get_all():
    """
    Pega todas as nfes do banco de dados
    """

    response = nfe_bo.read_all()

    return json.dumps(response)

@nfe_api.route('/access_key/<access_key>', methods=['GET'])
@nfe_api.response(
    code=HTTPStatus.OK,
    description='Get a nfe from database'
)
def get_one(access_key):
    """
    Pega a nfe do banco com a access_key recebida
    """

    response = nfe_bo.read_one(access_key)

    return json.dumps(response)
