# Generated by Django 3.0.4 on 2020-04-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0012_auto_20200418_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofilemodel',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myprofilemodel',
            name='listofcreators',
            field=models.CharField(blank=True, default='a', max_length=300, null=True),
        ),
    ]
