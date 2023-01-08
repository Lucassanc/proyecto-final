# Generated by Django 4.1.4 on 2023-01-08 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_final', '0003_post_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=1000)),
                ('enviado_el', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado_el',
            field=models.DateField(auto_now_add=True),
        ),
    ]
