import json
import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as Bs


class Parsing(ABC):
    html = None

    def __init__(self, url):
        self.url = url

    def get_html(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            self.html = Bs(response.text, features='lxml')
        else:
            raise RuntimeError(f'status code: {response.status_code}; {response.text}')

    @abstractmethod
    def parsing(self):
        ...

    def save(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.parsing(), file, indent=4, ensure_ascii=False)
