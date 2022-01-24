FROM python:3.10.1
FROM gorialis/discord.py

RUN apt-get -y update
RUN python3 --version


RUN mkdir -p /user/src/bot
WORKDIR /usr/src/bot

COPY . .

CMD ["python3", "main.py"]