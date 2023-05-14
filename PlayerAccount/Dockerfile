FROM python:3.11-slim

WORKDIR /app

COPY ./dist/player-0.1.0-py3-none-any.whl .

run pip3 install --upgrade --root-user-action=ignore pip
run pip3 install --root-user-action=ignore player-0.1.0-py3-none-any.whl
run pip3 install --root-user-action=ignore gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "player:create_app()" ]
