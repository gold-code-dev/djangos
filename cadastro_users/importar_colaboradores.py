import os
import django

# Configurar o Django dentro do script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tickets_project.settings")
django.setup()

import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from accounts_app.models import Usuario

FILE_PATH = "colaboradores.xlsx"

def importar_colaboradores():
    df = pd.read_excel(FILE_PATH, engine="openpyxl" if FILE_PATH.endswith(".xlsx") else "odf")

    for _, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        email = row["email"]
        senha = row["senha"]
        contador_email = row["contador_email"].strip()

        if Usuario.objects.filter(email=email).exists():
            print(f"⚠️ Colaborador {email} já existe. Pulando...")
            continue

        try:
            contador = Usuario.objects.get(email=contador_email, tipo_usuario="contador")
        except ObjectDoesNotExist:
            print(f"❌ ERRO: Contador {contador_email} não encontrado para {email}. Pulando...")
            continue

        colaborador = Usuario.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            tipo_usuario="colaborador",
            contador=contador,
            is_active=True,
            is_staff=False,
        )
        colaborador.set_password(senha)
        colaborador.save()

        print(f"✅ Colaborador {email} cadastrado com sucesso, vinculado ao contador {contador_email}!")

if __name__ == "__main__":
    importar_colaboradores()
