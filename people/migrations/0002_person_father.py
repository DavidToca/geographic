# Generated by Django 2.0.1 on 2018-01-11 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='father',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]
