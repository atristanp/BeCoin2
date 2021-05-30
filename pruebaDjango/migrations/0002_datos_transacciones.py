# Generated by Django 2.2.7 on 2021-05-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Transacciones',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.TextField()),
                ('criptomoneda', models.TextField()),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
                ('tipo', models.TextField()),
            ],
            options={
                'db_table': 'transacciones',
                'managed': False,
            },
        ),
    ]