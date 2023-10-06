FROM python:3.12.0a1-buster
RUN apt-get update &&\ 
    adduser myuser
ENV IMAGE_DIRECTORY="qrcodes"
ENV URL="https://github.com/bovanphillips2"
ENV FILE_NAME="github.png"
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","./main.py"]
