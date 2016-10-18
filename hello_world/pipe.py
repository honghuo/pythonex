# coding=utf-8
# 此文件在linux上运行
import multiprocessing
def procl(pipe):
    pipe.send('hello ')
    print('procl rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec: ',pipe.recv())
    pipe.send('hello,too')

pipe = multiprocessing.Pipe()
p1 = multiprocessing.Process(target=procl,args=(pipe[0],))
p2 = multiprocessing.Process(target=proc2,args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()
