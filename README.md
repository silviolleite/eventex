# Eventex

Sistema de Eventos encomendado pela morena.
[![Build Status](https://travis-ci.org/silviolleite/eventex.svg?branch=master)](https://travis-ci.org/silviolleite/eventex)
[![Code Health](https://landscape.io/github/silviolleite/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/silviolleite/eventex/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/d7c578fb4cdcef3555a7/maintainability)](https://codeclimate.com/github/silviolleite/eventex/maintainability)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtual env com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:silviolleite/eventex.git wttd
cd wttd
python -m venv .wttd
.wttd\Scripts\activate.bat
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configura o email
git push heroku master --force
```