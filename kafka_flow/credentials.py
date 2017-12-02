import json

class CredentialsManager:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        self.access_token = data['access_token']
        self.access_token_secret = data['access_token_secret']
        self.consumer_key = data['consumer_key']
        self.consumer_secret = data['consumer_secret']

    def parse(self):
        return self.access_token, self.access_token_secret, \
                    self.consumer_key, self.consumer_secret
