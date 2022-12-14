# Generated by Django 3.2.6 on 2022-10-24 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название товара', max_length=100, verbose_name='Название товара')),
                ('price', models.PositiveIntegerField(help_text='Введите цену товара', verbose_name='Цена товара')),
                ('description', models.CharField(blank=True, help_text='Введите описание товара', max_length=500, null=True, verbose_name='Описание товара')),
                ('image', models.ImageField(blank=True, help_text='Загрузите фото', null=True, upload_to='images/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Введите время создания объявления', verbose_name='Время создания объявления')),
                ('author', models.ForeignKey(help_text='Выберите автора объявления', on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Комментарий', max_length=500, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Введите время создания комментария', verbose_name='Время создания комментария')),
                ('ad', models.ForeignKey(help_text='Комментарий к объявлению', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='Объявление')),
                ('author', models.ForeignKey(help_text='Выберите автора комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-created_at',),
            },
        ),
    ]
