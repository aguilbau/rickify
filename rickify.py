#!/usr/bin/env python

from __future__ import print_function
import sys
import random
import os


def sip_some_wodka(a):
    r = random.random()
    if r < 0.:
        return a
    alcools = [
        'whisky',
        'wodka',
    ]
    a.insert(random.randint(1, len(a)), '*takes a sip of %s*' % alcools[random.randint(0, len(alcools) - 1)])
    return a

def add_a_burp(a):
    res = []
    for word in a[1:]:
        r = random.random()
        if r < 0.1:
            res.append('*burp*')
        res.append(word)
    res.insert(0, a[0])
    return res

def double_first_letter(a):
    res = []
    for word in a[1:]:
        r = random.random()
        if r < 0.2:
            word = '%s-%s' % (word[0], word)
        res.append(word)
    res.insert(0, '%s-%s' % (a[0][0], a[0]))
    return res

def rickify(s):
    funcs = [
        double_first_letter,
        add_a_burp,
        sip_some_wodka,
    ]
    a = list(filter(None, s.split(' ')))
    for f in funcs:
        a = f(a)
    return ' '.join(a)

def main():
    if len(sys.argv) != 2:
        print('usage: %s <funny sentence>' % sys.argv[0], file=sys.stderr)
        exit(1)
    random.seed(os.urandom(10))
    print(rickify(sys.argv[1]))

if __name__ == '__main__':
    main()
