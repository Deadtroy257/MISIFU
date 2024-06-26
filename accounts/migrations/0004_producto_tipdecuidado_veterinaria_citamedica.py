# Generated by Django 5.0.6 on 2024-06-06 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_customuser_nombre_completo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("imagen", models.ImageField(upload_to="productos/")),
            ],
        ),
        migrations.CreateModel(
            name="TipDeCuidado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("contenido", models.TextField()),
                ("imagen", models.ImageField(upload_to="tips/")),
            ],
        ),
        migrations.CreateModel(
            name="Veterinaria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("direccion", models.CharField(max_length=255)),
                ("imagen", models.ImageField(upload_to="veterinarias/")),
            ],
        ),
        migrations.CreateModel(
            name="CitaMedica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                (
                    "veterinaria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.veterinaria",
                    ),
                ),
            ],
        ),
    ]
