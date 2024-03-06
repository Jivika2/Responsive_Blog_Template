from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
def HomePage(request):
  return render(request,"index.html")
def course(request):
  return HttpResponse('csit')
def blogpost(request):
  if request.method=="GET":
    output=request.GET.get('output')
  return render(request,"blogpost.html",{'output':output})
def contact(request):
  return render(request,'contact.html')
def search(request):
  return render(request,'search.html')
def userForm(request):
  finalans=0
  '''try:
    (using get method)if request.method=="GET":
    #n=int(request.GET['num'])
    #n1=int(request.GET['num1'])
      n1=int(request.GET.get('num1'))
      n2=int(request.GET.get('num2'))
    #print(n+n1);
      finalans=n1+n2
  except:
    pass'''
  data={}
  try:
    if request.method=="POST":
    #n=int(request.GET['num'])
    #n1=int(request.GET['num1'])
      n1=int(request.POST.get('num1'))
      n2=int(request.POST.get('num2'))
    #print(n+n1);
      finalans=n1+n2
      data={
        'n1':n1,
        'n2':n2,
        'output':finalans
      }
      url="/blogpost?output{}".format(finalans)
      return redirect(url)
      #return HttpResponseRedirect(url)
  except:
    pass
  return render(request,'userform.html',data)
  #return render(request,'userform.html',{'output':finalans})