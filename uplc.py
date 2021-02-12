if __name__ != "uplc":
    print("Not allowed to import as " + str(__name__))

import json
import datetime

def obtain_time(acc):
    dtobj = datetime.datetime.now()
    y = str(dtobj.year)
    m = str(dtobj.month)
    d = str(dtobj.day)
    h = str(dtobj.hour)
    mi = str(dtobj.minute)
    s = str(dtobj.second)
    da = "-"
    cl = ":"
    if str(acc) == "0":
        ret = y+da+m+da+d+da+h+da+mi+da+s
        return ret
    elif str(acc) == "1":
        ret = m+da+d+da+h+da+mi+da+s
        return ret
    elif str(acc) == "2":
        ret = d+da+h+da+mi+da+s
        return ret
    elif str(acc) == "3":
        ret = h+cl+mi+cl+s
        return ret
    else:
        return "Options you provided is not valid"

class LogsCreator():
    def __init__(self, filename="DefaultLog"):
        self.fobj = open(str(filename + ".ulog"), 'a')
    def write(self, text, lvl="info",time_accuracy="0"):
        time = obtain_time(time_accuracy)
        construct_string = "[" + str(time) + "] [" + str(lvl.upper()) + "] " + str(text)
        self.fobj.write(construct_string + "\n")
        return True
    def close(self):
        self.fobj.close()
