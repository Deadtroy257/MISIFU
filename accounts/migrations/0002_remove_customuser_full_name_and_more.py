# Generated by Django 5.0.6 on 2024-06-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre_completo',
            field=models.CharField(default='Nombre Completo Temporal', max_length=255),
        ),
    ]