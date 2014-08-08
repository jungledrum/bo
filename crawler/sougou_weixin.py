# encoding=utf-8
import subprocess
from pymongo import MongoClient


db = MongoClient().bo

url = 'http://weixin.sogou.com/gzh?openid=oIWsFt86NKeSGd_BQKp1GcDkYpv0';
result = subprocess.Popen(['casperjs','sougou_weixin.js', url], stdout=subprocess.PIPE)
lines = result.stdout.read()


lines = lines.split('\n')
for line in lines:
    print line
    db.weixin_urls.insert({'url': line})