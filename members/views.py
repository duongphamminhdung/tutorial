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
            member.objects.get(id=temp).delete()
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
    x = request.POST['title']
    y = request.POST['content']
    member = Members(title=x, content=y)
    member.tomtat = request.POST['tomtat']
    member.type = request.POST['type']
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
    member.content = request.POST['content']
    member.id = request.POST['id']
    member.tomtat = request.POST['tomtat']
    member.type = request.POST['type']
    member.save()
    return HttpResponseRedirect(reverse('index'))
 
