# Generated by Django 5.0.4 on 2024-04-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Новая цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Старая цена')),
                ('image', models.FileField(blank=True, upload_to='items/', verbose_name='Изображение')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступно')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-price'],
            },
        ),
    ]
