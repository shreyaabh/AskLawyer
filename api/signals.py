from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

@receiver(pre_save, sender=User)
def user_on_active(sender, instance, created, **kwargs):
    if not created:
        oldUserObj = User.object.get(pk=instance.pk)
        userObj = instance
        if oldUserObj.active:
            if userObj.active:
                Points.objects.create(point=somepointfromPointsTableForQuestionAsked)

@receiver(pre_save, sender=question)
def question_on_approve(sender, instance, **kwargs):
    if instance.pk is not None:
        oldQuestionObj = question.object.get(pk=instance.pk)
        questionObj = instance
        if oldQuestionObj.status != 1 and questionObj.status == 1:
            Points.objects.create(point=somepointfromPointsTableForQuestionAsked)

@receiver(pre_save, sender=question)
def answer_on_approve(sender, instance, **kwargs):
    if instance.pk is not None:
        oldAnswerObj = answer.object.get(pk=instance.pk)
        answerObj = instance
        if oldAnswerObj.status != 1 and answerObj.status == 1:
            Points.objects.create(point=somepointfromPointsTableForQuestionAsked)


    
