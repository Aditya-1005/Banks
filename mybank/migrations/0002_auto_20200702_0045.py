# Generated by Django 3.0.6 on 2020-07-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='Bank_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='mybank.Banks'),
        ),
    ]
