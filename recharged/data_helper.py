#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from datetime import datetime


def date_datetime(dat):
    "reçoit une date return une datetime"
    dat = str(dat)
    day, month, year = dat.split('/')
    dt = datetime.now()
    return datetime(int(year), int(month), int(day),
                    int(dt.hour), int(dt.minute),
                    int(dt.second), int(dt.microsecond))


def format_date(dat):
    dat = str(dat)
    day, month, year = dat.split('/')
    return '-'.join([year, month, day])


def show_date(dat):
    return dat.strftime(u"%A le %d %b %Y a %Hh:%Mmn")
