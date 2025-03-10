import os
import django

# Configurar o Django dentro do script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tickets_project.settings")
django.setup()

import pandas as pd
from accounts_app.models import Usuario

FILE_PATH = "contadores.xlsx"

def importar_contadores():
    df = pd.read_excel(FILE_PATH, engine="openpyxl" if FILE_PATH.endswith(".xlsx") else "odf")

    for _, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        email = row["email"]
        senha = row["senha"]

        if Usuario.objects.filter(email=email).exists():
            print(f"⚠️ Contador {email} já existe. Pulando...")
            continue

        contador = Usuario.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            tipo_usuario="contador",
            is_active=True,
            is_staff=False,
        )
        contador.set_password(senha)
        contador.save()

        print(f"✅ Contador {email} cadastrado com sucesso!")

if __name__ == "__main__":
    importar_contadores()
