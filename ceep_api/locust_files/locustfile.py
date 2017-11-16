from locust import HttpLocust, TaskSet, task

# How to run Locust: (Web URL: http://127.0.0.1:8089)
# locust -f locust_files/locustfile.py --host=http://127.0.0.1:8888
# locust -f locust_files/locustfile.py --slave --master-host=127.0.0.1 --host=http://127.0.0.1:8888

class UserBehavior(TaskSet):
    def on_start(self):
        print('Locust on start...')

    @task(2)
    def index(self):
        self.client.get("/api/1.0")

    @task(1)
    def profile(self):
        self.client.get("/api/1.0/adbMonitors")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
