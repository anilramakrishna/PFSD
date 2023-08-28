# Generated by Django 4.1.1 on 2022-11-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0010_rename_submit_submit_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit_order',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Failed', 'Failed')], default='Pending', max_length=100, null=True),
        ),
    ]