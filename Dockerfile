FROM python:3.10
WORKDIR /bot
RUN apt-get update && apt-get install git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "otaku/bot.py" ]
