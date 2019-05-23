#!/usr/bin/env python3

import sys
from hashlib import md5

salt = b'jirlaogbfj'

# input
text = []
for l in sys.stdin:
    text.append(l.replace('\n','').encode('utf-8'))
num = len(text)
for i in range(num):
    salt_text = text[i] + salt
    hash_text = md5(salt_text).hexdigest()
    print(hash_text)
