import pyscreenshot
from screeninfo import get_monitors
import subprocess
import os

from win32api import GetMonitorInfo, MonitorFromPoint
def getTaskBarHeight():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    # print("The taskbar height is {}.".format(monitor_area[3]-work_area[3]))
    return monitor_area[3] - work_area[3]

def getDimensions():
    for m in get_monitors():
        width = m.width
        height = m.height
    return width, height

# def screenshot(fileName):


def getFen(width, height):
    #initial board
    # fen1 = chess.Board("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1")
    # os.system('python tensorflow_chessbot.py --filepath ss.png')
    
    wd = os.getcwd()
    pic = pyscreenshot.grab(bbox=(0, 0, width , height))
    pic.save("ss.png")
    os.chdir("../models/")
    out = subprocess.Popen(['python', 'tensorflow_chessbot.py', '--filepath', '..\\util\\ss.png'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)

    # out = subprocess.Popen(['python', 'models\\tensorflow_chessbot.py', '--filepath', 'util\ss.png'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
    stdout, stderr = out.communicate()
    stdoutls = stdout.decode('UTF-8').split("\r")
    fen = stdoutls[-3]

    os.chdir(wd)
    return fen