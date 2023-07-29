from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from uuid import uuid1


def gen_id() -> str:    
    return uuid1().hex


class User(AbstractUser):
    id = models.CharField('id', max_length=40, primary_key=True, default=gen_id)
    
    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        db_table = 'core_users'


class BaseModel(models.Model):
    id = models.CharField('id', max_length=40, primary_key=True, default=gen_id)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    deleted_at = models.DateTimeField('deletado em', null=True, blank=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)
    
    class Meta:
        abstract = True
        db_table = 'core_%(class)ss'