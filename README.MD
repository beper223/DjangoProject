## Команды Django

- Запустить проект:
  ```bash
  ./manage.py runserver 0.0.0.0:8000
  ```

- Создать суперпользователя:
  ```bash
  ./manage.py createsuperuser
  ```
admin
12345
- Создать миграции:
  ```bash
  ./manage.py makemigrations
  ```

- Применить миграции к базе данных:
  ```bash
  ./manage.py migrate
  ```

---

[Открыть Markdown по файлу forms.md](forms.md)


docker-compose build --no-cache
docker-compose up -d
docker ps
docker exec -it bibl_app sh
nc -z -w 1 db 5432 && echo "DB is up"
ls -la /app/staticfiles
docker logs bibl_db
docker compose down
docker network prune -f 
docker compose up -d --build
docker run --rm -it --entrypoint sh bibl_web:latest
docker run --rm -it bibl_web:latest sh -c "/entrypoint.sh echo hi"


