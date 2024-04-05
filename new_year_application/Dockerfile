FROM python:3.10-alpine3.18

RUN python -m pip install --upgrade pip

COPY . /new_year_application

WORKDIR /new_year_application

RUN python -m pip install -r requirements.txt

ENTRYPOINT flask --app app.py run --host=0.0.0.0 --port 5000