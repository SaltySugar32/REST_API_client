import json
import os

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
        self.files_url = "/files/"

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

    """
    --------------------------------------------------------------------------------------------------------------------
    -------------------------------------------------- File Storage ----------------------------------------------------
    --------------------------------------------------------------------------------------------------------------------
    """

    def post_files(self, file_path:str):
        with open(file_path, "rb") as file:
            response = requests.post(self.url + self.files_url, files={'file': file}, headers=self.headers)
            print(response.json())

    def get_files(self):
        response = requests.get(self.url + self.files_url, headers=self.headers)
        print(json.dumps(response.json(), indent=1))

    def delete_file(self, filename: str):
        response = requests.delete(self.url + self.files_url + filename, headers=self.headers)
        print(response.json())

    def download_file(self, filename: str):
        response = requests.get(self.url + self.files_url + filename, headers=self.headers, stream=True)
        if response.status_code != 200:
            print(response.json())

        else:
            files_path = "./files/"
            if not os.path.exists(files_path):
                os.mkdir(files_path)

            path = files_path + self.body["username"]+"/"
            if not os.path.exists(path):
                os.mkdir(path)

            f = open(path + str(filename), 'wb')
            f.write(response.content)
            f.close()


