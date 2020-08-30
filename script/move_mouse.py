import pyautogui as pg
import datetime
import time

# 想定デバイスはWindows10
# Toolbarの右上にトークルームの右下を合わせた場合を想定


def move_mouse():

    # 1番下をクリック
    pg.moveTo(1238, 547)
    pg.click()

    # 3本線をクリック
    pg.moveTo(1263, 327)
    pg.click()

    # Save chatをクリック
    pg.moveTo(1200, 527)
    pg.click()

    # 元のファイル名を消去
    pg.keyDown('backspace')
    for i in range(14):
        pg.press('backspace')
    pg.keyUp('backspace')

    # ファイル名を記入
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d%H%M%S') + '.txt'
    pg.typewrite(filename)

    # savesをクリック
    pg.moveTo(998, 689)
    pg.click()

if __name__ == "__main__":

    move_mouse()
