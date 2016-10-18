import thread
from time import sleep,ctime
loops = [4,2]
def loop0():
    print 'start loop 0 at: ', ctime()
    sleep(4)
    print 'loop 0 done at: ',ctime()

def loop1():
    print  'srart loop 1 at : ',ctime()
    sleep(2)
    print 'loop 1 done at : ',ctime()

def main():
    print "start:" ,ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(4)
    print 'all end:',ctime()

if __name__ =='__main__':
    main()
