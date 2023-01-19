from django.shortcuts import render

def app(request):
    return render(request,"index.html")

def show(request):
    val=request.GET['val']
    return render(request,'show.html',{'val':val})