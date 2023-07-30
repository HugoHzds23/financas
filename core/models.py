from uuid import uuid1

from django.contrib.auth.models import AbstractUser
from django.db import models


def gen_id() -> str:
    return uuid1().hex


class User(AbstractUser):
    id = models.CharField(
        'id', max_length=40, primary_key=True, default=gen_id
    )

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        db_table = 'core_users'


class BaseModel(models.Model):
    id = models.CharField(
        'id', max_length=40, primary_key=True, default=gen_id, editable=False
    )
    created_at = models.DateTimeField(
        'criado em', auto_now_add=True, db_index=True
    )
    deleted_at = models.DateTimeField(
        'deletado em', null=True, blank=True, db_index=True, editable=False
    )   # TODO: Implement logical exclusion
    updated_at = models.DateTimeField(
        'atualizado em', auto_now=True, db_index=True
    )

    class Meta:
        abstract = True
        db_table = 'core_%(class)ss'


class Category(BaseModel):
    owner = models.ForeignKey(
        'core.User',
        related_name='owner',
        verbose_name='dono',
        on_delete=models.PROTECT,
        editable=False,
    )
    name = models.CharField('nome', max_length=100, db_index=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
