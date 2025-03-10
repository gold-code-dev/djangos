import os
import django

# Configuração do Django dentro do script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_help.settings")
django.setup()

import pandas as pd
from django.contrib.auth.models import User

FILE_PATH = "colaboradores.xlsx"


def importar_colaboradores():
    df = pd.read_excel(FILE_PATH, engine="openpyxl" if FILE_PATH.endswith(".xlsx") else "odf")

    for _, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        email = row["email"]
        senha = row["senha"]

        # Verifica se o usuário já existe pelo email
        if User.objects.filter(email=email).exists():
            print(f"⚠️ Colaborador {email} já existe. Pulando...")
            continue

        # Criação do usuário padrão do Django
        colaborador = User.objects.create_user(
            username=email,  # usamos o email como username
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=senha,
            is_staff=False,  # Não é staff
            is_superuser=False,  # Não é superusuário
        )
        print(f"✅ Colaborador {email} cadastrado com sucesso!")


if __name__ == "__main__":
    importar_colaboradores()
