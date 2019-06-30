# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# License: BSD (see file COPYING for details)
from __future__ import unicode_literals




def populate(pg):

    pg.set_args('fr nl de en')
    pg.province("Limbourg", "Limburg", "Limburg", "Limbourg")
    pg.set_args('zip_code fr nl de en')
    
    pg.village("3800", "Aalst-bij-Sint-Truiden", "", "", "")
