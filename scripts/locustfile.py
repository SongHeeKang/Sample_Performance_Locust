from locust import HttpUser, task, between
import requests
import json


class MyUser(HttpUser):

    wait_time = between(1, 1)
    # def on_start(self):
    def on_start(self):
        # Read the image file and store it as an attribute of the User class
        with open("./images/sample.jpg", "rb") as file:
            self.image_data = file.read()
    @task
    def api_request(self):
        url = "/api-01"

        files = {
            "image": ("sample.jpg", self.image_data, "image/jpeg")
            # "param_a": ("", "4"),
            # "param_b": ("", "jpg"),
        }

        response = self.client.post(url, files=files)
        assert response.status_code == 200
        # res = json.loads(response.text)
        # print(res["result"])
        # assert res["result"] == 0.9399832
