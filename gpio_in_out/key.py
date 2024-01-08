#本代码需要使用管理员权限运行
from pynq import Overlay
import os
import time
overlay=Overlay('./design_1.bit')
led = overlay.axi_gpio_0
key = overlay.axi_gpio_1
print("gpio start!")
states=[1,2,4,8]
state=0
led.write(0x00,15)
while 1:
    led.write(0x04,states[state%4])
    state=state+1
    time.sleep(0.5)
    if not key.read(0x00):
        print("stopping...")
        break;
led.write(0x00,0)
pid=os.getpid()
print(f"key.py stop.pid:{pid}")
    


