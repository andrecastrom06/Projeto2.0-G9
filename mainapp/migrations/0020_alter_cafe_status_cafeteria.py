# Generated by Django 5.0.4 on 2024-04-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_rename_titulo_cafe_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='status_cafeteria',
            field=models.CharField(choices=[('NL', 'Quero ir'), ('EL', 'Fui')], default='NL', max_length=2),
        ),
    ]
