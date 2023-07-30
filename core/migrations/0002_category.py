# Generated by Django 4.2.3 on 2023-07-30 00:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.CharField(
                        default=core.models.gen_id,
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        verbose_name='id',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name='criado em',
                    ),
                ),
                (
                    'deleted_at',
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        null=True,
                        verbose_name='deletado em',
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name='atualizado em',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        db_index=True, max_length=100, verbose_name='nome'
                    ),
                ),
                (
                    'owner',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='owner',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='dono',
                    ),
                ),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
    ]