# Generated by Django 4.2.4 on 2025-03-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0003_alter_bigtimetransaction_reference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='paystack_active',
            field=models.BooleanField(default=False),
        ),
    ]
