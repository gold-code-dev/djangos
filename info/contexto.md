# Como compartilhar dados entre views no Django

## 1. Usar Session (Sessão)

Armazena dados entre requests na sessão do usuário.

**View 1 - Salvando dado na sessão:**

```python
def minha_view(request):
    dado = "Esse é o dado compartilhado"
    request.session['meu_dado'] = dado  # Armazena o dado na sessão
    return HttpResponse("Dado armazenado na sessão!")
```

**View 2 - Recuperando o dado da sessão:**

```python
def outra_view(request):
    dado = request.session.get('meu_dado', 'Dado não encontrado')
    return HttpResponse(f"O dado compartilhado é: {dado}")
```

---

## 2. Repassar Dados via Query Parameters (GET)

Passa dados pela URL (recomendado somente para dados simples e não-sensíveis).

**View 1 - Redireciona com parâmetro na URL:**

```python
from django.shortcuts import redirect


def minha_view(request):
    dado = "meu_dado"
    return redirect(f"/outra-rota/?dado={dado}")  # Adiciona o dado na URL
```

**View 2 - Recupera o parâmetro da URL:**

```python
def outra_view(request):
    dado = request.GET.get('dado', 'Dado não encontrado')
    return HttpResponse(f"Dado recebido: {dado}")
```

---

## 3. Repassar Dados via POST/Formulário

Repasse de dados entre rotas via formulário ou requisição POST.

**View 1 - Envia o dado com formulário:**

```python
from django.shortcuts import render


def minha_view(request):
    dado = "meu_dado"
    return render(request, 'formulario.html', {'dado': dado})
```

**Template de formulário (`formulario.html`)**:

```html

<form action="/outra-rota/" method="post">
    {% csrf_token %}
    <input type="hidden" name="dado" value="{{ dado }}">
    <button type="submit">Enviar dado para outra rota</button>
</form>
```

**View 2 - Recupera o dado via POST:**

```python
def outra_view(request):
    if request.method == 'POST':
        dado = request.POST.get('dado', 'Dado não encontrado')
        return HttpResponse(f"Dado compartilhado: {dado}")
    return HttpResponse("Método inválido")
```

---

## 4. Reaproveitar Dados com Context Processor

Usado para compartilhar dados globais entre múltiplas views/templates.

**Cria um Context Processor (`context_processors.py`):**

```python
def meu_contexto_compartilhado(request):
    return {
        'meu_dado_global': "Esse dado está disponível em todos os templates"
    }
```

**Adiciona o Context Processor no `settings.py`:**

```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # Outros context processors padrão
                'meu_app.context_processors.meu_contexto_compartilhado',
            ],
        },
    },
]
```

**Template - Acessa o dado diretamente:**

```html
<p>{{ meu_dado_global }}</p>
```

---

## 5. Armazenar Dados Temporários no Cache

Armazena dados temporários no cache do Django.

**View 1 - Armazena no cache:**

```python
from django.core.cache import cache


def minha_view(request):
    cache.set('meu_dado', 'Esse é um dado enviado', timeout=60)  # Salva por 60 segundos
    return HttpResponse("Dado armazenado no cache!")
```

**View 2 - Recupera o dado do cache:**

```python
def outra_view(request):
    dado = cache.get('meu_dado', 'Dado não encontrado')
    return HttpResponse(f"Dado do cache: {dado}")
```

---

## Resumo: Quando usar cada método?

| Método                     | Quando usar?                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------|
| **Session (Sessão)**       | Quando o dado precisa ser mantido entre requests para o mesmo usuário.                           |
| **Query Parameters (GET)** | Quando o dado não é sensível e pode ser passado pela URL.                                        |
| **POST/Formulário**        | Sempre que for enviar dados de formulários, recomenda-se o uso de requisições POST.              |
| **Context Processor**      | Quando o dado é necessário em várias views/templates e não depende de uma requisição específica. |
| **Cache**                  | Quando dados temporários (não sensíveis) devem ser compartilhados entre requests ou usuários.    |
