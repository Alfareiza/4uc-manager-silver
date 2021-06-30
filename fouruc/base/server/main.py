import json
import time
import requests
from decouple import config


class Client:
    def __init__(self, token, name=None, account=None, type=None):
        self.name = name
        self.token = token
        self.account = account
        self.type = type
        self.users = None
        self.user_groups = None
        self.uploads = None
        self.medias = None
        self.media_category = None
        self.players = None
        self.playlists = None
        self.templates = None
        self.news = None
        self.newsources = None
        self.videowall = None
        self.reports = None

    def get_all(self, resource, payload={}):
        allResources = list()
        count = 0
        i, limit = 1, 1
        while i <= limit:
            url = f'https://api.4yousee.com.br/v1/{resource}?page={i}'
            headers = {
                'Secret-Token': self.token,
                'Content-Type': 'application/json'
            }
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, params=payload)
            data = json.loads(response.text)
            print('coletando...{}'.format(resource))
            # data = json.dumps(data, indent=2)
            if data.get('totalPages', False):
                limit = data['totalPages']
                for item in data['results']:
                    allResources.append(item)
                    count += 1
                    # print(count, medias)
                i += 1
            else:
                break
        return allResources

    def get_users(self):
        self.users = self.get_all('users')

    def get_user_groups(self):
        self.user_groups = self.get_all('users/groups')

    def get_uploads(self):
        self.uploads = self.get_all('uploads')

    def get_medias(self):
        self.medias = self.get_all('medias')

    def get_media_category(self):
        self.media_category = self.get_all('medias/categories')

    def get_players(self):
        self.players = self.get_all('players')

    def get_playlists(self):
        self.playlists = self.get_all('playlists')

    def get_templates(self):
        self.templates = self.get_all('templates')

    def get_news(self):
        self.news = self.get_all('news')

    def get_newsources(self):
        self.newsources = self.get_all('newsources')

    def get_videowall(self):
        self.videowall = self.get_all('videowall')

    def get_reports(self):
        self.reports = self.get_all('reports')


if __name__ == '__main__':
    account = Client(config('TOKEN_4UC'))
    account.get_players()
    print(account.players)
