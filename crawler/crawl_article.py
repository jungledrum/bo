# encoding=utf-8
from datetime import datetime
import requests
from pymongo import MongoClient
from readability.readability import Document


db = MongoClient().bo

def crawl_url(url):
    html = requests.get(url)
    doc = Document(html.content)
    content = doc.summary().encode('utf-8')
    title = doc.title().encode('utf-8')
    return {
        'content': content,
        'title': title
    }


def main():
    urls = db.weixin_urls.find()
    t1 = datetime.now()

    for item in urls:
        url = item['url']
        try:
            html = crawl_url(url)
        except Exception, e:
            continue

        # filename = 'articles/%s.txt' % html['title']
        # with open(filename, 'ab') as f:
        #     f.write(html['content'])
        print html['title']
        u = db.weixin_urls.find_one({'_id': item['_id']})
        u['content'] = html['content']
        u['title'] = html['title']
        db.weixin_urls.save(u)

    t2 = datetime.now()
    print t2-t1

if __name__ == '__main__':
    main()