euntrie numa janela anonima para acessar meu localhost e sabe eu tava logado na outra 
janela. e a demais navegadores sejam crhome ou firefox anonimos ou nao se eu to logado todos compartilham o 
mesmo user. e mesmo estado de login. se eu desconecto todos sao descontados. 

to no django 4.2 isso preciso melhor algo no futuro neh ainda to em dev.


Isso acontece porque o Django usa **cookies de sessão** para armazenar o estado do login. Como o servidor Django armazena o ID da sessão no cookie do navegador, todas as janelas (mesmo anônimas) compartilham a mesma sessão **se estiverem no mesmo navegador**.

### No futuro (produção), melhore isso:
1. **Troque o backend de sessão**  
   No `settings.py`, mude `SESSION_ENGINE` para usar **cache ou banco de dados**, como Redis ou PostgreSQL. Exemplo com Redis:

   ```python
   SESSION_ENGINE = "django.contrib.sessions.backends.cache"
   SESSION_CACHE_ALIAS = "default"
   ```

2. **Use `SESSION_COOKIE_SECURE = True`** em produção  
   Isso evita que cookies sejam enviados por HTTP (somente HTTPS).

3. **Considere `SESSION_COOKIE_SAMESITE = 'Lax'` ou `'Strict'`**  
   Para evitar compartilhamento de sessão entre abas.

4. **Implemente "expiração forçada"** no logout  
   No `views.py`, remova manualmente a sessão:

   ```python
   from django.contrib.auth import logout

   def custom_logout(request):
       logout(request)
       request.session.flush()  # Remove a sessão ativa
   ```

Agora, na **produção**, cada login será tratado de forma mais isolada e segura.
