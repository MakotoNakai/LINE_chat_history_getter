
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

    # # #カーソルを自動操作する
    # move_mouse()
    #
    # # # ダウンロードしたファイルのpathを取得する
    # txt_path = '../txt_files/'
    # now = datetime.datetime.now()
    # now += datetime.timedelta(seconds=2)
    # txt_path += now.strftime('%Y%m%d%H%M%S') + '.txt'
    #
    # time.sleep(5)

    #.txtファイルを.jsonファイルに変換する
    #txt_to_json('../txt_files/pentas.txt')

    # time.sleep(1)
    #
    # json_list = glob.glob('../json_files/*')
    # json_data = max(json_list, key=os.path.getctime)
    # print("File name:", json_data)
    #
    # print()


    url = "https://o9s422tqzg.execute-api.ap-northeast-1.amazonaws.com/prod/"
    #
    # json_open = open( "../json_files/20200828172902.json", "r", encoding="utf-8_sig") # ぺんたさんが入ってるもの
    json_open = open( "../json_files/20200829005437.json", "r", encoding="utf-8_sig") # かぶっているもの
    json_load = json.load(json_open)
    response = requests.post(url, json = json_load)

    resDatas = response.json()
    print(response) # <Response [200]>
    print()
    print(resDatas)
    print()

    # ぺんたさんが入ってるもののresponse
    # {'errorMessage': '(1064, \'You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near \\\'わ"\\\' at line 1\')', 'errorType': 'ProgrammingError', 'stackTrace': ['  File "/var/task/lambda_function.py", line 23, in lambda_handler\n    cursor.execute("select * from messages where post_time=\\"" + message["postTime"] + "\\" and post_user=\\"" + message["postUser"] + "\\";")\n', '  File "/var/task/pymysql/cursors.py", line 163, in execute\n    result = self._query(query)\n', '  File "/var/task/pymysql/cursors.py", line 321, in _query\n    conn.query(q)\n', '  File "/var/task/pymysql/connections.py", line 505, in query\n    self._affected_rows = self._read_query_result(unbuffered=unbuffered)\n', '  File "/var/task/pymysql/connections.py", line 724, in _read_query_result\n    result.read()\n', '  File "/var/task/pymysql/connections.py", line 1069, in read\n    first_packet = self.connection._read_packet()\n', '  File "/var/task/pymysql/connections.py", line 676, in _read_packet\n    packet.raise_for_error()\n', '  File "/var/task/pymysql/protocol.py", line 223, in raise_for_error\n    err.raise_mysql_exception(self._data)\n', '  File "/var/task/pymysql/err.py", line 107, in raise_mysql_exception\n    raise errorclass(errno, errval)\n']}


    # かぶってるもののresponse
