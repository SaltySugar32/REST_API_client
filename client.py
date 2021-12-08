import json

import requests


class Client:

    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.body = {
            "username": username,
            "password": password
        }
        self.user_url = "/user/"
        self.todo_url = "/todo/"

        response = requests.post(self.url + self.user_url, data=self.body)
        token = "Bearer " + response.json()['access_token']
        self.headers = {"Authorization": token}

    def get_todo(self):
        response = requests.get(self.url + self.todo_url, headers=self.headers)
        print(json.dumps(response.json(), indent = 1))

    def post_todo(self, description: str):
        response = requests.post(self.url + self.todo_url, data={'description': description}, headers=self.headers)
        print(response.json())

    def put_todo(self, task_id: int, description: str):
        response = requests.put(self.url+self.todo_url+str(task_id), data={'description': description}, headers=self.headers)
        print(response.json())

    def delete_todo(self, task_id: int):
        response = requests.delete(self.url+self.todo_url+str(task_id), headers=self.headers)
        print(response.json())