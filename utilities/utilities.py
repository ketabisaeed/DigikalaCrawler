"""
Author: Saeed Ketabi
Email: saeed.ketabi@gmail.com
Telegram: @Sbooki / @Sboooki
http://Boooki.ir

2020 september 21
"""
from config.config import Config


class Exporters:

    def __init__(self,
                 destination="./output/",
                 file_name="output.csv"):
        """
        Description
        :param destination: Destination to write
        :param file_name: File_name to write output
        """
        self.destination = destination
        self.file_name = file_name

    def publish(self,
                data,
                file_name=None):
        """
        Append a list to a csv file
        :param data: data
        :param file_name: file_name to write output
        :return: None
        """
        TOOLS = {
            'CSV': self.append_to_csv,
            'RABBITMQ': self.publish_to_rabbit,
            'MONGODB': self.publish_to_mongodb,
        }
        method = TOOLS[Config.CRAWLERS['digikala_comments']['output']]
        method(data,file_name)

    def append_to_csv(self,
                      data: list,
                      file_name = None):
        """
        Append a list to a csv file
        :param data: data in list
        :param file_name: file_name to write output
        :return: None
        """
        if not file_name:
            file_name = self.file_name
        if type(data) == dict:
            data = list(data.values())
        print(data)
        try:
            with open(self.destination+file_name+'.csv','a') as f:
                f.write(",".join(data)+"\n")
        except FileExistsError:
            print('(E) Destination not found!')

    def publish_to_rabbit(self):
        pass

    def publish_to_mongodb(self):
        pass


if __name__ == '__main__':
    exporter = Exporters()
    exporter.append_to_csv(['comment','positives','negatives','opinion'])