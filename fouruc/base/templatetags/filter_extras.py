import math

from django import template

register = template.Library()


@register.filter
def minutes_in_time(minutes):
    '''
    Calc the time from minutes and return a string with the calculation.
    Returns empty string on any error.
    Ex.: minutes: 256587
    :param minutes: 351702 :int
    :return: 'há 8 meses' :str
    '''
    # minutes = eval(minutes)
    try:
        if minutes is not None:
            hours = minutes // 60
            days = hours / 24
            days = math.ceil(days)
            months = days // 30
            year = months // 12
            if year > 0:
                return f"há {year} Anos"
            elif months > 0:
                return f"há {months} Meses"
            elif days > 0:
                return f"há {days} Días"
            elif hours > 0:
                return f"há {hours} Horas"
            elif minutes > 0:
                return f"há {minutes} Minutos"
        else:
            return 'Sem Informação'
    except Exception as e:
        print('Error > ', e)
    return ''


@register.filter
def dict_key(dictionary, key):
    """
    Receive and dictinoary and a key
    :param dictionary: 'playlists': {'0': {'id': 3, 'name': 'Novo'}, '1': {'id': 3, 'name': 'Novo'}}
    :param key: '0' :str
    :return: The value of the dict. Ex: {'id': 3, 'name': 'Novo'} :dict
    """
    return dictionary[str(key)]
