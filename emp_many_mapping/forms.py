from django import forms
from .models import Employee,Address


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


def getListOfEmp():
    listOfEmps = Employee.objects.all()
    #print(listOfEmps)
    #print(type(listOfEmps))
    choicesList = []
    for emp in listOfEmps:
        #print(emp.ename)
        choicesList.append((emp.eid,emp.ename))
    return choicesList


class AddressForm(forms.ModelForm):
    aid = forms.IntegerField()
    acity = forms.CharField()
    astate = forms.CharField()
    emp_choices = getListOfEmp()
    #print(emp_choices)
    #emp = forms.CharField(label='', widget=forms.MultipleChoiceField(choices=emp_choices))
    emp = forms.MultipleChoiceField(choices=emp_choices)

    class Meta:
        model = Address
        fields = ['aid', 'acity', 'astate', 'emp']





