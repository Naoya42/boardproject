# Generated by Django 3.0.4 on 2020-04-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_boardmodel_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='comment',
            field=models.CharField(blank=True, default='コメントしてね', max_length=200, null=True),
        ),
    ]