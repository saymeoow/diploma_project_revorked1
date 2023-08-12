FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
