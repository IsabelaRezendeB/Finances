# Generated by Django 4.1 on 2022-08-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('A', 'Alimentação'), ('S', 'Saúde'), ('M', 'Moradia'), ('T', 'Transporte'), ('E', 'Educação'), ('L', 'Lazer'), ('I', 'Imprevisto'), ('O', 'Outras')], default='O', max_length=1, null=True),
        ),
    ]