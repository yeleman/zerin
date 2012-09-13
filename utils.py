#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

import re


def clean_phone_number(number):
    """ turns 21345678 into 12 34 56 78 """

    def is_int(number):
        if re.match(r'^[+|(]', number):
            return True
        if re.match(r'^\d{1,4}\.\d+$', number):
            return True
        return False

    if not isinstance(number, basestring):
        number = number.__str__()

    # cleanup markup
    clean_number = re.sub(r'[^\d]', '', number)

    # is in international format?
    if is_int(re.sub(r'[\-\s]', '', number)):
        h, indicator, clean_number = \
                            clean_number.partition('')
        return (indicator, clean_number)
    return (None, clean_number)


def phone_number_formatter(number):
    """ turns 21345678 into 12 34 56 78 """

    def format(number):
        if len(number) & 1:
            span = 3
        else:
            span = 2
        return u" ".join([u"".join(number[i:i + span]) \
                          for i in range(0, len(number), span)])

    ind, clean_number = clean_phone_number(number)
    if ind:
        return u"(%(ind)s) %(num)s" \
               % {'ind': ind, 'num': format(clean_number)}
    return format(clean_number)
