'''Palindrome dates'''

from datetime import datetime
from itertools import chain


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def palinDay(y):
    '''A possibly empty list containing the palindromic
       date for the given year, if such a date exists.
    '''
    s = str(y).rjust(4, '0')
    r = s[::-1]
    iso = ''.join([s, r[0:2], r[2:]])
    try:
        datetime.strptime(iso, '%Y%m%d')
        return [iso]
    except ValueError:
        return []


def palinDay2(y):
    ''' include something like 00010101'''
    res = []
    for month in range(1, 13):
        for day in range(1, 31 + (month % 2 == (month < 8)) - 2 * (month == 2)):
            t = "%02d%02d" % (month, day)
            for i in range(1, 5):
                part = t[::-1][:i]
                date = part + t
                if date == date[::-1]:
                    iso = date.rjust(8, '0')
                    try:
                        x = datetime.strptime(iso, '%Y%m%d')
                        if x < datetime(y, 1, 1, 0, 0):
                            res.append(iso)
                    except:
                        pass
    return res


if __name__ == "__main__":
    palinDates = list(chain.from_iterable(
        map(palinDay, range(0, 2022))
    ))
    print(len(palinDates))
    print(list(chunks(palinDates, 5)))

    res = palinDay2(2022)
    res = sorted(res)
    print(len(res))
    print(list(chunks(res, 5)))
