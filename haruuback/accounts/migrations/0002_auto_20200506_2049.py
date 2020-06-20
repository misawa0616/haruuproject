# Generated by Django 2.2.12 on 2020-05-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='token',
            field=models.CharField(default='b3c0278946934e5ab68cf2889489f7cc', max_length=32),
        ),
        migrations.AlterField(
            model_name='customtoken',
            name='key',
            field=models.CharField(default='ee042c8da1f5489ca23dc0c458efb4cd', max_length=32),
        ),
        migrations.AlterField(
            model_name='emailconfirm',
            name='token',
            field=models.CharField(default='42a89021a0014bebaa5ae2ea356476a5', max_length=32),
        ),
        migrations.AlterField(
            model_name='haruuuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
