# syntax=docker/dockerfile:1

FROM python_hello_world

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY favicon.ico favicon.ico
COPY leaflet.css leaflet.css
COPY leaflet.js leaflet.js
COPY leaflet.js.map leaflet.js.map
COPY main.py /
COPY templates templates

CMD [ "python", "./main.py", "--host=0.0.0.0"]