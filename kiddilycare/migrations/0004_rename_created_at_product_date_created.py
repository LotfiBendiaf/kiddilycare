# Generated by Django 4.0.2 on 2022-03-18 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kiddilycare', '0003_product_created_at_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='date_created',
        ),
    ]
