# -*-coding:utf-8 -*-



#def software(request):
#    soft=SoftWare.objects.all()
#    content = {'soft':soft}
#    return render(request,'soft_index.html',content)

def deco(cls):
    def decorator(func):
        def wapper(*args,**kw):
            print (func.__name__)
            return func(*args,**kw)
        return wapper
    return decorator

@deco('mymodule')
def myfunc():
    print("test")

myfunc()

