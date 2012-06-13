# -*- coding: utf-8 -*-

class CAD(object):
    code = u'CAD'
    name = u'Canadian dollar'
    exp = 2
    symbol = u'$'


class EUR(object):
    code = u'EUR'
    name = u'Euro'
    exp = 2
    symbol = u'€'


class IQD(object):
    code = u'IQD'
    name = u'Iraqi dinar'
    exp = 3
    symbol = u'ع.د'


class Currency(object):
    DATA = {
        'CAD': CAD,
        'EUR': EUR,
        'IQD': IQD,
    }


def is_valid_currency_code(code):
    return code in Currency.DATA

def currency_symbol(code):
    return Currency.DATA[code].symbol


if __name__ == '__main__':
    assert is_valid_currency_code('CAD')
    assert is_valid_currency_code('EUR')
    assert is_valid_currency_code('IQD')
    assert currency_symbol('CAD') == u'$'
    assert currency_symbol('EUR') == u'€'
    assert currency_symbol('IQD') == u'ع.د'
