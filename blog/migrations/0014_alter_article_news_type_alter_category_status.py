# Generated by Django 4.1.1 on 2022-10-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0013_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='news_type',
            field=models.BooleanField(blank=True, choices=[(False, 'خبر معمولی'), (True, 'خبر ویژه')], default=False,
                                      help_text='<div id="id_short_description_helptext" class="help">اگر خبر شما جزو اخبار مهم و فوری می باشد می توانید آن را در دسته<strong style="margin:5px">ویژه</strong>قرار دهید.</div>',
                                      null=True, verbose_name='نوع خبر'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(choices=[(False, 'غیرفعال'), (True, 'فعال')], default=True, verbose_name='وضعیت'),
        ),
    ]
