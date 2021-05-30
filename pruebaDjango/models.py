# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.TextField()  # This field type is a guess.
    id = models.TextField(primary_key=True)  # This field type is a guess.
    permission_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    codename = models.TextField()
    content_type_id = models.TextField()  # This field type is a guess.
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    date_joined = models.DateTimeField()
    email = models.TextField()
    first_name = models.TextField()
    id = models.BigIntegerField(primary_key=True)  # This field type is a guess.
    is_active = models.TextField()  # This field type is a guess.
    is_staff = models.TextField()  # This field type is a guess.
    is_superuser = models.TextField()  # This field type is a guess.
    last_login = models.DateTimeField()
    last_name = models.TextField()
    password = models.TextField()
    username = models.TextField(unique=True)

    cartera = models.FloatField()
    binancecoin = models.FloatField()
    bitcoin = models.FloatField()
    ethereum = models.FloatField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    group_id = models.TextField()  # This field type is a guess.
    id = models.TextField(primary_key=True)  # This field type is a guess.
    user_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    permission_id = models.TextField()  # This field type is a guess.
    user_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_flag = models.TextField()  # This field type is a guess.
    action_time = models.DateTimeField()
    change_message = models.TextField()
    content_type_id = models.TextField()  # This field type is a guess.
    id = models.TextField(primary_key=True)  # This field type is a guess.
    object_id = models.TextField()
    object_repr = models.TextField()
    user_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.TextField()
    id = models.TextField(primary_key=True)  # This field type is a guess.
    model = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.TextField()
    applied = models.DateTimeField()
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    expire_date = models.DateTimeField()
    session_data = models.TextField()
    session_key = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'django_session'


class Tweet(models.Model):

    #id = models.IntegerField(primary_key=True)
    _id = models.TextField(primary_key=True)
    texto = models.TextField()
    fecha = models.TextField()
    usuario = models.TextField()
    nombre = models.TextField()
    imagen_perfil = models.TextField()

    class Meta:
        managed = False
        db_table = 'tweets'


class Noticias(models.Model):

    #id = models.IntegerField(primary_key=True)
    _id = models.TextField(primary_key=True)
    titulo = models.TextField()
    articulo = models.TextField()
    myhoras = models.TextField()

    class Meta:
        managed = False
        db_table = 'noticias'


class Datos_Cripto(models.Model):
    _id = models.IntegerField(primary_key=True)
    simbolo = models.TextField()
    nombre = models.TextField()
    precio = models.IntegerField()
    cambio = models.TextField()
    cambio_porcentaje = models.TextField()

    hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'datos_cripto'


class Datos_Transacciones(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.TextField()
    criptomoneda = models.TextField()
    cantidad = models.FloatField()
    precio = models.FloatField()
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'transacciones'
