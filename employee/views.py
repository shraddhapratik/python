from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import EmployeeForm
from django.http import HttpResponse


def show(request):
    employees = Employee.objects.all()
    form = EmployeeForm()
    return render(request,'empInfo.html',{'empList' : employees,'form' : form})


def add_or_update_emp(request):
    if request.method == "POST":
        if request.POST['id'] != '':
            emp = Employee.objects.get(eid=request.POST['eid'])
            form = EmployeeForm(request.POST,instance=emp)
        else:
            form = EmployeeForm(request.POST)
        form.save()
        return redirect('/emp')


def edit_emp(request,id):
    emp = Employee.objects.get(eid=id)
    employees = Employee.objects.all()
    form = EmployeeForm()
    form.initial['eid'] = emp.eid
    form.initial['ename'] = emp.ename
    form.initial['eage'] = emp.eage
    form.initial['econtact'] = emp.econtact
    form.initial['eemail'] = emp.eemail
    form.initial['eaddress'] = emp.eaddress
    form.initial['esalary'] = emp.esalary
    return render(request, 'empInfo.html', {'emp' : emp,'empList': employees, 'form': form})


def delete_emp(request,id):
    emp = Employee.objects.get(eid=id)
    emp.delete()
    return redirect("/emp")