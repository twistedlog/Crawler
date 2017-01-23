import urllib2

class Crawler(object):
    """
    Crawler class goes and actually gets the url
    """
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def run(self):
        while True:
            url = self.reader.get_url()
            page = self.fetch_page(url)
            if page.is_jquery():
                self.writer.write(url)

    def fetch_page(self, url):
        try:
            resp = urllib2.open(url.url)
        except Exception as e:
            print e
            raise e
        else:
            return Page(url=url, body=resp.body)


class Page(object):
    """
    Page class where details of request body are kept
    url is URL class instance
    body is actual content of that page
    """
    
    def __init__(self, url, body):
        self.url = url
        self.body = body
        self.is_jquery = self._check_for_jquery()

    def _check_for_jquery(self):
        return False

    @property
    def is_jquery(self):
        return False


class URL(object):
    """
    URL class represents a url object
    """
    
    def __init__(self, url):
        self.url = url

    @property
    def url(self):
        return self.url

    def __repr__(self):
        return 'URL : %s' % self.url

class Reader(object):
    """
    Reader is an abstract class reads from a src
    """

    def get_url(self):
        raise NotImplementedError


class FileReader(Reader):
    """
    Filereader class reads from file
    """
    def __init__(self, src):
        self.src = src
        self.fd = self._get_file_handle()

    def _get_file_handle(self):
        try:
            fd = open(self.src, 'r+')
        except Exception as e:
            raise e
        else:
            return fd

    def get_url(self):
        try:
            yield URL(url=fd.readLine())
        except Exception as e:
            print e
            fd.close() # potential memory leak rewrite this

class Writer(object):
    """
    Writer is an abstract class to output results to a src
    """

    def write(self, data):
        raise NotImplementedError

class FileWriter(Writer):
    """
    Filewriter class writes to a file
    """
    
    def __init__(self, src):
        pass

    def write(self, data):
        pass
