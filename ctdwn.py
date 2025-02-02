import time
def ctdwn(s):
    sec = s
    digitlen = len(str(sec))
    while sec >= 0:
        print(sec, end="\r")
        time.sleep(1)
        sec -= 1
