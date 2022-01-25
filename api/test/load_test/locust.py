from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 5.0)

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def get_genre(self):
        self.client.get(
            "http://localhost:5000/api/genre?stdate=20211101&eddate=20211130"
        )
