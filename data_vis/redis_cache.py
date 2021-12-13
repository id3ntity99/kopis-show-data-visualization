import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT
        )


def get_redis(key):
    result = r.get(key)
    print(f"{result} is written.")
    return dict(json.loads(result))


# setter only accepts dict-type.
# def set_redis(key:str, value:Dict)
def set_redis(key, value, expire):
    to_json = json.dumps(value).encode('utf-8')
    r.set(key, to_json, expire)
    print(f"{key} is(are) written.")


def does_exist(key):
    if r.get(key) is None:
        return False
    else:
        return True
