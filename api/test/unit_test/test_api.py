import unittest
import os
import sys
import time

currentdir = os.path.dirname(__file__)
srcdir = "../../"
fullpath = os.path.abspath(os.path.join(currentdir, srcdir))
sys.path.insert(0, fullpath)

from app import create_app
from utils.logger.logger import Logger


class TestApi(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.tester = app.test_client()
        self.logger = Logger()

    def test_get_genre(self):
        start_test = time.time()
        response = self.tester.get("/api/genre?stdate=20211101&eddate=20211130")
        self.assertEqual(
            200,
            response.status_code,
        )
        msg = "Runtime: {}".format(time.time() - start_test)
        print(msg)


if __name__ == "__main__":
    unittest.main()
