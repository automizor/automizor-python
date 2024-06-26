# Automizor Python automation framework

## dev setup
this package compiles version pinned dependencies via [uv](https://astral.sh/blog/uv) (compatible to [pip-tools](https://github.com/jazzband/pip-tools)) and provides a [justfile](https://github.com/casey/just) for convenience.

change dependencies in either `requirements/app.in` or `requirements/dev.in` and run `just refresh-requirements` in your console afterwards (assumes `uv` is used).

you also need a valid `.env` file to run tests, you can use the example `cp .env_example .env` and edit the content accordingly.