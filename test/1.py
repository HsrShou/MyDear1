import json
import random
from time import localtime
from requests import get, post
from datetime import datetime, date
from zhdate import ZhDate
import sys
import os



def get_weather(region):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    key = config["weather_key"]
    region_url = "https://geoapi.qweather.com/v2/city/lookup?location={}&key={}".format(region, key)
    response = get(region_url, headers=headers).json()
    if response["code"] == "404":
        print("推送消息失败，请检查地区名是否有误！")
        os.system("pause")
        sys.exit(1)
    elif response["code"] == "401":
        print("推送消息失败，请检查和风天气key是否正确！")
        os.system("pause")
        sys.exit(1)
    else:
        # 获取地区的location--id
        location_id = response["location"][0]["id"]
    weather_url = "https://devapi.qweather.com/v7/weather/now?location={}&key={}".format(location_id, key)
    response = get(weather_url, headers=headers).json()
    # 天气
    weather = response["now"]["text"]
    # 当前温度
    temp = response["now"]["temp"] + u"\N{DEGREE SIGN}" + "C"
    # 风向
    wind_dir = response["now"]["windDir"]
    return weather, temp, wind_dir


def get_zh_weather(region):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    key = config["weather_key"]
    region_url = "https://geoapi.qweather.com/v2/city/lookup?location={}&key={}".format(region, key)
    response = get(region_url, headers=headers).json()
    if response["code"] == "404":
        print("推送消息失败，请检查地区名是否有误！")
        os.system("pause")
        sys.exit(1)
    elif response["code"] == "401":
        print("推送消息失败，请检查和风天气key是否正确！")
        os.system("pause")
        sys.exit(1)
    else:
        # 获取地区的location--id
        location_id = response["location"][0]["id"]
    weather_url = "https://devapi.qweather.com/v7/indices/1d?location={}&key={}&type=1,3,9,13".format(location_id, key)
    response = get(weather_url, headers=headers).json() ["daily"]
    # 天气指数
    for response_index, response_val in enumerate(response):  
            #指数名称
            zs_name = response_val ["name"]
            #指数等级
            level = response_val ["level"]
            #指数推荐
            category = response_val ["category"]
            # 指数解释
            zs_text = response_val ["text"]
    return zs_name, level, category, zs_text




if __name__ == "__main__":
    try:
        with open("config.txt", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)
    # 传入地区获取天气信息
    region = config["region"]
    zs_name, level, category, zs_text = get_zh_weather(region)
    print(zs_name+ level+ category+ zs_text)
    os.system("pause")
