#本程序不使用
import os
import time
import psutil

def kill_process(pid):
    parent_proc = psutil.Process(pid)
    for child_proc in parent_proc.children(recursive=True):
        child_proc.kill()
    parent_proc.kill()

pid=os.fork()
if(pid!=0):#父进程
    print(f"key进程编号{os.getpid()}")
    time.sleep(1)
    os.system("sudo python key.py")
    print("parent_pid_end")
    kill_process(os.getpid())
    exit(0)
if not pid:#子进程
    print("请在1秒后，10秒内输入密码欸：")
    time.sleep(10)
    print("开始运行检测程序：")
    print(f"face进程编号{os.getpid()}")
    os.system("python faceDetect.py")
            
                
            
    

    