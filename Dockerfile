FROM python:3.8

ADD recomendador.py .

ADD anime.csv .

RUN pip install -r requirements.txt

CMD [ "python", "./recomendador.py" ]