import os

from client import Client

if __name__ == '__main__':
    username = "user1"
    password = "pass1"

    # SaltySugar REST_API_server
    # https://github.com/SaltySugar32/REST_API_server
    url = "http://52.168.122.249:5000"

    status = True
    client = Client(url, username, password)

    while status:
        print('>_', end=' ')
        cmd = input().strip().split()
        try:
            if cmd[0] == "get":
                client.get_todo()

            elif cmd[0] == "post":
                assert len(cmd) >= 2
                description = " ".join(cmd[1:])
                client.post_todo(description)

            elif cmd[0] == "put":
                assert len(cmd) >= 3
                description = " ".join(cmd[2:])
                client.put_todo(cmd[1], description)

            elif cmd[0] == "delete":
                assert len(cmd) >= 2
                client.delete_todo(cmd[1])

            else:
                status = False

        except:
            print("Ошибка ввода")
