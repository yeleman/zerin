#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import os
import sys
import subprocess
import signal

HTTP_PORT = 5000


def main_http():
    from http import runserver
    runserver(False)


def killprocess(proc):
    proc.terminate()
    try:
        proc.send_signal(signal.CTRL_C_EVENT)
    except:
        pass
    try:
        proc.send_signal(signal.CTRL_BREAK_EVENT)
    except:
        pass

    try:
        import ctypes
        # 0 => Ctrl-C
        ctypes.windll.kernel32.GenerateConsoleCtrlEvent(0, proc.pid)
    except:
        pass


def main_gui():
    from PySide import QtGui
    from mainwindow import MainWindow

    target = "zmain.exe" if os.path.exists("zmain.exe") else "zmain.py"
    http = subprocess.Popen([sys.executable, target, "--runserver", str(HTTP_PORT)],
                            shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.base_url = u'http://127.0.0.1:%d' % HTTP_PORT
    window.show()

    ret = app.exec_()
    # shutdown runserver
    killprocess(http)
    # http.terminate()
    sys.exit(ret)

if __name__ == "__main__":
    print(sys.argv)
    if '--runserver' in sys.argv:
        print("HTTP")
        sys.argv.remove('--runserver')
        main_http()
    else:
        print("GUI")
        main_gui()
