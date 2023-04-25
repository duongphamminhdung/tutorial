from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members


def index(request):
    mymembers = Members.objects.all().values()
    #update ID
    prev = 0
    for member in Members.objects.all():
        if member.id != prev+1:
            temp = member.id
            member.id = prev+1
            Members.objects.get(id=temp).delete()
        prev += 1
        member.save()
    #update ID complete
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
  

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    member = Members(title=request.POST['title'])
    member.title = request.POST['title']
    member.hs11 = request.POST['hs11']
    member.hs12 = request.POST['hs12']
    member.hs13 = request.POST['hs13']
    member.hs14 = request.POST['hs14']
    member.CK = request.POST['CK']
    member.GK = request.POST['GK']
    member.GOAL = request.POST['GOAL']
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    member = Members.objects.get(id=id)
    member.title = request.POST['title']
    member.hs11 = request.POST['hs11']
    member.hs12 = request.POST['hs12']
    member.hs13 = request.POST['hs13']
    member.hs14 = request.POST['hs14']
    member.CK = request.POST['CK']
    member.GK = request.POST['GK']
    member.GOAL = request.POST['GOAL']
    member.save()
    return HttpResponseRedirect(reverse('index'))
 
def calc(request):
    mymember = Members.objects.all().values()
    m = {}
    for i in mymember:
        mean_ = 0
        count = 0
        if float(i['hs11']) == 0.0:count += 1
        if float(i['hs12']) == 0.0:count += 1
        if float(i['hs13']) == 0.0:count += 1
        if float(i['hs14']) == 0.0:count += 1
        if float(i['GK']) == 0.0:count += 2
        if float(i['CK']) == 0.0:count += 3
        mean_ = float(i['GOAL'])*9-(float(i['hs11'])+float(i['hs12'])+float(i['hs13'])+float(i['hs14'])+float(i['GK'])*2+float(i['CK'])*3)
        mean_ = mean_ / count if count != 0 else 0
        mean_ = round(mean_, 2)
        mean_ = 'aim: ' + str(mean_)

        mem = Members.objects.get(id=i['id'])
        mem.hs11 = mean_ if float(i['hs11']) == 0.0 else mem.hs11
        mem.hs12 = mean_ if float(i['hs12']) == 0.0 else mem.hs12
        mem.hs13 = mean_ if float(i['hs13']) == 0.0 else mem.hs13
        mem.hs14 = mean_ if float(i['hs14']) == 0.0 else mem.hs14
        mem.GK = mean_ if float(i['GK']) == 0.0 else mem.GK
        mem.CK = mean_ if float(i['CK']) == 0.0 else mem.CK
        m.update({i['id']:mem})
    template = loader.get_template('calc.html')
    context = {
    'mem': m,
    }
    for i, x in m.items():
        # print(x.title, x.hs11, x.hs12)
        print(x)
    return HttpResponse(template.render(context, request))
