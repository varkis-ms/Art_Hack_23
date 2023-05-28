# Backend for mobile app (popularization of Moscow art)

## Info
При запуске сервиса доступна документация. `http://your_domain:port/swagger`

## Commands
* `make env` - создание конфигурационного файла .env из данных в .env.sample
* `make service_up` - запуск docker-compose с сервисом и базами данных (Postgresql, Redis, Mongo)
* `make revision` - создание новой ревизии миграции базы данных
* `make migrate head` - миграция базы данных
* `poetry run python3 -m backend` - запуск сервиса локально
* `poetry run python3 -m isort` & `poetry run python3 -m black` - реформатирование кода
* `poetry run python3 -m pylint` - линтер кода