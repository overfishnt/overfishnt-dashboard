FROM python:3.11.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install unzip

RUN pip install gdown

# Replace this with the model version google drive ids
# The file is in the folder model/{version}/saved_model.zip

RUN mkdir models

RUN gdown 1ygiax7dIVrHhvgevaA2o1CpTb_MoGUGL

RUN unzip saved_model.zip -d models/

RUN rm saved_model.zip

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

EXPOSE 8001

CMD ["python", "main.py"]

