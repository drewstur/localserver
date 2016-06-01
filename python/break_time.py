import time
import webbrowser

total_break = 3
break_count = 0
print("This program started on "+time.ctime())
while(break_count < total_break):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=13ad95Ul-vg&list=PL14RUAozXp0wtqUeEFEJF2KuPoXmWzsSr&index=7")
    break_count += 1
