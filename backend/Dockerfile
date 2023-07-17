FROM python:3.8

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt /ws/requirements.txt

WORKDIR /ws

RUN pip install -r requirements.txt

COPY ./app/ /ws

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]