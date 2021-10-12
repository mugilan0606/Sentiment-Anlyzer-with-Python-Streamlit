from django.shortcuts import render
from subprocess import run,PIPE
import sys
def button(request):
    return  render(request,'test.html')

def test1(request):
    input1=request.POST.get('inp')
    out =run([sys.executable,'D://Internship//front end//test.py',input1],shell=False,stdout=PIPE)
    print(out)

    return render(request,'test.html',{'data1':out.stdout.decode('utf-8')})