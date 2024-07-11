import os
import random
from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class NextcloudUser(HttpUser):
    auth = None
    user_name = None
    wait_time = between(2, 5)

    def on_start(self):
        user_idx = random.randrange(1, 31)  # Assuming user indices are from 1 to 30
        self.user_name = f'user{user_idx}'  # Assuming user names are like 'user1', 'user2', etc.
        self.auth = HTTPBasicAuth(self.user_name, f'Test1234_{user_idx}')  # Password pattern as per your credentials

    @task
    def propfind(self):
        response = self.client.request("PROPFIND", f"/remote.php/dav/files/{self.user_name}/", auth=self.auth)
        print(f"PROPFIND response for {self.user_name}: {response.status_code}")

    @task
    def upload_big(self):
        filename = "testfile_5mb"
        file_path = '/mnt/locust/' + filename  # Assuming test files are in this path

        with open(file_path, 'rb') as f:
            response = self.client.put(f"/remote.php/dav/files/{self.user_name}/{filename}",
                                       auth=self.auth, data=f, name=f"/remote.php/dav/files/{self.user_name}/testfile_5mb")
            print(f"Upload response for {self.user_name}: {response.status_code}")

        if response.status_code not in [201, 204]:
            with open("output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user_name}.\n")
            return

        for i in range(0, 5):
            response = self.client.get(f"/remote.php/dav/files/{self.user_name}/{filename}",
                                       auth=self.auth, name=f"/remote.php/dav/files/{self.user_name}/testfile_5mb")
            print(f"Download response for {self.user_name}: {response.status_code}")

        response = self.client.delete(f"/remote.php/dav/files/{self.user_name}/{filename}",
                                      auth=self.auth, name=f"/remote.php/dav/files/{self.user_name}/testfile_5mb")
        print(f"Delete response for {self.user_name}: {response.status_code}")

