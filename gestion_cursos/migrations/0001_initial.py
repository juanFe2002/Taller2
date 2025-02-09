# Generated by Django 3.2.16 on 2025-02-09 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del curso*')),
            ],
            options={
                'permissions': (('crear_curso', 'Puede Crear Curso'), ('listar_cursos', 'Puede Consultar Cursos'), ('actualizar_curso', 'Puede Actualizar Curso'), ('eliminar_curso', 'Puede Eliminar Curso')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50, unique=True, verbose_name='Materia*')),
                ('maestro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Maestro asignado*')),
                ('nombre_curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion_cursos.cursos', verbose_name='Curso*')),
            ],
            options={
                'permissions': (('crear_materia', 'Puede Crear Materia'), ('listar_materias', 'Puede Consultar Materias'), ('actualizar_materia', 'Puede Actualizar Materia'), ('eliminar_materia', 'Puede Eliminar Materia'), ('detalle_materia', 'Puede Ver Detalle Materia')),
                'default_permissions': (),
            },
        ),
    ]
