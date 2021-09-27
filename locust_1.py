from locust import User, task


class FirstTest(User):

    @task
    def launch(self):
        print("launching")

    @task
    def search(self):
        print("Searchinh")
