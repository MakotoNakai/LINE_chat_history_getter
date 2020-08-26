import pyautogui as pg
import datetime
import time

# # Toolbarの右上にトークルームの右下を合わせた場合を想定
# positionX, positionY = pg.position()
# print(positionX, positionY)

# 3本線をクリック
pg.moveTo(1242, 305)
pg.click()

# Save chatをクリック
pg.moveTo(1196, 403)
pg.click()

# 緑のボタン(OK)をクリック
pg.moveTo(1072, 561)
time.sleep(0.2)
pg.click()

# ファイル名に移動
pg.moveTo(612, 85)
time.sleep(0.2)
pg.click()

# ファイル名を記入
pg.keyDown('backspace')
for i in range(10):
    pg.press('backspace')
pg.keyUp('backspace')

now = datetime.datetime.now()
filename = now.strftime('%Y%m%d%H%M%S') + '.txt'
pg.typewrite(filename)

# LINE_chat_history_getterフォルダをクリック
pg.moveTo(275, 331)
pg.click()

# downloadフォルダをクリック
pg.moveTo(461, 180)
pg.click()

# Saveボタンをクリック
pg.moveTo(1005, 744)
pg.click()





