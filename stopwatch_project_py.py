# -*- coding: utf-8 -*-
"""StopWatch Project.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zxRmFgJzzg_IC9B7XqzS7kDR7v8m_UmS
"""

import time

print("press the ENTER key to start ")
print("press the CTRL+c to exit timer")
while True:
    try:
        input()
        start = time.time()
        print("Started")
    except KeyboardInterrupt:
        print("Stopped")
        end = time.time()
        print("Total Time: ",round(end-start,2),"Seconds")
        break