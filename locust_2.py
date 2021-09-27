import logging

from locust import HttpUser, task, constant,events

@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 100:
        logging.error("Test failed due to average response time ratio > 200 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0

class Reqres(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)

    @task
    def get_user(self):
        res=self.client.get("api/users?page=2")
        print(res.status_code)

    @task
    def create_user(self):
        res=self.client.post("api/users",data='''{"name": "morpheus","job": "leader"x}''')
        print(res.text)
