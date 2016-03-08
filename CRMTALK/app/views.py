"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.template import RequestContext
from datetime import datetime
from app.forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from app.models import Lead, Contact, Note, User


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def register(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user=authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = CreateUserForm()
        return render(
            request,
            'app/register.html',
            context_instance = RequestContext(request,
            {
                'form': form
            })
        )

def details(request, leadcompany):
    #assert isinstance(request, HttpRequest)
    retDict=dict()
    retDict['lead']=list()
    retDict['contacts']=list()
    retDict['notes']=list()
    leads = Lead.objects.filter(company__iexact=leadcompany)
    for lead in leads:
        retDict['lead']=lead.owner.username
    contacts = Contact.objects.filter(lead__company__iexact=leadcompany)
    for contact in contacts:
        retDict['contacts'].append([contact.title,contact.phone,contact.direct,contact.fax,contact.cell,contact.lead.company])
    notes = Note.objects.filter(lead__company__iexact=leadcompany)
    for note in notes:
        retDict['notes'].append([note.text, note.commenter.username])
    return JsonResponse(retDict)

def leads(request):
    assert isinstance(request, HttpRequest)
    retDict=dict()
    leads = Lead.objects.all()
    for lead in leads:
        if not retDict.get(lead.status):
            retDict[lead.status] = [{'name':lead.company}]
        else:
            retDict[lead.status].append({'name':lead.company})
    return JsonResponse(retDict)