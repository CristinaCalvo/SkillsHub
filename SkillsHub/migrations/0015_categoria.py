# Generated by Django 5.0.4 on 2024-06-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillsHub', '0014_remove_usuarioinsignia_activa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
