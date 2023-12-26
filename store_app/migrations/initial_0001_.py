''' Generated by Django 4.2.7 on 2023-11-02 08:52'''

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''миграция'''

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID')),
                (
                    'name',
                    models.CharField(
                        max_length=30,
                        unique=True)),
                (
                    'slug',
                    models.SlugField(
                        max_length=15,
                        unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')
                 ),
                ('name', models.CharField(
                    max_length=30,
                    unique=True)
                 ),
                ('slug', models.SlugField(
                    max_length=15,
                    unique=True)
                 ),
                ('category', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='store_app.category')
                 ),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID')
                ),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=15, unique=True)),
                ('price', models.IntegerField()),
                ('subcategory', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='store_app.subcategory')
                 ),
            ],
        ),
    ]