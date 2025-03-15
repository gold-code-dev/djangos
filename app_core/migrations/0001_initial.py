# Generated by Django 4.2.20 on 2025-03-14 22:13

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
            name='Escritorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.OneToOneField(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='escritorio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('abertura', 'Abertura'), ('alteracao', 'Alteração'), ('transformacao', 'Transformação'), ('baixa', 'Baixa')], max_length=20)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('prazo', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('numero_escritorio', models.PositiveIntegerField()),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('escritorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='app_core.escritorio')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('concluido', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('prazo', models.DateTimeField(blank=True, null=True)),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas_criadas', to=settings.AUTH_USER_MODEL)),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarefas_responsaveis', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='app_core.ticket')),
            ],
            options={
                'verbose_name_plural': 'Tarefas',
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='RelacaoColaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='colaboracao', to=settings.AUTH_USER_MODEL)),
                ('escritorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colaboradores', to='app_core.escritorio')),
            ],
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='anexos/')),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='app_core.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TarefaAnexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('anexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='app_core.anexo')),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='app_core.tarefa')),
            ],
            options={
                'unique_together': {('tarefa', 'anexo')},
            },
        ),
    ]
