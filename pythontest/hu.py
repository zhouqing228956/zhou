# -*- coding: utf-8 -*-
import json
def zhou():
    L = [('ni', 'j', '周'), (3, 4, 5), (3, 1, 1)]
    for s in L:
        yield {
            'd': s[0],
            'k': s[1],
            'p': s[2]
        }
def qing():
    k=zhou()
    for h in k:
        print(h)
        write(h)
def write(content):
    with open('zhou.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False)+ '\n')
        f.close()
qing()