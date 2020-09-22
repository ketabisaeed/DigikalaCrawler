"""
Author: Saeed Ketabi
Email: saeed.ketabi@gmail.com
Telegram: @Sbooki / @Sboooki
http://Boooki.ir

2020 september 21
"""


class DataCleaner:

    DATA_MODEL = {
        "comment": str,
        "positives": list,
        "negatives": list,
        "opinion": str,
    }

    def __init__(self):
        pass

    def process(self,data: dict):
        self._validate(data)
        return self._clean(data)

    def _clean(self,data):
        """
        *****************************************************
        *****************************************************
                 COMPLETE THIS FUNCTION AS YOU WANT!
        *****************************************************
        *****************************************************
        """
        data['positives'] = " - ".join(data['positives'])
        data['negatives'] = " - ".join(data['negatives'])
        return data

    def _validate(self,data: dict):
        """
        Validate data
        :param data:
        :return:
        """
        for key, value in self.DATA_MODEL.items():
            if key in data:
                if type(data[key]) == value:
                    pass
                else:
                    raise Exception("Data validation error in {},{}!".format(key, value))
            else:
                raise Exception("Data validation error in {},{}!".format(key,value))
        for key,value in data.items():
            if key in self.DATA_MODEL:
                pass
            else:
                raise Exception("Data validation error in {},{}!".format(key,value))


if __name__ == '__main__':
    data = {
        "comment": 'str',
        "positives": [],
        "negatives": [],
        "opinion": 'str',
    }
    cleaner = DataCleaner()
    cleaner.clean(data)
