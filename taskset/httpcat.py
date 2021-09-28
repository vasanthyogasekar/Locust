from locust import TaskSet, constant, task, HttpUser, SequentialTaskSet


class Httpcat200(SequentialTaskSet ):
    @task
    def get_status_200(self):
        self.client.get("/200")
        self.interrupt()


class Httpcat100300(SequentialTaskSet  ):
    @task
    def get_status_100(self):
        self.client.get("/100")
        self.interrupt()

    @task
    def get_status_100(self):
        self.client.get("/300")
        self.interrupt()

    @task
    def get_status_100(self):
        self.client.get("/400")
        self.interrupt()





class Loadtest(HttpUser):
    host = "http://http.cat"
    wait_time = constant(1)
    tasks = [Httpcat200,Httpcat100300]



