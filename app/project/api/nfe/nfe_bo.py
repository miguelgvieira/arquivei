from project.utils import arquivei_api, utils
from project.api.nfe import nfe_model

def get_nfe_arquivei_and_save():
    res = arquivei_api.get_data()
    if res == 'verb not allowed':
        return res

    response = res.json()

    nfes = utils.decode_response(response['data'])

    nfe_list = []
    for nfe in nfes:
        access_key = nfe['access_key']
        total_dict = utils.find_key(nfe, 'ICMSTot')

        total = [float(x) for x in list(total_dict.values())]

        nfe_filtered = {
            'access_key': access_key,
            'total': sum(total)
        }
        nfe_list.append(nfe_filtered)

    return nfe_model.create_many(nfe_list)

def read_all():
    return nfe_model.read_all()

def read_one(access_key):
    return nfe_model.read_one(access_key)