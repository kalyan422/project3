from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def calculate(request):
    X=int(request.POST["t1"])
    Y=int(request.POST["t2"])
    op=request.POST["op"]
    res=0
    data=""
    if op=="add":
        res=X+Y
        data="the SUM is:"
    elif op=="sub":
        res=X-Y
        data="the SUB is:"
    elif op=="mul":
        res=X*Y
        data="the MUL is:"
    else:
        res=X/Y
        data="the DIV is:"
    return HttpResponse(data+str(res))

