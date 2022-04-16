import os
from datetime import datetime, timedelta, time

def send_ping(ip:str, interval:int, count:int) -> str:
    '''

    :param ip:
    :param tempo:
    :param contagem:
    :return: name of saved file
    '''
    pings = os.system('ping -i {} -c {} -n {} > ping_{}.txt'.format(interval,
                                                                    count,
                                                                    ip,
                                                                    datetime.now().strftime('%d-%m-%Y_%H:%M')))

    return('ping_{}.txt'.format(ip, datetime.now().strftime('%d-%m-%Y %H:%M')))
