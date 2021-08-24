from rest_framework.response import Response
from django.conf import settings

import requests


def get_movie_data_by_title(title):
    url = f'https://www.omdbapi.com/?t={title}&apikey={settings.OMDB_API_KEY}'
    response = requests.get(url)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return {
            'msg' : "Error: " + str(e),
            'status' : response.status_code
        }
    
    data = response.json()
    
    if data['Response'] == 'True':
        return {
            'result' : data,
            'status' : response.status_code
        }
    else:
        return {
            'msg' : data['Error'],
            'status' : 404
        }
    