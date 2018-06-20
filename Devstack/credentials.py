import os

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = 'admin'
    d['password'] = 'Huy27101997'
    d['auth_url'] = 'http://192.168.201.133/identity'
    d['project_id'] = 'default'
    return d