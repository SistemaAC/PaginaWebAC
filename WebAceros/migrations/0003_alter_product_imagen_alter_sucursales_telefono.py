# Generated by Django 5.2.2 on 2025-06-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAceros', '0002_alter_categoria_status_alter_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(upload_to='productos/'),
        ),
        migrations.AlterField(
            model_name='sucursales',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
