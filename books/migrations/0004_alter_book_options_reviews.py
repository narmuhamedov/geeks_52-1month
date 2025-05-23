# Generated by Django 5.2 on 2025-05-08 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_page_size_book_page_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'книгу', 'verbose_name_plural': 'книги'},
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='как вас зовут?')),
                ('text', models.TextField(verbose_name='как вам книга?')),
                ('books_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.book')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]
