# Generated by Django 4.2.4 on 2023-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickleball', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='deadline_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]