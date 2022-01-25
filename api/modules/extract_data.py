import json
from abc import ABC, abstractmethod


class Extractor(ABC):
    def __init__(self, parsed_data):
        self.data = parsed_data["prfsts"]["prfst"]
        self.data_len = len(self.data)

    @abstractmethod
    def _extract(self):
        pass

    def get_new_json(self):
        self._extract()
        pass


class DayExtractor(Extractor):
    def _extract(self):
        self.date = [x["prfdt"] for x in self.data]
        self.open_cnt = [x["prfprocnt"] for x in self.data]
        self.run_cnt = [x["prfdtcnt"] for x in self.data]
        self.sales = [x["amount"] for x in self.data]
        self.tickets = [x["nmrs"] for x in self.data]

    def get_new_json(self):
        self._extract()
        dict_data = {
            "date": self.date,
            "open_count": self.open_cnt,
            "run_count": self.run_cnt,
            "sales": self.sales,
            "tickets": self.tickets,
        }
        return dict_data


class GenreExtractor(Extractor):
    def _extract(self):
        self.genres = [x["cate"] for x in self.data]
        self.tickets = [x["nmrs"] for x in self.data]
        self.sales = [x["amount"] for x in self.data]
        self.sale_shr = [x["amountshr"] for x in self.data]
        self.open_cnt = [x["prfprocnt"] for x in self.data]
        self.run_cnt = [x["prfdtcnt"] for x in self.data]
        self.aud_shr = [x["nmrsshr"] for x in self.data]

    def get_new_json(self):
        self._extract()
        dict_data = {
            "genres": self.genres,
            "tickets": self.tickets,
            "sales": self.sales,
            "sale_share": self.sale_shr,
            "open_count": self.open_cnt,
            "run_count": self.run_cnt,
            "audience_share": self.aud_shr,
        }
        return dict_data
