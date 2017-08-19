def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def helloworld():
    print ('Hello World')



helloworld()
#print('function %s called'%(helloworld.__name__))
