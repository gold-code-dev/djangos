# Utilização de Métodos HTTP em um Sistema de Tickets e Pagamentos

No desenvolvimento de um sistema de tickets e pagamentos, é importante usar os métodos HTTP corretos para cada operação,
mantendo a aplicação organizada e alinhada às boas práticas. Aqui está uma explicação completa.

---

## Métodos HTTP Principais

### **1. GET – Leitura de informações**

Usado para **obter informações sem modificar dados no servidor**.

**Exemplos no sistema:**

- Listar tickets abertos:
  ```
  GET /tickets/
  ```
- Exibir detalhes de um ticket:
  ```
  GET /tickets/123/
  ```
- Buscar detalhes de um pagamento:
  ```
  GET /pagamentos/456/
  ```

---

### **2. POST – Criação de dados**

Utilizado para **criar novos recursos ou executar ações que modificam dados no servidor**.

**Exemplos no sistema:**

- Criar um novo ticket:
  ```
  POST /tickets/
  Corpo (JSON):
  {
    "titulo": "Erro no sistema",
    "descricao": "Não consigo acessar a página inicial",
    "prioridade": "Alta"
  }
  ```
- Registrar um novo pagamento:
  ```
  POST /pagamentos/
  Corpo (JSON):
  {
    "ticket_id": 123,
    "valor": 500.00,
    "metodo_pagamento": "cartao"
  }
  ```

---

### **3. PUT – Atualização completa de um recurso**

Usado para **substituir todos os campos de um recurso existente**.

**Exemplos no sistema:**

- Atualizar todos os dados de um ticket:
  ```
  PUT /tickets/123/
  Corpo (JSON):
  {
    "titulo": "Novo título do ticket",
    "descricao": "Descrição atualizada",
    "prioridade": "Baixa",
    "status": "Resolvido"
  }
  ```
- Atualizar o registro de pagamento:
  ```
  PUT /pagamentos/456/
  Corpo (JSON):
  {
    "ticket_id": 123,
    "valor": 600.00,
    "metodo_pagamento": "pix",
    "status_pagamento": "Confirmado"
  }
  ```

---

### **4. PATCH – Atualização parcial de um recurso**

Utilizado para **atualizar apenas campos específicos**.

**Exemplos no sistema:**

- Atualizar apenas o status de um ticket:
  ```
  PATCH /tickets/123/
  Corpo (JSON):
  {
    "status": "Resolvido"
  }
  ```
- Atualizar apenas o status de um pagamento:
  ```
  PATCH /pagamentos/456/
  Corpo (JSON):
  {
    "status_pagamento": "Cancelado"
  }
  ```

---

### **5. DELETE – Remoção de dados**

Usado para **remover um recurso do servidor**.

**Exemplos no sistema:**

- Deletar um ticket:
  ```
  DELETE /tickets/123/
  ```
- Deletar um registro de pagamento:
  ```
  DELETE /pagamentos/456/
  ```

**⚠️ Cuidado:** Em vez de excluir permanentemente, no caso de tickets e pagamentos, prefira marcar como "cancelado" ou "
inativo".

---

### **6. HEAD – Obtenção apenas de cabeçalhos**

Semelhante ao GET, mas sem retornar o corpo (útil para verificar a existência de recursos).

**Exemplo no sistema:**

- Verificar se um ticket existe:
  ```
  HEAD /tickets/123/
  ```
- Verificar se um pagamento existe:
  ```
  HEAD /pagamentos/456/
  ```

---

### **7. OPTIONS – Consultar métodos suportados**

Responde com os métodos permitidos pelo servidor para a URL requisitada.

**Exemplo no sistema:**

- Descobrir métodos permitidos para tickets:
  ```
  OPTIONS /tickets/123/
  ```

**Resposta típica:**

  ```
  Allow: GET, POST, PUT, DELETE
  ```

---

## Outros Métodos HTTP

- **CONNECT** → Usado para estabelecer túneis. Raramente usado em sistemas normais.
- **TRACE** → Retorna uma cópia da requisição enviada. Pouco utilizado.

---

## Boas Práticas

1. **Mantenha URLs amigáveis e organizadas:**
    - `/tickets/` → Para listar/criar tickets.
    - `/tickets/<id>/` → Operações específicas em um ticket.
    - `/pagamentos/` → Para criar ou listar pagamentos.
    - `/pagamentos/<id>/` → Operações específicas em pagamentos.

2. **Autenticação e autorização:**
    - Use autenticação para proteger rotas sensíveis (ex.: pagamentos ou tickets privados).
    - Tokens ou sessões podem ser usados para identificar usuários autorizados.

3. **Validação de dados:**
    - Verifique sempre os dados recebidos em **POST**, **PUT** ou **PATCH** para garantir consistência e evitar
      problemas no banco de dados.

4. **Códigos de resposta HTTP consistentes:**
    - **200 OK** → Sucesso.
    - **201 Created** → Recurso criado com sucesso.
    - **400 Bad Request** → Dados inválidos na requisição.
    - **401 Unauthorized** → Autenticação necessária.
    - **404 Not Found** → Recurso inexistente.
    - **500 Internal Server Error** → Erro do servidor.

5. **Evite deletar dados sensíveis:**
    - Para tickets ou pagamentos, use uma flag como "cancelado" em vez de excluir permanentemente.

---

## Resumo dos Métodos HTTP no Sistema

| Método      | Uso                                                                               |
|-------------|-----------------------------------------------------------------------------------|
| **GET**     | Consultar ou listar dados (ex.: listar/exibir tickets ou pagamentos).             |
| **POST**    | Criar novos recursos (ex.: criar ticket ou registrar pagamento).                  |
| **PUT**     | Atualizar completamente um recurso (ex.: substituir todos os dados de um ticket). |
| **PATCH**   | Atualizar parcialmente um recurso (ex.: alterar status de um ticket).             |
| **DELETE**  | Deletar recurso (ex.: remover ticket ou pagamento).                               |
| **HEAD**    | Verificar existência de recurso, sem transferir corpo da resposta.                |
| **OPTIONS** | Descobrir métodos HTTP permitidos para uma URL específica.                        |

---

Com essas orientações, você terá um sistema de **tickets e pagamentos bem estruturado** e alinhado com os padrões
RESTful. Escolha o método correto de acordo com cada operação do seu sistema.
