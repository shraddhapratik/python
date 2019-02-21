from django.shortcuts import render,redirect
from emp_mapping.models import Employee,Address
from emp_mapping.forms import EmployeeForm,AddressForm
from django.http import HttpResponse,HttpResponseRedirect


def showemp(request):
    employees = Employee.objects.all()
    eform = EmployeeForm()
    return render(request,'empone.html',{'empList' : employees,'form' : eform})


def add_Update_emp(request):
    if request.method == "POST":
        print('----------',request.POST)
        if request.POST['id'] != '':
            emp = Employee.objects.get(eid=request.POST['eid'])
            form = EmployeeForm(request.POST,instance=emp)
        else:
            form = EmployeeForm(request.POST)
        form.save()
        return redirect('/empone')


def edit_empone(request,id):
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
    return render(request, 'empone.html', {'emp' : emp,'empList': employees, 'form': form})


def delete_empone(request,id):
    emp = Employee.objects.get(eid=id)
    emp.delete()
    return redirect("/empone")


##############addresss################

def showaddress(request):
    addr = Address.objects.all()
    aform = AddressForm()
    return render(request,'addressone.html',{'addressList' : addr,'form' : aform})


def add_address(request):
    if request.method == 'POST':
        print(request.POST)
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            '''aid = request.POST.get("aid")
            acity = request.POST.get("acity")
            astate = request.POST.get("astate")
            emp_id = request.POST.get("emp")
            address = Address.objects.create(aid=aid, acity=acity, astate=astate, emp_id=emp_id)'''
            return HttpResponseRedirect("/address")
        else:
            return HttpResponse("form is not validated")
        #return redirect('/address')



def edit_address():
    pass


def delete_address(request,id):
    addr = Address.objects.get(aid=id)
    addr.delete()
    return redirect("/address")