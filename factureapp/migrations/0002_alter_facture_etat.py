# Generated by Django 4.2.16 on 2024-11-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factureapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='etat',
            field=models.CharField(choices=[(0, 'Non payé'), (1, 'Payé')], max_length=1),
        ),
    ]
