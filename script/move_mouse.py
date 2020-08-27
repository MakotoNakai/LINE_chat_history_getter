import pyautogui as pg
import datetime
import time

# 想定デバイスはMacbook Pro 13-inch
# Toolbarの右上にトークルームの右下を合わせた場合を想定


def move_mouse():

    # 3本線をクリック
    pg.moveTo(1242, 305)
    pg.click()

    # Save chatをクリック
    pg.moveTo(1196, 403)
    pg.click()

    # 緑のボタン(OK)をクリック
    pg.moveTo(1072, 561)
    time.sleep(0.5)
    pg.click()

    # ファイル名に移動
    pg.moveTo(630, 74)
    time.sleep(0.5)
    pg.click()

    # ファイル名を記入
    pg.keyDown('backspace')
    for i in range(10):
        pg.press('backspace')
    pg.keyUp('backspace')

    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d%H%M%S') + '.txt'
    pg.typewrite(filename)

    # savesをクリック
    pg.moveTo(327, 298)
    pg.click()






