# encoding=utf-8

# Приведено два варианта решения
def get_season(month_num):
    u"""Возвращение сезона по номеру месяца.

    Args:
            month_num: номер месяца

    """
    if all([isinstance(month_num, int), month_num >= 1, month_num <= 12]):
        if any([month_num == 12, month_num <= 2]):
            return u'зима'
        elif month_num <= 5:
            return u'весна'
        elif month_num <= 8:
            return u'лето'
        else:
            return u'осень'
    else:
        raise Exception('month_num should be int. The value of x was: {}'.format(month_num))


def get_season_2(month_num):
    u"""Возвращение сезона по номеру месяца.

    Args:
            month_num: номер месяца

    """
    if all([isinstance(month_num, int), month_num >= 1, month_num <= 12]):
        season = month_num // 3
        if any([season == 4, month_num == 0]):
            return u'зима'
        elif season == 1:
            return u'весна'
        elif season == 2:
            return u'лето'
        else:
            return u'осень'
    else:
        raise Exception('month_num should be int. The value of x was: {}'.format(month_num))
