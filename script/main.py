
from move_mouse import move_mouse
from txt_to_json import txt_to_json
import urllib.request

import datetime
import requests
import glob
import time
import json
import os

if __name__ == "__main__":

    # # 以下のプログラムを延々と実行する
    # while True:
    #
    # # カーソルを自動操作する
    # move_mouse()
    #
    # # ダウンロードしたファイルのpathを取得する
    # txt_path = '../txt_files/'
    # now = datetime.datetime.now()
    # now += datetime.timedelta(seconds=1)
    # txt_path += now.strftime('%Y%m%d%H%M%S') + '.txt'
    #
    # time.sleep(5)
    #
    # #.txtファイルを.jsonファイルに変換する
    # txt_to_json(txt_path)
    #
    # time.sleep(5)
    #
    # json_list = glob.glob('../json_files/*')
    # json_data = max(json_list, key=os.path.getctime)
    # print(json_data)


    # url = "https://o9s422tqzg.execute-api.ap-northeast-1.amazonaws.com/prod/"
    # method = "POST"
    # headers = {"Content-Type":"applic
    # # json_data = "../json_files/20200827230652.json"
    #
    # request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    #
    # with urllib.request.urlopen(request) as response:
    #     response_body = response.read().decode("utf-8")


    url = "https://o9s422tqzg.execute-api.ap-northeast-1.amazonaws.com/prod/"

    json_open = open( "../json_files/20200827230652.json", "r", encoding="utf-8_sig")
    json_load = json.load(json_open)
    response = requests.post(url, json = json_load)

    resDatas = response.json()
    print(response)
