# estimate-back
back-end projetao

* Como executar:

Execute no repositório raiz:

```
python -m venv env
```

Após isso, vá ao repositório em /app e execute:

```
pip freeze > requirements.txt
```

Após isso, no mesmo local, execute, com o docker local aberto:

```
docker-compose up --build
```

Portas:

Swagger:
https://localhost:8000/docs

Banco (EM CRIAÇÃO):
https://localhost:5000