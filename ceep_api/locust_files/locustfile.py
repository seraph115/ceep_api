from locust import HttpLocust, TaskSet, task

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
    max_wait = 5000

# locust -f test/locust_test.py --host=http://127.0.0.1:8888
# locust -f test/locust_test.py --slave --master-host=127.0.0.1 --host=http://127.0.0.1:8888
