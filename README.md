
```
# gerar projeto para enviar ao gpchat
tar --exclude='djangos/.git' \
    --exclude='djangos/**/__pycache__' \
    --exclude='djangos/**/migrations' \
    --exclude='djangos/**/*.pyc' \
    --exclude='djangos/**/*.pyo' \
    --exclude='djangos/.venv' \
    --exclude='djangos/venv' \
    --exclude='djangos/.idea' \
    --exclude='djangos/.mypy_cache' \
    --exclude='djangos/.pytest_cache' \
    -czvf projeto.tar.gz djangos

```