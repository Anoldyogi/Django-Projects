from django.shortcuts import render
from newsApp.models import employee


# Create your views here.
def index(request):
	return render(request,'empApp/index.html')
def empview(request):
	emp_list=employee.objects.all()
	my_dict={'emp_list':emp_list}
	return render(request,'empApp/emp.html',context=my_dict)
