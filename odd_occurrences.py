# -*- coding: utf-8 -*-

def oddoccurrence(A):
    dict_value = dict((number, A.count(number)) for number in set(A))
    temp = 0
    for key, value in dict_value.iteritems():
        if value % 2 != 0:
            temp = key
    return temp

oddoccurrence([9, 3, 9, 3, 9, 7, 9])