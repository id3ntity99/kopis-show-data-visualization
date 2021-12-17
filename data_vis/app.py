from flask import Flask, request, abort
from dotenv import load_dotenv
from create_chart import create_double_line, create_double_bars
from public import get_parsed_data
from redis_cache import does_exist, get_redis, set_redis
from extract_data import extract_day_data, extract_genre_data
from flask_cors import CORS
import os
import datetime
import json


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

    # Check if data exists on Redis.
    REDIS_KEY = f"/api/genre?stdate={start_date}&eddate={end_date}"
    if request.method == "GET":

        if does_exist(REDIS_KEY):
            dict_data = get_redis(REDIS_KEY)
            print(f"Data exists, key:{REDIS_KEY}")
        else:
            dict_data = get_parsed_data(URL)
            time_out = datetime.timedelta(minutes=30)
            set_redis(REDIS_KEY, dict_data, time_out)
    else:
        return abort(400)

    """
    (
        genres,
        tickets,
        sales,
        sale_shr,
        open_cnt,
        run_cnt,
        aud_shr,
    ) = extract_genre_data(dict_data)
    """


@app.route("/api/day", methods=["GET"])
def get_request_day():
    start_date = request.args.get("stdate")
    BASE_URL = os.environ.get("API_BASE_URL_MONTH")
    URL = f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&ststype=day&stdate={start_date}"
    REDIS_KEY = f"/api/day?stdate={start_date}"
    if request.method == "GET":
        if does_exist(REDIS_KEY):
            dict_data = get_redis(REDIS_KEY)
            print(f"Data exists, key:{REDIS_KEY}")
            return dict_data
        else:
            dict_data = get_parsed_data(URL)
            time_out = datetime.timedelta(minutes=60)
            set_redis(REDIS_KEY, dict_data, time_out)
            return dict_data
    else:
        return abort(400)

    # (date, open_cnt, run_cnt, sales, tickets) = extract_day_data(dict_data)


if __name__ == "__main__":
    app.run(debug=True)
