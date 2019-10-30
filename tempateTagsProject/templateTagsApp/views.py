from django.shortcuts import render
import datetime
# Create your views here.
def dateinfo(request):
	date=datetime.datetime.now()
	guest='Sunny'
	msg=''
	h=int(date.strftime('%H'))
	if h<12:
		msg='Good Morning'
	elif h<16:
		msg='Good AfterNoon'
	elif h<21:
		msg='Good Evening'
	else:
		msg='Good Night'
	my_dict={'date':date,'guest':guest,'msg':msg}
	return render(request,'templateApp/test.html',context=my_dict)
