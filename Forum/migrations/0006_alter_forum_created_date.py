# Generated by Django 3.2 on 2021-07-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_forum_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
