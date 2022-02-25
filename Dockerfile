FROM python:3.8

#Author and Maintainer
MAINTAINER wisrovi.rodriguez@gmail.com

WORKDIR /buscador_coincidencias

RUN uname -a

RUN pip install uvicorn
RUN pip install jinja2
RUN pip install "uvicorn[standard]"
RUN pip install python-multipart
RUN pip install fastapi
RUN pip install requests

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]