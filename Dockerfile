#FROM ubuntu:latest
FROM python:3-alpine
MAINTAINER juancra264 "juancra264@hotmail.com"
#RUN apt-get update -y --fix-missing
#COPY ./scripts/requirements.txt /tmp/requirements.txt
#RUN apt-get install -y python-pip python-dev build-essential 
ADD ./scripts /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]:
