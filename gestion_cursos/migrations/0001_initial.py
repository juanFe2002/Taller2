# Generated by Django 3.2.16 on 2025-02-10 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del curso*')),
            ],
            options={
                'permissions': (('registrar_curso', 'Puede Crear Curso'), ('listar_cursos', 'Puede Consultar Cursos'), ('actualizar_curso', 'Puede Actualizar Curso'), ('eliminar_curso', 'Puede Eliminar Curso')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50, unique=True, verbose_name='Materia*')),
            ],
            options={
                'permissions': (('registrar_materia', 'Puede Crear Materia'), ('listar_materias', 'Puede Consultar Materias'), ('actualizar_materia', 'Puede Actualizar Materia'), ('eliminar_materia', 'Puede Eliminar Materia'), ('detalle_materia', 'Puede Ver Detalle Materia')),
                'default_permissions': (),
            },
        ),
    ]
