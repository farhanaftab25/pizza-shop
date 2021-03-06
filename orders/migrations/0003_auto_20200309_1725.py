# Generated by Django 3.0.3 on 2020-03-09 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20200227_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Item'},
        ),
        migrations.AlterModelOptions(
            name='itemprice',
            options={'verbose_name_plural': 'ItemPrice'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': 'Size'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Topping'},
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
    ]
