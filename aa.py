import requests
import re
import json


def get_stations():
    url = 'https://www.12306.cn/index/script/core/common/station_name_v10026.js'
    r = requests.get(url)
    pattern = '([\u4e00-\u9fa5]+)\|([A-Z]+)'
    results = re.findall(pattern, r.text)
    stationName = dict(results)
    print(stationName)
    with open('./station.json', 'w') as f:
        json.dump(stationName, f)
    return stationName


if __name__ == "__main__":
    get_stations()
