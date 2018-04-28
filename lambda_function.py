import os
import sys

# HACK: Include 'libs' dir to PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'libs'))

from stravalib import Client


def lambda_handler(event, context):
    code = event['code']
    exchange_mode, exchange_opt = event['state'].split('-')

    client = Client()
    access_token = client.exchange_code_for_token(
        client_id=os.environ.get('STRAVA_CLIENT_ID'),
        client_secret=os.environ.get('STRAVA_CLIENT_SECRET'),
        code=code
    )

    if exchange_mode == 'REDIRECT':
        return {
            'location': f'http://127.0.0.1:{exchange_opt}?access_token={access_token}'
        }
