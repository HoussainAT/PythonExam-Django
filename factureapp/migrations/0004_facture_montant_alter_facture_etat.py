# Generated by Django 4.2.16 on 2024-11-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factureapp', '0003_alter_facture_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='montant',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='facture',
            name='etat',
            field=models.CharField(choices=[('0', 'Non payé'), ('1', 'Payé')], max_length=1),
        ),
    ]
