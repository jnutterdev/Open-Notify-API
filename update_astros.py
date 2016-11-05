"""One-off set the current astronauts in space. Edit the list and run once to update
"""
from redis import StrictRedis
import json

# Redis connection
redis = StrictRedis(host='localhost', port=6379)

astros = [
    {'name': "Jing Haipeng",            'craft': "Shenzhou 11"},
    {'name': "Chen Dong",               'craft': "Shenzhou 11"},
    {'name': "Sergey Rizhikov",         'craft': "ISS"},
    {'name': "Andrey Borisenko",        'craft': "ISS"},
    {'name': "Shane Kimbrough",         'craft': "ISS"},
]

redis.set('people-in-space', json.dumps({'message': "success", 'number': len(astros), 'people': astros}))
