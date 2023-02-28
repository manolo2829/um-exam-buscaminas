FROM python:3

RUN git clone https://github.com/manolo2829/um-exam-buscaminas.git

WORKDIR /um-exam-buscaminas

RUN pip install -r requirements.txt

CMD ["python3", "-m", "unittest"]