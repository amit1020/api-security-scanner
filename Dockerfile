FROM python:3.9

WORKDIR  /app

COPY requirements.txt .

RUN  pip install --upgrade pip

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 8000

#for running Django server
CMD ["python", "webscanner/manage.py", "runserver", "0.0.0.0:8000"]