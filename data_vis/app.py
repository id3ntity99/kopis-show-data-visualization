from flask import Flask, request, abort
from dotenv import load_dotenv
from create_chart import create_double_line, create_double_bars
from public import get_parsed_data
from redis_cache import does_exist, get_redis, set_redis
import os
import json
import datetime


# dotenv env variables.
load_dotenv()
API_KEY_NAME = os.environ.get("API_KEY_NAME")
API_KEY_VAL = os.environ.get("API_KEY_VALUE")


def extract_day_data(data):
    data = data["prfsts"]["prfst"]
    data_length = len(data)
    date = [data[i]["prfdt"] for i in range(data_length)]
    open_cnt = [data[i]["prfprocnt"] for i in range(data_length)]
    run_cnt = [data[i]["prfdtcnt"] for i in range(data_length)]
    sales = [data[i]["amount"] for i in range(data_length)]
    tickets = [data[i]["nmrs"] for i in range(data_length)]

    return date, open_cnt, run_cnt, sales, tickets


def extract_genre_data(data):
    data = data["prfsts"]["prfst"]
    data_length = len(data)
    genres = [data[i]["cate"] for i in range(data_length)]
    tickets = [data[i]["nmrs"] for i in range(data_length)]
    sales = [data[i]["amount"] for i in range(data_length)]
    sale_shr = [data[i]["amountshr"] for i in range(data_length)]
    open_cnt = [data[i]["prfprocnt"] for i in range(data_length)]
    run_cnt = [data[i]["prfdtcnt"] for i in range(data_length)]
    aud_shr = [data[i]["nmrsshr"] for i in range(data_length)]

    return genres, tickets, sales, sale_shr, open_cnt, run_cnt, aud_shr


# Flask app
app = Flask(__name__)


@app.route("/api/genre", methods=["GET"])
def get_request_genre():
    start_date = request.args.get("stdate")
    end_date = request.args.get("eddate")
    fltr = request.args.get("filter")
    BASE_URL = os.environ.get("API_BASE_URL_GENRE")
    URL = (
        f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&stdate={start_date}&eddate={end_date}"
    )
    REDIS_KEY = f"/api/genre?filter={fltr}&stdate={start_date}&eddate={end_date}"

    # Check if data exists on Redis.
    if does_exist(REDIS_KEY):
        dict_data = get_redis(REDIS_KEY)
        print("data exists")
    else:
        dict_data = get_parsed_data(URL)
        set_redis(REDIS_KEY, dict_data, datetime.timedelta(minutes=30))

    (
        genres,
        tickets,
        sales,
        sale_shr,
        open_cnt,
        run_cnt,
        aud_shr,
    ) = extract_genre_data(dict_data)

    if request.method == "GET" and fltr == "share":
        # Return charts related to "share"
        return create_double_bars(
            "Genres", "Solds", genres, sale_share=sale_shr, audience_share=aud_shr
        )
    elif request.method == "GET" and fltr == "sales":
        return create_double_bars(
            "Genres", "Solds", genres, tickets=tickets, sales=sales
        )
    elif request.method == "GET" and fltr == "count":
        return create_double_bars(
            "Genres", "Counts", genres, run_count=run_cnt, audience_count=aud_shr
        )
    else:
        return abort(400)


@app.route("/api/day", methods=["GET"])
def get_request_day():
    start_date = request.args.get("stdate")
    fltr = request.args.get("filter")
    BASE_URL = os.environ.get("API_BASE_URL_MONTH")
    URL = f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&ststype=day&stdate={start_date}"

    # get_parsed_data will return dictionary
    dict_data = get_parsed_data(URL)

    (date, open_cnt, run_cnt, sales, tickets) = extract_day_data(dict_data)

    if request.method == "GET" and fltr == "sales":
        return create_double_line("Date", "Amount", date, sales=sales, tickets=tickets)
    elif request.method == "GET" and fltr == "count":
        return create_double_line(
            "Date", "Shares", date, open_count=open_cnt, run_count=run_cnt
        )
    else:
        return abort(400)


if __name__ == "__main__":
    app.debug = False
    app.run()
