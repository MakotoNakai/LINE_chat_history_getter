
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime


def txt_to_json(file):
    #ファイルを開く
    txt = open(file)
    all_messages = txt.readlines()
    txt.close()

    #print(all_messages[8].split())

    # 全てのメッセージをまとめる
    each_message = []
    years = [str(i) for i in range(2020, 10000)]
    months = [str(i).zfill(2) for i in range(13)]
    days = [str(i).zfill(2) for i in range(32)]
    hours = [str(i).zfill(2) for i in range(24)]
    minutes = [str(i).zfill(2) for i in range(60)]

    i = 0
    while i < len(all_messages):

        if all_messages[i][:4] in years and all_messages[i][5:7] in months and all_messages[i][8:10] in days and all_messages[i][4] == all_messages[i][7] == '.':

            each_message.append(all_messages[i][:-1])

        elif all_messages[i][:2] in hours and all_messages[i][3:5] in minutes and all_messages[i][2] == ':':

            each_message.append(all_messages[i][:-1])

        else:
            each_message[-1] += all_messages[i][:-1]

        i += 1

    # for message in each_message:
    #     print(message[5:7])


    # Bodyの各項目をまとめる
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


        if each_message[j][:4] in years and each_message[j][5:7] in months and each_message[j][8:10] in days and each_message[j][4] == each_message[j][7] == '.':

            year = each_message[j][:4]
            month = each_message[j][5:7]
            day = each_message[j][8:10]

        elif each_message[j][:2] in hours and each_message[j][3:5] in minutes and each_message[j][2] == ':':

            hour = each_message[j][:2]
            minute = each_message[j][3:5]
            postTime = "{}-{}-{} {}:{}:00".format(year, month, day, hour, minute)

            word_array = each_message[j].split()

            if len(word_array) == 2:
                postUser = ''
            else:
                postUser = word_array[1] + word_array[2]

            if len(each_message[j].split()) == 2:
                message = each_message[j].split()[1]
            else:
                message = ''.join(each_message[j].split()[3:])

            now = datetime.datetime.now()
            createdAt = now.strftime('%Y-%m-%d %H:%M:%S')

            postTime_list.append(postTime)
            postUser_list.append(postUser)
            message_list.append(message)
            createdAt_list.append(createdAt)

        j += 1


    #JSONファイルの中身を書き込む
    JSON = {"resource":"/", "path":"/", "httpMethod":"GET", "body":{}}

    ### bodyを挿入 ####
    for l in range(len(postTime_list)):

        dict_ = dict()
        dict_["postTime"] = postTime_list[l]
        dict_["postUser"] = postUser_list[l]
        dict_["message"] = message_list[l]
        dict_["createdAt"] = createdAt_list[l]

        JSON["body"][str(l+1)] = dict_

    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d%H%M%S')
    f = open("../json_files/{}.json".format(filename), "w")
    json.dump(JSON, f, ensure_ascii=False, indent=4, separators=(',', ': '))
