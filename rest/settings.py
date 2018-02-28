MONGO_HOST = 'Localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'myplatform_db'
DOMAIN = {
    'myplatform': {
        'schema': {
            'sysname': {
                'type': 'string'
            },
            'osystem': {
                'type': 'string'
            },
            'memory': {
                'type': 'string'
            },
            'processor': {
                'type': 'string'
            },
            'diskspace': {
                'type': 'string',
                 'unique': True
            }
        }
    }
}
RESOURCE_METHODS = ['GET','POST']

