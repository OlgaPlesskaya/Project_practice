from locust import HttpUser, task, between
class UserBehavior(HttpUser):
    wait_time = between(5, 15)
    @task
    def login(self):
        self.client.post("/login/", {"username": "test_user", "password": "test_password"})
    @task
    def index_page(self):
        self.client.get("/")