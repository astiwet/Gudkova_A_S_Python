import requests

from dotenv import load_dotenv
import os
load_dotenv()


class ProjectApi:
    def __init__(self, url) -> None:
        self.url = url

    def create_project(self, name):
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("API_KEY")
        my_headers['Content-type'] = 'application/json'
        project = {
            'title': name
            }
        resp = requests.post(self.url + '/api-v2/projects', json=project,
                             headers=my_headers)
        print("Ответ от сервера:", resp.json())
        return resp, resp.json()

    def edit_project(self, new_name, id):
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("API_KEY")
        my_headers['Content-type'] = 'application/json'
        project = {'title': new_name}
        resp = requests.put(self.url + '/api-v2/projects/' + str(id),
                            json=project, headers=my_headers)
        print("Ответ от сервера:", resp.json())
        return resp, resp.json()

    def get_project(self, id):
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("API_KEY")
        my_headers['Content-type'] = 'application/json'
        resp = requests.get(self.url + '/api-v2/projects/' + str(id),
                            headers=my_headers)
        print("Ответ от сервера:", resp.json())
        return resp, resp.json()
