# Generated by Django 5.0.3 on 2024-03-11 03:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_rename_habilidades_habilidadesmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleadosmodel',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.RenameField(
            model_name='empleadosmodel',
            old_name='Habilidades',
            new_name='habilidades',
        ),
        migrations.AddField(
            model_name='empleadosmodel',
            name='content_cv',
            field=ckeditor.fields.RichTextField(default='Texto vacio'),
            preserve_default=False,
        ),
    ]