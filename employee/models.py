from django.db import models


class Employee(models.Model):
    eid=models.CharField(max_length=20,primary_key=True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    eage=models.IntegerField()
    esalary=models.IntegerField()
    eaddress=models.CharField(max_length=300)

    class Meta:
        db_table = "emp_info"