# Generated by Django 4.2.5 on 2023-09-28 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FilaEspera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_chegada', models.DateTimeField(auto_now_add=True)),
                ('prioridade', models.BooleanField(default=False)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.paciente')),
            ],
        ),
    ]
