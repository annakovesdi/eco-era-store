# Generated by Django 3.2.4 on 2021-08-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_addition'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_payment_id',
            field=models.CharField(default='', max_length=300),
        ),
    ]
