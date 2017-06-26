#!/usr/bin/env python3
# coding:utf-8

import requests
res = requests.get("https://search.jd.com/Search?keyword=%E8%B7%9F%E8%80%81%E9%BD%90%E5%AD%A6Python&enc=utf-8&suggest=1.def.0.T07&wq=genlaoqipython&pvid=995fab2000564d719669a02a91ede77b")
print(res.text)
