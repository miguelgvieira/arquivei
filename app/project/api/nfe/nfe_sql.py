'''
    Arquivo para gerar as SQLs para inserir e recuperar dados
        no banco de dados.
'''

def create(nfe_list):
    sql_string = f'''
        INSERT INTO nfe_value
            (access_key, total_value)
        VALUES
    '''
    for nfe in nfe_list:
        access_key = nfe['access_key']
        total = nfe['total']
        sql_string = sql_string + f'({access_key},{total})'
    sql_string = sql_string + ';'
    sql_string = sql_string.replace(')(', '),(')
    return sql_string

def read_all():
    return 'SELECT * FROM nfe_value'

def read_one(access_key):
    return f'''
        SELECT *
        FROM
            nfe_value
        WHERE
            access_key = {access_key}
        '''