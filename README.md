# Portfolio Project
---
This project is going to be a mixture of a project blog/cover letter/Django practice(With HTMX).

I will showcase projects I have worked on, and discuss what I've built while at PIRCH .

Current TODO:
    - Build main page, to discuss projects completed at Pirch and about me.
    - Use HTMX for some kind of interactivity.
    - Maybe build some kind of web scrapper to see what I'm working on between multiple sites.



---

This is a build out from my DjangoHtmxTodo project, which was practice for working on this.
https://github.com/SeanP94/DjangoHtmxTodo



Your .env file inside core/ should look like this (Obviously change things)
```
DEBUG=0
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=password123
DJANGO_SUPERUSER_EMAIL=none@gmail.com
DJANGO_SECRET_KEY=123123123123123123jkhjkjk

DB_USE_SSL=0
POSTGRES_DB=db
POSTGRES_PASSWORD=pgpassword123
POSTGRES_USER=myuser
POSTGRES_HOST=postgres_db
POSTGRES_PORT=5433
POSTGRES_READY=1
```


Commands for me in the future:

docker build -t registry.digitalocean.com/krayte/portfolio-core:latest -f Dockerfile .
docker push registry.digitalocean.com/krayte/portfolio-core --all-tags

kubectl create secret generic django-core-env --from-env-file=core/.env.prod
