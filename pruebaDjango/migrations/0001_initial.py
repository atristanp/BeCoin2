# Generated by Django 3.0.5 on 2021-04-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('group_id', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('permission_id', models.TextField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('codename', models.TextField()),
                ('content_type_id', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('date_joined', models.DateTimeField()),
                ('email', models.TextField()),
                ('first_name', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('is_active', models.TextField()),
                ('is_staff', models.TextField()),
                ('is_superuser', models.TextField()),
                ('last_login', models.DateTimeField()),
                ('last_name', models.TextField()),
                ('password', models.TextField()),
                ('username', models.TextField(unique=True)),
                ('cartera', models.BigIntegerField()),
                ('binancecoin', models.BigIntegerField()),
                ('bitcoin', models.BigIntegerField()),
                ('ethereum', models.BigIntegerField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('group_id', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('user_id', models.TextField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('permission_id', models.TextField()),
                ('user_id', models.TextField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datos_Cripto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('simbolo', models.TextField()),
                ('nombre', models.TextField()),
                ('precio', models.IntegerField()),
                ('cambio', models.TextField()),
                ('cambio_porcentaje', models.TextField()),
                ('hora', models.TextField()),
            ],
            options={
                'db_table': 'datos_cripto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('action_flag', models.TextField()),
                ('action_time', models.DateTimeField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('object_id', models.TextField()),
                ('object_repr', models.TextField()),
                ('user_id', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('app_label', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('model', models.TextField()),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('app', models.TextField()),
                ('applied', models.DateTimeField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('expire_date', models.DateTimeField()),
                ('session_data', models.TextField()),
                ('session_key', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('articulo', models.TextField()),
                ('myhoras', models.TextField()),
            ],
            options={
                'db_table': 'noticias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('fecha', models.TextField()),
                ('usuario', models.TextField()),
                ('nombre', models.TextField()),
                ('imagen_perfil', models.TextField()),
            ],
            options={
                'db_table': 'tweets',
                'managed': False,
            },
        ),
    ]
