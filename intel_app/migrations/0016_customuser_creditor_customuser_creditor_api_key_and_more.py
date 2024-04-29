# Generated by Django 4.2.4 on 2024-04-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0015_announcement_afaregistration_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='creditor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='creditor_api_key',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='creditor_user_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mtntransaction',
            name='transaction_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='topuprequest',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
