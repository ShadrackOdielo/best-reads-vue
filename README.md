# bestreads

Best reads is a book review site that allows users to search for books, leave reviews for individual books, and see the reviews made by other people. It also uses the a third-party API by Google books api, another book review website, to pull in ratings from a broader audience. Finally, users are able to query for book details and book reviews programmatically via the website’s API.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Api Endpoints
(currently only supports GET requests)
- /api/books
- /api/books/<isbn>
- /api/books/<isbn>/reviews
- /api/books/<isbn>/reviews/<review_id>(incomplete)
- /api/books/<isbn>/reviews/<review_id>/comments(incomplete)
- /api/books/<isbn>/reviews/<review_id>/comments/<comment_id>(incomplete)


## Basic Commands
### Running the Server

this app uses docker for development and deployment, so you will need to install docker and docker-compose
##### With Docker
```sh
docker-compose -f local.yml up
```
to run django commands, you will need to run them in the docker container
```sh
docker-compose -f local.yml run --rm django python manage.py <command>
```
##### Without Docker
not currently fully supported, I disabled it for later development
`




For more information, refer to the [Vue3 Vite Django Cookiecutter project](https://github.com/ilikerobots/cookiecutter-vue-django).




### Type checks

Running type checks with mypy:

    $ mypy best_reads2

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation
the app uses bootstrap 5 for styling, and uses sass for css compilation

## Deployment

The following details how to deploy this application.

### Vue

For production deployment, the Vue frontend must be built into static resources, which will be served
using the same Django staticfiles strategy as the rest of your site.

If you are using the production Docker configuration, this will be performed automatically when the images are built.

Otherwise, you must build the static assets yourself as part of your build and deploy process, sometime before the
`collectstatic` management command is run. The static assets may be built by running `npm run build` from within the
`vue_frontend` directory. The resulting files will be placed into the `best_reads2/static/vue` directory
and are handled subsequently as standard static assets.

Note the setting `VUE_FRONTEND_USE_DEV_SERVER` dictates whether your Django app will be expecting to serve Vue assets
from the Vite Dev Server or from a static build.  This setting defaults to the same as `DEBUG`, but can be modified as
needed.
If you wish to build static Vue assets on the local Docker configuration, you may run:
`docker-compose -f local.yml run vite vite build`

For more information, refer to the [Vue3 Vite Django Cookiecutter project](https://github.com/ilikerobots/cookiecutter-vue-django).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Authored by
- shadrack odielo

### Tools used
- [cookiecutter-django]()
- [cookiecutter-vue-django]()
- docker
- vue 3
- vite
- python
- django
- postgresql
- google books api
- nyt books api
