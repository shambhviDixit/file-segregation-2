import time
seconds=input("enter seconds")
def countdown(seconds):
    mins = int(seconds/60)
    secs=int(seconds%60)
    timer = f'{mins}:{secs}'
    print(timer)
    seconds -=1
    print('time up!!!')
countdown(int(seconds))