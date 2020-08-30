
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

    while True:

        starttime = time.time()

        # #カーソルを自動操作する
        move_mouse()

        time.sleep(1)

        # # ダウンロードしたファイルのpathを取得する
        txt_list = glob.glob('../txt_files/*')
        txt_data = max(txt_list, key=os.path.getctime)

        #.txtファイルを.jsonファイルに変換する
        txt_to_json(txt_data)

        time.sleep(1)

        json_list = glob.glob('../json_files/*')
        json_data = max(json_list, key=os.path.getctime)
        json_open = open(json_data, "r", encoding="utf-8_sig") # かぶっているもの
        json_load = json.load(json_open)

        url = "https://o9s422tqzg.execute-api.ap-northeast-1.amazonaws.com/prod/"
        response = requests.post(url, json = json_load)
        resDatas = response.json()

        time.sleep(14.6)

        endtime = time.time()
        print("done")
