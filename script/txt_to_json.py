
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime


def txt_to_json(file):

    #ファイルを開く
    txt = open(file, encoding="utf-8_sig")
    all_messages = txt.readlines()
    txt.close()

    # 全てのメッセージをまとめる
    each_message = []

    # 年・月・日・時間・分・秒を定義　（コメントの場合分けで使う）
    years = [str(i) for i in range(2020, 10000)]
    months = [str(i).zfill(2) for i in range(13)]
    days = [str(i).zfill(2) for i in range(32)]
    hours = [str(i).zfill(2) for i in range(24)]
    minutes = [str(i).zfill(2) for i in range(60)]

    ###### 各投稿の加工 ######
    i = 0
    while i < len(all_messages):

        # 送信が取り消された場合
        if "送信を取り消しました" in all_messages[i]:

            #そのコメントはスルー
            pass


        # 年・月・日を含んでいる場合
        elif all_messages[i][:4] in years and all_messages[i][5:7] in months and all_messages[i][8:10] in days and all_messages[i][4] == all_messages[i][7] == '.':

            # 配列に格納
            each_message.append(all_messages[i][:-1])


        # 時間:分を含んでいる場合
        elif all_messages[i][:2] in hours and all_messages[i][3:5] in minutes and all_messages[i][2] == ':':

            # 配列に格納
            each_message.append(all_messages[i][:-1])


        # それ以外　(同一コメント内で改行されている場合)
        else:

            # 最後のコメントに追加
            each_message[-1] += all_messages[i][:-1]

        i += 1


    # bodyの各項目をまとめる
    postTime_list = []
    postUser_list = []
    message_list = []
    createdAt_list = []

    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0

    j = 0
    while j < len(each_message):

        # 年・月・日を含んでいる場合
        if each_message[j][:4] in years and each_message[j][5:7] in months and each_message[j][8:10] in days and each_message[j][4] == each_message[j][7] == '.':

            # postTime用に年・月・日をセット
            year = each_message[j][:4]
            month = each_message[j][5:7]
            day = each_message[j][8:10]


        # 時間:分を含んでいる場合
        elif each_message[j][:2] in hours and each_message[j][3:5] in minutes and each_message[j][2] == ':':

            # postTime用に時間・分をセット
            hour = each_message[j][:2]
            minute = each_message[j][3:5]

            # postTimeを作成
            postTime = "{}-{}-{} {}:{}:00".format(year, month, day, hour, minute)

            word_array = each_message[j].split()

            # postUserを取得
            if len(word_array) == 2:
                postUser = ''
            else:
                postUser = word_array[1]

            # messageを取得
            if len(each_message[j].split()) == 2:
                message = word_array[1]
            else:
                message = ''.join(word_array[2:])

            # createdAtを取得
            now = datetime.datetime.now()
            createdAt = now.strftime('%Y-%m-%d %H:%M:%S')

            # bodyの各項目を、各配列に格納
            postTime_list.append(postTime)
            postUser_list.append(postUser)
            message_list.append(message)
            createdAt_list.append(createdAt)

        j += 1


    #JSONファイルの中身を書き込む
    JSON = {"resource":"/", "path":"/", "httpMethod":"GET", "body":{}}

    # bodyを挿入
    for l in range(len(postTime_list)):

        # bodyの各項目を辞書にまとめる
        dict_ = dict()
        dict_["postTime"] = postTime_list[l]
        dict_["postUser"] = postUser_list[l]
        dict_["message"] = message_list[l]
        dict_["createdAt"] = createdAt_list[l]

        # 辞書をbodyに格納
        JSON["body"][str(l+1)] = dict_


    # 現在時刻を取得
    now = datetime.datetime.now()

    # ファイルを命名
    filename = now.strftime('%Y%m%d%H%M%S')
    # now += timedelta(second=1)

    #新規作成したファイルを開く
    f = open("../json_files/{}.json".format(filename), "w", encoding='utf-8_sig')

    # JSONファイルの中身を書き込む
    json.dump(JSON, f, ensure_ascii=False, indent=4, separators=(',', ': '))
