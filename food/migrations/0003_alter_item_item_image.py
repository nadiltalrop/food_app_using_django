# Generated by Django 4.2.3 on 2023-07-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.URLField(default='https://us.123rf.com/450wm/jovanas/jovanas1802/jovanas180200399/95580559-cutlery-icons-vector-illustration.jpg?ver=6'),
        ),
    ]
