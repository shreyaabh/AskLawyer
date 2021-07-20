from django.db import models


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

class askLawyer(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10,blank=True)
    address=models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.first_name+' '+self.last_name

    def no_rating(self):
        ratings=Points.objects.filter(user=self)
        return len(ratings)

    def total_points(self):
        sum=0
        stars=Points.objects.filter(user=self)
        for point in stars:
            sum+=point.stars
        return sum


class answer(models.Model):
    # CHOICES=[
    #     ('Edit','Edit'),
    #     ('View','View'),
    #     ('Delete','Delete'),
    # ]
    s_no=models.AutoField(primary_key=True)
    user = models.ForeignKey(askLawyer, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer=models.TextField(blank=False)
    # options=models.CharField(max_length=20, choices=CHOICES)
    correct = models.BooleanField('Correct', default=False)

    def __str__(self):
        return self.answer



class Points(models.Model):
    user = models.ForeignKey(askLawyer, on_delete=models.CASCADE)
    answer = models.ForeignKey(answer, on_delete=models.CASCADE)
    stars= models.IntegerField(default=15, blank=True)

    def __str__(self):
        return str(self.user)+'  '+str(self.stars)