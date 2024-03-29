refresh-requirements:
    uv pip compile requirements/app.in -o requirements/app.txt
    uv pip compile requirements/dev.in -o requirements/dev.txt
    uv pip sync requirements/dev.txt