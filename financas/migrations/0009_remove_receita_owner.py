# Generated by Django 4.1 on 2022-08-15 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0008_alter_receita_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='owner',
        ),
    ]