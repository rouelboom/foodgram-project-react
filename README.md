# Foodgram

http://51.250.2.131/

Сайт для публикации кулинарных рецептов. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в txt формате. 

### Установка
Проект собран в Docker и содержит четыре образа:

1. backend - образ бэка проекта (в разработке)
2. frontend - образ фронта проекта
3. postgres - образ базы данных PostgreSQL
4. nginx - образ web сервера nginx


#### Запуск проекта:
- Установите Docker
- Выполнить команду docker pull rouelboom/foodgram (will be able soon...)

#### Первоначальная настройка Django:
- docker-compose exec backend python manage.py migrate --noinput
- docker-compose exec backend python manage.py collectstatic --no-input 

#### Загрузка тестовой фикстуры в базу:
- docker-compose exec backend python manage.py loaddata fixtures.json

#### Создание суперпользователя:
- Суперпользователь был создать при загрузке фикстур автоматически. 
- Для доступа к учебной записи администратора используйте следующие данные: admin@admin.ru / admin

