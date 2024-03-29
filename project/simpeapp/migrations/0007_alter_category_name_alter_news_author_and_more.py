# Generated by Django 4.2.7 on 2024-02-23 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpeapp', '0006_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='category name', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simpeapp.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simpeapp.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, verbose_name='CategoryType'),
        ),
        migrations.AlterField(
            model_name='news',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='dateCreation'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
