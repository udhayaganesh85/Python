import time
import threading

def first():
  for i in range(5):
    time.sleep(.5)
    print("Hello")


    
def second():
  for i in range(5):
    time.sleep(.5)
    print("World")

firstThd = threading.Thread(target = first)
secThd = threading.Thread(target = second)

firstThd.start()
secThd.start()


firstThd.join()
secThd.join()