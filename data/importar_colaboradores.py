import os
import django

# Configuração do Django dentro do script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_help.settings")
django.setup()

import pandas as pd
from django.contrib.auth.models import User
from app_core.models import RelacaoColaborador, Escritorio  # Importa os modelos

# FILE_PATH = "colaboradores.xlsx"
FILE_PATH = "colaboradores_corrigido.xlsx"


def importar_colaboradores():
    df = pd.read_excel(FILE_PATH, engine="openpyxl" if FILE_PATH.endswith(".xlsx") else "odf")

    for _, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        email = row["email"]
        senha = row["senha"]
        contador_email = row["contador_email"]  # Associa ao email do contador

        # Verifica se o colaborador já existe pelo email
        if User.objects.filter(email=email).exists():
            print(f"⚠️ Colaborador {email} já existe. Pulando...")
            continue

        # Verifica se o escritório do contador existe
        try:
            escritorio = Escritorio.objects.get(contador__email=contador_email)
        except Escritorio.DoesNotExist:
            print(
                f"❌ Escritório relacionado ao contador {contador_email} não encontrado. Pulando colaborador {email}...")
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

        # Associa o colaborador ao escritório
        relacao, created = RelacaoColaborador.objects.get_or_create(
            escritorio=escritorio,
            colaborador=colaborador
        )
        if created:
            print(f"✅ Colaborador {email} associado ao escritório do contador {contador_email}.")
        else:
            print(f"⚠️ Colaborador {email} já está associado ao escritório do contador {contador_email}.")


if __name__ == "__main__":
    importar_colaboradores()
