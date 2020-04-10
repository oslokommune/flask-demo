Serverless Flask app demo
=========================

Based on example at <https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/>


## Tests

Tests are run using [tox](https://pypi.org/project/tox/): `make test`

For tests and linting we use [pytest](https://pypi.org/project/pytest/),
[flake8](https://pypi.org/project/flake8/) and
[black](https://pypi.org/project/black/).


## Deploy

`make deploy` or `make deploy-prod`

Requires `saml2aws`
