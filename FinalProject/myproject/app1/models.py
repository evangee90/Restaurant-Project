from django.db import models

# Create your models here.
class registermodel(models.Model):
    n_ame=models.CharField(max_length=30)
    a_ddress=models.CharField(max_length=50)
    e_mail=models.CharField(max_length=20)
    p_wd=models.CharField(max_length=20)

class recipemodel(models.Model):
    i_tem=models.CharField(max_length=20)
    p_rice=models.IntegerField()
    f_ile=models.ImageField(upload_to="app1/static/")

class ordermodel(models.Model):
    i_tem=models.CharField(max_length=20)
    p_rice=models.IntegerField()
    q_uantity=models.IntegerField()
    answer=models.IntegerField(null=True)