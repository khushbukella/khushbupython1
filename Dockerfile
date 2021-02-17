FROM python:2
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./sources/calc.py" ]