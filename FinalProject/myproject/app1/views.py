from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *

# Create your views here.
def mainhome(request):
    return render(request, "mainhome.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")


def home(request):
    return render(request, "home.html")

def adminaccessfunction(request):
    return render(request, "adminentry.html")

def register(request):
    if request.method=='POST':
        m=registerform(request.POST)
        if m.is_valid():
            name=m.cleaned_data['n_ame']
            address=m.cleaned_data['a_ddress']
            email=m.cleaned_data['e_mail']
            pwd=m.cleaned_data['p_wd']
            n=registermodel(n_ame=name,a_ddress=address,e_mail=email,p_wd=pwd)
            n.save()
            return redirect('/app1/login')
        else:
            return HttpResponse('Error')
    else:
        return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        m=loginform(request.POST)
        if m.is_valid():
            email=m.cleaned_data['e_mail']
            pwd=m.cleaned_data['p_wd']
            c=registermodel.objects.all()
            for i in c:
                if email==i.e_mail and pwd==i.p_wd:
                    return redirect('/app1/mainhome/')
        else:
            return HttpResponse('Invalid email id or password')
    else:
        return render(request,"login.html")

def adminfunction(request):
    if request.method=='POST':
        q=adminform(request.POST)
        if q.is_valid():
            administrator=q.cleaned_data['a_dministrator']
            adminpwd=q.cleaned_data['a_dminpwd']
            if administrator=="Administrator" and adminpwd=="finalprojectadmin":
                 return redirect('/app1/adminaccess/')
        else:
            return HttpResponse('Error')
    else:
        return render(request,"admin.html")


def adminlogged(request):
    if request.method=='POST':
        return redirect('app1/')

def recipeload(request):
    if request.method == 'POST':
        a = recipeform(request.POST, request.FILES)
        if a.is_valid():
            item = a.cleaned_data['i_tem']
            price=a.cleaned_data['p_rice']
            file = a.cleaned_data['f_ile']
            b = recipemodel(i_tem=item, p_rice=price ,f_ile=file)
            b.save()
            return redirect('/app1/adminsgallery/')
        else:
            return HttpResponse('Error')
    else:
        return render(request, "recipeupload.html")

def adminrecipes(request):
    x=recipemodel.objects.all()
    l=[]
    m=[]
    for i in x:
        path=i.f_ile
        l.append(str(path).split("/")[2])
    return render(request,"admingallery.html",{'im': l})

def userdisplay(request):
    x=recipemodel.objects.all()
    l=[]
    m=[]
    n=[]
    for i in x:
        path=i.f_ile
        l.append(str(path).split("/")[2])
        m.append(i.i_tem)
        n.append(i.p_rice)
    return render(request,"recipe.html",{'z' : zip(l,m,n)})

def quantityselection(request,val):
    x=recipemodel.objects.filter(i_tem=val)
    return render(request,'priceshow.html',{'f_ile':x})

def orderbill(request):
    if request.method=="POST":
        item=request.POST.get('i_tem')
        price=request.POST.get('p_rice')
        quantity=request.POST.get('q_uantity')
        answer=int(price)*int(quantity)
        a=ordermodel(i_tem=item,p_rice=price,q_uantity=quantity,answer=answer)
        a.save()
    return render(request,'orderplacing.html',{'b_ill':answer,'i_tem':item})

def adminbilling(request):
    a=ordermodel.objects.all()
    return render(request,"adminbill.html",{'total':a})

