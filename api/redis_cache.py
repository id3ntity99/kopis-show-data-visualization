import redis
import json
import os
from dotenv import load_dotenv


class RedisCache:
    def __init__(self, key):
        load_dotenv()
        REDIS_HOST = os.environ.get("REDIS_HOST")
        REDIS_PORT = os.environ.get("REDIS_PORT")
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        self.key = key

    def get_redis(self):
        result = self.r.get(self.key)
        return dict(json.loads(result))

    def set_redis(self, value, expr):
        to_json = json.dumps(value)
        self.r.set(self.key, to_json, expr)
        print(f"{self.key} is saved completely")

    def does_exist(self):
        if self.r.get(self.key) is None:
            return False
        else:
            return True
