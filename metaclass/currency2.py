# -*- coding: utf-8 -*-

class CurrencyMeta(type):
    def __init__(cls, name, bases, attrs):
        super(CurrencyMeta, cls).__init__(name, bases, attrs)
        if not hasattr(cls, 'DATA'):
            cls.DATA = {}
        else:
            if 'code' not in attrs:
                raise TypeError('%s currency does not define a code' % name)
            cls.DATA[attrs['code']] = cls


class BaseCurrency(object):
    __metaclass__ = CurrencyMeta


class CAD(BaseCurrency):
    code = u'CAD'
    name = u'Canadian dollar'
    exp = 2
    symbol = u'$'


class EUR(BaseCurrency):
    code = u'EUR'
    name = u'Euro'
    exp = 2
    symbol = u'€'


class IQD(BaseCurrency):
    code = u'IQD'
    name = u'Iraqi dinar'
    exp = 3
    symbol = u'ع.د'


#class BTC(BaseCurrency):
#    name = 'Bitcoins'
#    exp = 2
#    symbol = u'☺'


def is_valid_currency_code(code):
    return code in BaseCurrency.DATA

def currency_symbol(code):
    return BaseCurrency.DATA[code].symbol


if __name__ == '__main__':
    assert is_valid_currency_code('CAD')
    assert is_valid_currency_code('EUR')
    assert is_valid_currency_code('IQD')
    assert currency_symbol('CAD') == u'$'
    assert currency_symbol('EUR') == u'€'
    assert currency_symbol('IQD') == u'ع.د'
