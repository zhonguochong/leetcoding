import time
def timer(func):
    def wrapper(*args, **kwds):
        t0=time.time()
        func(*args,**kwds)
        t1=time.time()
        print('take time: %0.3f' % (t1-t0))
    return wrapper