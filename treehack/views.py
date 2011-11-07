# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from codes.models import *
from django.core import serializers
from django.utils import simplejson
from parser.parse import *
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, Context

def GiveGetCode(request):
     if request.is_ajax():
          if request.method == "POST":
               parsed = HACK(request.POST["code"])
               thiscode = Code(rawcode = request.POST["code"],
                               serialcode = parsed)
               thiscode.save()
               return HttpResponse(simplejson.dumps({"ID": thiscode.id , "parsed":parsed}), 'application/json')
          elif request.method == "GET":
               # probably want to return a 404 if object doesnt exist
               thiscode = Code.objects.get(id=request.GET["ID"])
               return HttpResponse(simplejson.dumps({"raw":thiscode.rawcode, "parsed":HACK(thiscode.rawcode)}), 'application/json')
          else:
               return HttpResponse( simplejson.dumps( {'4':3} ) )
     else:
          # probably want to return a 404 or something
          return HttpResponse( simplejson.dumps( {'4':3} ) )

def DisplayCode(request, ID):
     return render_to_response('results.html', context_instance=RequestContext(request))
