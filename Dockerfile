FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc
WORKDIR /Test_Energo
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn run:app --host 0.0.0.0 --port 8000 --reload