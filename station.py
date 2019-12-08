# coding:utf-8
import requests
import re
import json


def get_stations():
    url = 'https://www.12306.cn/index/script/core/common/station_name_v10026.js'
    r = requests.get(url)
    pattern = '([\u4e00-\u9fa5]+)\|([A-Z]+)'
    results = re.findall(pattern, r.text)
    # print(results)
    stationName = dict(results)
    # print(stationName)
    with open('./station.json', 'w') as f:
        json.dump(stationName, f, ensure_ascii=False)
    return stationName



def get_query_url(station_dict, from_station, to_station, date):

    date = date
    from_station = from_station + ',' + station_dict[from_station]
    to_station = to_station + ',' + station_dict[to_station]
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}'
           '&leftTicketDTO.from_station={}'
           '&leftTicketDTO.to_station={}'
           '&purpose_codes=ADULT'
           ).format(date, from_station, to_station)
    print(url)
    return url

def get_trains(url):
	r = requests.get(url)
	all_trains = r.json
if __name__ == '__main__':
    get_query_url(get_stations(), '天津', '上海', '2019-12-11')
