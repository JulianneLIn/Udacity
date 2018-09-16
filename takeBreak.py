import webbrowser
import time

total_break = 3
break_count = 0

print("This program start on " +time.ctime())
while(break_count < total_break):
    time.sleep(60)
    webbrowser.open("https://www.youtube.com/watch?v=6YZlFdTIdzM")
    break_count = break_count + 1
