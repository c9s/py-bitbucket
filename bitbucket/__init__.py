import oauthlib
from requests_oauthlib import OAuth1Session, OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

import click
import pickle
import os
import sys
import yaml

import json

authorization_base_url = 'https://bitbucket.org/site/oauth2/authorize'
token_url = 'https://bitbucket.org/site/oauth2/access_token'


class BitBucketClient:
    def __init__(self, client_id, client_secret, token=None, scope=None, client=None):
        self.client = client if client else BackendApplicationClient(client_id=client_id)
        self.oauth = OAuth2Session(client=self.client, token=token, scope=scope)
        self.token = self.oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

    def hooks(self, user, repo):
        resp = self.oauth.get('https://api.bitbucket.org/2.0/repositories/%s/%s/hooks' % (user, repo))
        data = json.loads(resp.content)
        return data['values']

    def create_hook(self, user : str, repo : str, url, description, events):
        resp = self.oauth.post('https://api.bitbucket.org/2.0/repositories/%s/%s/hooks' % (user, repo), data = json.dumps({
            "url": url,
            "description": description,
            "active": True,
            "events": events
        }))
        return json.loads(resp.content)
