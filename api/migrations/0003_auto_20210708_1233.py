# Generated by Django 3.2 on 2021-07-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210706_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.asklawyer'),
        ),
    ]
