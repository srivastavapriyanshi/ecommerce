# Generated by Django 4.2.7 on 2023-12-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(db_index=True, default=1),
        ),
    ]