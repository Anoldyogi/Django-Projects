from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"newsApp/index.html")


def sportsnews(request):
	head_msg='sports news below'
	msg1='kohli breaks records'
	msg2='Manchester United win CL'
	msg3='IPL to be held in dehradun'
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,"newsApp/news.html",context=my_dict)

def politicsnews(request):
	head_msg='politics news below'
	msg1='Modi to work hard for black money'
	msg2='Rahul to marry'
	msg3="Menka gandhi retires"
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,"newsApp/news.html",context=my_dict)

def moviesnews(request):
	head_msg='movies news below'
	msg1='Dhoom 28 to release on friday'
	msg2='Salman  to marry katrina'
	msg3="Sunny to promote ferrari"
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,"newsApp/news.html",context=my_dict)
