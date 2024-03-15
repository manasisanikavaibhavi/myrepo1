from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .models import Registration
from .models import feedback
from .models import contact 
from .models import artistfrom
from .models import Payment


# Create your views here.
def display(request):
    return render(request,'login.html')

def show(request):
    return render(request,'Registration.html')

def clear(request):
    return render(request,'feedback.html')

def present(request):
    return render(request,'mycontact.html')

def art(request):
    return render(request,'artistfrom.html')

def start(request):
    return render(request,'homepage.html')
def myoffer(request):
    return render(request,'offers2.html')


def collect(request):
    return render(request,'collections.html')
def exhibit(request):
    return render(request,'exhibition.html')
def review(request):
    return render (request,'reviews.html')
def about(request):
    return render(request,'aboutus.html')
def paintig(request):
    return render(request,'paint.html')

def Radh(request):
    return render(request,'radha.html')
def dood(request):
    return render(request,'doodle.html')

def arch(request):
    return render(request,'architecture1.html')
def sculp(request):
    return render(request,'sculp.html')
def sprodut(request):
    return render(request,render,'sproduct1.html')
def mycart(request):
    return render(request,'cart.html')
def makepayment(request):
    return render(request,'payment.html')






def receive(request):
    if request.method=='POST':
        myemail=request.POST.get('myemail')
        mypwd=request.POST.get('mypsw')

        z=Login(email=myemail,password=mypwd)
        z.save()
        return HttpResponse("Data Entered ...")
    else:
        return HttpResponse('Invalid Request')
    



def doreg(request):
    if request.method=='POST':
        myname=request.POST.get('myname')
        myemail=request.POST.get('myemail')
        myphone=request.POST.get('myphone')
        myaddress=request.POST.get('myaddress')
        mycountry=request.POST.get('mycountry')
        mycity=request.POST.get('mycity')
        myregion=request.POST.get('myregion')
        mycode=request.POST.get('mycode')

        z=Registration(name=myname,email=myemail,phone=myphone,address=myaddress,country=mycountry,city=mycity,region=myregion,code=mycode)
        z.save()
        return HttpResponse("data is suessfull enter")
    else:
        return HttpResponse('Invalid Request')
    

def feed(request):
    if request.method=='POST':
        myname=request.POST.get('myname')
        myemail=request.POST.get('myemail')
        myphone=request.POST.get('myphone')
        satisfy=request.POST.get('satisfy')
       
        msg=request.POST.get('msg')

        z=feedback(name=myname,email=myemail,phone=myphone,satisfy=satisfy,msg=msg)
        z.save()
        return HttpResponse("Data Enter...")
    else:
        return HttpResponse('Invalid Request...')
    

def com(request):
    if request.method=='POST':
        myname=request.POST.get('myname')
        myemail=request.POST.get('myemail')
        mymessage=request.POST.get('mymessage')

        z=contact (name=myname,email=myemail,message=mymessage)
        z.save()
        return HttpResponse("Data Enter...")
    else:
        return HttpResponse('Invalid Request...')
    

def artist(request):
    if request.method=='POST':
        myname=request.POST.get('myname')
        myart=request.POST.get('myart')
        myartname=request.POST.get('myartname')
        myage=request.POST.get('myage')
        myamount=request.POST.get('myamount')
        mynation=request.POST.get('mynation')
        myemail=request.POST.get('myemail')
        myphone=request.POST.get('myphone')
        myimage=request.POST.get('myimage')
        z=artistfrom (name=myname,art=myart,artname=myartname,age=myage,Amount=myamount, Nationality=mynation,email=myemail,phone=myphone,image=myimage)
        z.save()
        return HttpResponse("Data Enter...")
    else:
        return HttpResponse('Invalid Request...')

def repartist(request):
    art=artistfrom.objects.all()
    return render(request,'report1.html',{'art':art}) 

def replogin(request):
     log=Login.objects.all()
     return render(request,'report2.html',{'log':log})


def repregister(request):
     Register =Registration.objects.all()
     return render(request,'report3.html',{'Register':Register})


def repcontact (request):
     cont1 =contact.objects.all()
     return render(request,'report4.html',{'cont1':cont1})


def repfeedback (request):
     Feed =feedback.objects.all()
     return render(request,'report5.html',{'Feed':Feed})

def dopayment(request):
    if request.method=="POST":
        name=request.POST.get('name')
        cardname=request.POST.get('cardname')
        email=request.POST.get('email')
        address=request.POST.get('addr')
        city=request.POST.get('city')
        pay_detail=request.POST.get('pay')
        cardno=request.POST.get('cardno')
        cvc=request.POST.get('cvc')
        phoneno=request.POST.get('phoneno')
        month=request.POST.get('month')
        year=request.POST.get('year')
        amount=request.POST.get('amount')
        z=Payment(name=name,email=email,cardname=cardname,address=address,city=city,pay_detail=pay_detail,cardno=cardno,cvc=cvc,phoneno=phoneno,month=month,year=year,amount=amount)
        z.save()
        return HttpResponse("<h1>Your Payment Is Received Successfully...</h1>")
    else:
        return HttpResponse("<h1>Invalid Request...</h1>")


    
