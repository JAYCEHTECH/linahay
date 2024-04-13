# Generated by Django 5.0 on 2024-01-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0014_admininfo_afa_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='afaregistration',
            name='region',
            field=models.CharField(blank=True, choices=[('Greater Accra', 'Greater Accra'), ('Ashanti', 'Ashanti'), ('Western', 'Western'), ('Central', 'Central'), ('Eastern', 'Eastern'), ('Volta', 'Volta'), ('Northern', 'Northern'), ('Upper East', 'Upper East'), ('Upper West', 'Upper West'), ('Bono', 'Bono'), ('Bono East', 'Bono East'), ('Ahafo', 'Ahafo'), ('Savannah', 'Savannah'), ('North East', 'North East'), ('Western North', 'Western North'), ('Oti', 'Oti')], max_length=250, null=True),
        ),
    ]