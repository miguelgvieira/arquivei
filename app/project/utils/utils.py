import base64

import xmltodict
from nested_lookup import nested_lookup

def xml_to_dict(xml_info):
    return xmltodict.parse(xml_info)

def decode_response(nfe_dict):
    for nfe in nfe_dict:
        xml_information = base64.b64decode(str(nfe['xml']))
        nfe['xml'] = xml_to_dict(xml_information.decode('utf-8'))

    return nfe_dict

def find_key(full_dictionary, key):
    return nested_lookup(key, full_dictionary)[0]
