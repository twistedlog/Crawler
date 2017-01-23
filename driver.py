from crawl import Crawler
from crawl import FileReader
from crawl import Writer


class Driver():
    """
    Driver function to run the crawler
    """

    def __init__(self, src, output):
        # TODO change the way FileReader and FileWriter classes are being used there should be an abstraction generating these classes and not called directly
        self.reader = FileReader(src)
        self.writer = FileWriter(output)
        self.crawer = Crawler(reader=self.reader, writer=self.writer)

    def run(self):
        self.crawler.run()


if __name__ == "__main__":
    driver = Driver("", "")
    driver.run()
