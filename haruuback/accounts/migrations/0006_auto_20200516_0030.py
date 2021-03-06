# Generated by Django 2.2.12 on 2020-05-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200506_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='token',
            field=models.CharField(default='e16ca8c678904f48a48c3367129890d1', max_length=32),
        ),
        migrations.AlterField(
            model_name='customtoken',
            name='key',
            field=models.CharField(default='d728c0f61cae41de9ac9b017287fda68', max_length=32),
        ),
        migrations.AlterField(
            model_name='emailconfirm',
            name='token',
            field=models.CharField(default='68af3ace30104efb86de80345c3efde0', max_length=32),
        ),
        migrations.AlterField(
            model_name='haruuuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
