from dotenv import load_dotenv
from modules.request_api import Converter
from modules.extract_data import GenreExtractor
from modules.extract_data import DayExtractor
from utils.logger.logger import Logger
from redis_cache.redis_cache import RedisCache
from flask import Blueprint
from flask import request
from flask import abort
import os
import datetime

blueprint = Blueprint("api", __name__, url_prefix="/api")
load_dotenv(verbose=True)
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY_VAL = os.getenv("API_KEY_VALUE")
logger = Logger()


@blueprint.route("/genre", methods=["GET"])
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
            logger.set_new_format("%(asctime)s | %(name)s | %(levelname)s | EXSIST | %(message)s")
            logger.log_caching("Cache exists")
            return cacher.get_redis()
        else:
            dict_data = requester.get_parsed_data()
            new_json = GenreExtractor(dict_data).get_new_json()
            time_out = datetime.timedelta(minutes=30)
            cacher.set_redis(new_json, time_out)
            logger.log_caching("Saved in cache")
            return new_json
    else:
        return abort(400)


@blueprint.route("/day", methods=["GET"])
def get_request_day():
    start_date = request.args.get("stdate")
    BASE_URL = os.environ.get("API_BASE_URL_MONTH")
    URL = f"{BASE_URL}?{API_KEY_NAME}={API_KEY_VAL}&ststype=day&stdate={start_date}"
    REDIS_KEY = f"/api/day?stdate={start_date}"

    requester = Converter(URL)
    cacher = RedisCache(REDIS_KEY)

    if request.method == "GET":
        if cacher.does_exist():
            logger.set_new_format("%(asctime)s | %(name)s | %(levelname)s | EXSIST | %(message)s")
            logger.log_caching("Cache exists")
            return cacher.get_redis()
        else:
            dict_data = requester.get_parsed_data()
            new_json = DayExtractor(dict_data).get_new_json()
            time_out = datetime.timedelta(minutes=60)
            cacher.set_redis(new_json, time_out)
            logger.log_caching("Saved in cache")
            return new_json
    else:
        return abort(400)
