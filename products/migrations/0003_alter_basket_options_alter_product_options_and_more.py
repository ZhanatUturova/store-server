# Generated by Django 4.2.1 on 2023-06-03 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'корзина', 'verbose_name_plural': 'корзины'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категория(ю) продукта', 'verbose_name_plural': 'категории продуктов'},
        ),
    ]
