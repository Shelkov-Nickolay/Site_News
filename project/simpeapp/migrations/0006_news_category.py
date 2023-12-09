# Generated by Django 4.2.7 on 2023-12-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpeapp', '0005_rename_sabscription_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simpeapp.category'),
            preserve_default=False,
        ),
    ]
