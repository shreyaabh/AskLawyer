# Generated by Django 3.2 on 2021-07-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('biography', models.TextField()),
                ('award', models.TextField()),
                ('practice_area', models.CharField(max_length=30)),
                ('experience', models.FloatField(blank=True)),
                ('legal_fees', models.IntegerField(blank=True, default=15)),
                ('publication', models.TextField()),
                ('website', models.URLField()),
                ('status', models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected')], max_length=20)),
                ('professional_associations', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='wakil/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
