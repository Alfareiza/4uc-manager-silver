import math
import datetime
from django import template

register = template.Library()


@register.filter
def date_from_minute(m):
    """
    Calc date from minutes and return a string with the date.
    :param minutes: 351702: int
    :return: 'Jan 25 de 2021 15:44'
    """
    if m is not None:
        now = datetime.datetime.utcnow()
        deltadate = now - datetime.timedelta(minutes=m)
        return deltadate.strftime("%d %b %Y %H:%M")
    else:
        return 'Sem Informação'


@register.filter
def minutes_in_time(minutes):
    '''
    Calc the time from minutes and return a string with the calculation.
    Returns empty string on any error.
    Ex.: minutes: 256587
    :param minutes: 351702 :int
    :return: 'há 8 meses' :str
    '''
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
            elif days == 1:
                return f"há {days} Día"
            elif days > 1:
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
def format_str_date(date_time_str):
    """
    Transform str to date
    :param date_str: '2021-06-22 12:16:27'
    :return:
    """
    if date_time_str is not None:
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        date_time_obj.strftime("%d %b %Y %H:%M:%S")
        return date_time_obj
    else:
        return '-'


@register.filter
def number_day_to_name_day(number):
    """
    Receives a number where 0 is sunday and returns the name of the day
    :param number:
    :return:
    """
    weekDay = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado', 7: 'Domingo'}
    return weekDay[number]


@register.filter
def dict_key(dictionary, key):
    """
    Receive and dictinoary and a key
    :param dictionary: 'playlists': {'0': {'id': 3, 'name': 'Novo'}, '1': {'id': 3, 'name': 'Novo'}}
    :param key: '0' :str
    :return: The value of the dict. Ex: {'id': 3, 'name': 'Novo'} :dict
    """
    return dictionary[str(key)]
