# Flask-uWSGI-NGINX

**Flask-uWSGI-NGINX** is an example project of a Flask application that uses [NGINX](#NGINX) as Reverse Proxy and a [uWSGI](#uWSGI) Server. The Flask application has one single endpoint:

> / - This endpoint only returns a HTML string:

```bash
Hello, world!
```

## Contents

- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Run](#run)
- [Authors](#Authors)

---

## Dependencies

![Python +3.7](https://img.shields.io/badge/python-+3.7-blue.svg)
![Docker](https://img.shields.io/badge/docker-*-blue.svg)
![NGINX 1.17.3](https://img.shields.io/badge/nginx-*-green.svg)

---

## Configuration

### NGINX

The Docker instance of **NGINX** needs an `nginx.conf` file that contains the following custom settings at least:

```bash
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://flask-api-ip:flask-api-port/;
        proxy_set_header Host "localhost";
    }
}
```

You can find this file in `./nginx`, also in this directory is the Dockerfile to create the **NGINX** instance.

### uWSGI

To run the uWSGI server it's necessary a `run.ini` file with the following settings at least:

```bash
[uwsgi]
module = wsgi:app
protocol = http
socket = :8080
plugin = python
master = 1
```

You can run this project locally with the following command:

```bash
pipenv run uwsgi run.ini -H $(pipenv --venv)
```

## Run

This system comes with a `docker-compose.yml` file to run it, just open a terminal in this directory and execute:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)
