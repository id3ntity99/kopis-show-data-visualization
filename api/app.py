from flask import Flask, request, abort
from dotenv import load_dotenv
from flask_cors import CORS
from request_api import Converter
from redis_cache import RedisCache
from extract_data import DayExtractor, GenreExtractor
import os
import datetime

# dotenv env variables.
load_dotenv()
API_KEY_NAME = os.environ.get("API_KEY_NAME")
API_KEY_VAL = os.environ.get("API_KEY_VALUE")
FRONT_URL = os.environ.get("FRONT_URL")


# Flask app
app = Flask(__name__)

# CORS
cors = CORS(app, resources={r"/api/*": {"origins": FRONT_URL}})


@app.route("/api/genre", methods=["GET"])
def get_request_genre():
    start_date = request.args.get("stdate")
    end_date = request.args.get("eddate")
    BASE_URL = os.environ.get("API_BASE_URL_GENRE")
    URL = (
        f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&stdate={start_date}&eddate={end_date}"
    )
    REDIS_KEY = f"/api/genre?stdate={start_date}&eddate={end_date}"

    requester = Converter(URL)
    cacher = RedisCache(REDIS_KEY)

    if request.method == "GET":
        if cacher.does_exist():
            print(f"Data exists, key:{REDIS_KEY}")
            return cacher.get_redis()
        else:
            dict_data = requester.get_parsed_data()
            new_json = GenreExtractor(dict_data).get_new_json()
            time_out = datetime.timedelta(minutes=30)
            cacher.set_redis(new_json, time_out)
            return new_json
    else:
        return abort(400)


@app.route("/api/day", methods=["GET"])
def get_request_day():
    start_date = request.args.get("stdate")
    BASE_URL = os.environ.get("API_BASE_URL_MONTH")
    URL = f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&ststype=day&stdate={start_date}"
    REDIS_KEY = f"/api/day?stdate={start_date}"

    requester = Converter(URL)
    cacher = RedisCache(REDIS_KEY)

    if request.method == "GET":
        if cacher.does_exist():
            print(f"Data exists, key:{REDIS_KEY}")
            return cacher.get_redis()
        else:
            dict_data = requester.get_parsed_data()
            new_json = DayExtractor(dict_data).get_new_json()
            time_out = datetime.timedelta(minutes=60)
            cacher.set_redis(new_json, time_out)
            return new_json
    else:
        return abort(400)


if __name__ == "__main__":
    app.run(debug=True)
