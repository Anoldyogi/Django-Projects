from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def wishing(request):
	date=datetime.datetime.now()
	h=int(date.strftime('%H'))
	msg="<h1> Hello Friends How are you "
	if h<12:
		msg=msg+" GM "
	elif h<16:
		msg=msg+" GA "
	elif h<21:
		msg=msg+" GE "
	else:
		msg=msg+" GN "
	msg=msg+"</h1><hr>"
	msg=msg+"<h1> crrent time is "+str(date)+"</h1>"
	return HttpResponse(msg)
