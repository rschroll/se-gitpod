import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Queue:

    def __init__(self, todo):
        self.todo = set(todo)
        self.done = set()

    def add(self, item):
        if item not in self.todo and item not in self.done:
            self.todo.add(item)
    
    def pop(self):
        item = self.todo.pop()
        self.done.add(item)
        return item

    def __bool__(self):
        return bool(self.todo)

todo = Queue(['http://www.clevelandmemory.org/ebooks/tinkerbelle/contents.html'])

def process(url):
    print(f'Processing {url}')
    fn = url.split('/')[-1]
    resp = requests.get(url)
    if not 'html' in resp.headers.get('Content-Type', ''):
        with open(fn, 'wb') as f:
            f.write(resp.content)
    else:
        with open(fn, 'w') as f:
            f.write(resp.text)
        doc = BeautifulSoup(resp.text)
        for img in doc.select('img[src]'):
            todo.add(urljoin(url, img['src']))
        for link in doc.select('a[href]'):
            todo.add(urljoin(url, link['href']))

while todo:
    process(todo.pop())