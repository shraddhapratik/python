from django.shortcuts import render,redirect
from .models import Employee,Address
from .forms import EmployeeForm,AddressForm
from django.http import HttpResponse,HttpResponseRedirect


def showoneemp(request):
    employees = Employee.objects.all()

    eform = EmployeeForm()
    return render(request,'oneempl.html',{'empList' : employees,'form' : eform})


def add_Update_empone(request):
    if request.method == "POST":
        print('----------',request.POST)
        if request.POST['id'] != '':
            emp = Employee.objects.get(eid=request.POST['eid'])
            form = EmployeeForm(request.POST,instance=emp)
        else:
            form = EmployeeForm(request.POST)
        form.save()
        return redirect('/oneEmpl')


def edit_employeeone(request,id):
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
    return render(request, 'oneempl.html', {'emp' : emp,'empList': employees, 'form': form})


def delete_employeeone(request,id):
    emp = Employee.objects.get(eid=id)
    emp.delete()
    return redirect("/oneEmpl")


##############addresss################

def showmanyaddress(request):
    addr = Address.objects.all()
    print(addr)
    aform = AddressForm()
    return render(request,'addressmany.html',{'addressList' : addr,'form' : aform})


def add_manyaddress(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['emp'][1])



        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            '''aid = request.POST.get("aid")
            acity = request.POST.get("acity")
            astate = request.POST.get("astate")
            emp_id = request.POST.get("emp")
            address = Address.objects.create(aid=aid, acity=acity, astate=astate, emp_id=emp_id)'''
            return HttpResponseRedirect("/manyAddress")
        else:
            return HttpResponse("form is not validated")
        #return redirect('/manyAddress')


def edit_manyaddress():
    pass


def delete_manyaddress(request,id):
    addr = Address.objects.get(aid=id)
    addr.delete()
    return redirect("/manyAddress")