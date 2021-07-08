from django.db import models

'''question ko euta model
question ma ni user(kolle post gareko)
answer ko euta model (question lai foreign key rakhera)
answer ma ni user (who answered)
points chai pachi milaunu parcha'''

# Create your models here.
class askUser(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10,blank=True)
    address=models.CharField(max_length=50,blank=True)
    
    
    def __str__(self):
        return self.email

class question(models.Model):
    CHOICES=[
        ('Edit','Edit'),
        ('View','View'),
        ('Delete','Delete'),
    ]
    s_no=models.AutoField(primary_key=True)
    user = models.ForeignKey(askUser, on_delete=models.CASCADE)
    question=models.TextField(blank=False)
    options=models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.question
#For the answer part
class askLawyer(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10,blank=True)
    address=models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.email

class answer(models.Model):
    CHOICES=[
        ('Edit','Edit'),
        ('View','View'),
        ('Delete','Delete'),
    ]
    s_no=models.AutoField(primary_key=True)
    user = models.ForeignKey(askLawyer, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer=models.TextField(blank=False)
    options=models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.answer



    

