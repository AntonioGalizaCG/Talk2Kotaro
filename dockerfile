FROM ubuntu:20.04

ENV TZ=Japan
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev espeak ffmpeg libsm6 libxext6

#RUN pip3 install --upgrade tensorflow

#RUN pip3 install psutil

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

RUN mkdir -p /app/flask_session

RUN chmod 777 /app/flask_session

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY flaskapp.py /app
COPY mailer.py /app
COPY locker.py /app
COPY encryption.py /app
#COPY EmotionEstimator.py /app
COPY forbidden_phonemes.py /app
COPY utils.py /app
COPY tabler.py /app
#COPY model.h5 /app
COPY static /app/static

#Uncomment the line below if you want to include the webpage templates in the dockerfile
#COPY templates /app/templates

#COPY memory /app/memory

RUN useradd -ms /bin/bash <youruser>

ENTRYPOINT [ "python3" ]

CMD [ "flaskapp.py" ]
