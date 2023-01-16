# Generated by Django 4.1.1 on 2022-10-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0018_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(choices=[(False, 'غیرفعال'), (True, 'فعال')], default=True, verbose_name='وضعیت'),
        ),
    ]
