# Generated by Django 5.1.2 on 2025-02-02 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttag',
            old_name='name',
            new_name='tag_name',
        ),
    ]
