"""employee_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import add_or_update_emp,edit_emp,show,delete_emp
from emp_mapping.views import showemp,add_Update_emp,edit_empone,delete_empone,showaddress,add_address,edit_address,delete_address
from emp_many_mapping.views import showoneemp,add_Update_empone,edit_employeeone,delete_employeeone,showmanyaddress,add_manyaddress,edit_manyaddress,delete_manyaddress

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', show),
    path('create/', add_or_update_emp),
    path('edit/<int:id>', edit_emp),
    path('delete/<int:id>', delete_emp),

    ##ONE TO ONE##
    path('empone/', showemp),
    path('addEmp/', add_Update_emp),
    path('editEmp/<int:id>', edit_empone),
    path('deleteEmp/<int:id>', delete_empone),

    path('address/', showaddress),
    path('addAddress/', add_address),
    path('editAddress/<int:id>', edit_address),
    path('deleteAddress/<int:id>', delete_address),

    ##ONE TO MANY##
    path('oneEmpl/', showoneemp),
    path('addOneEmp/', add_Update_empone),
    path('editEmpOne/<int:id>', edit_employeeone),
    path('deleteEmpOne/<int:id>', delete_employeeone),

    path('manyAddress/', showmanyaddress),
    path('addManyAddress/', add_manyaddress),
    path('editManyAddress/<int:id>', edit_manyaddress),
    path('deleteAddress/<int:id>', delete_manyaddress),

]
