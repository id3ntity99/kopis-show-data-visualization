import redis
import json

r = redis.Redis(
        host="localhost",
        port=6379
        )


def get_redis(key):
    result = r.get(key)
    print(f"{result} is written.")
    return dict(json.loads(result))


# setter only accepts dict-type.
# def set_redis(key:str, value:Dict)
def set_redis(key, value):
    to_json = json.dumps(value).encode('utf-8')
    r.set(key, to_json)
    print(f"{key} is(are) written.")


def does_exist(key):
    if r.get(key) is None:
        return False
    else:
        return True
