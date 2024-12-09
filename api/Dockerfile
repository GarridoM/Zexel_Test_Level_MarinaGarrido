FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies
# Section 3- Compiler and OS libraries
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \ 
  libpq-dev netcat-traditional curl libcurl4-openssl-dev libssl-dev \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy project
COPY . $APP_HOME

# Add the current directory to PYTHONPATH
ENV PYTHONPATH=$APP_HOME:$PYTHONPATH

# entrypoint.sh
RUN sed -i 's/\r$//g' $APP_HOME/scripts/entrypoint.sh
RUN chmod +x $APP_HOME/scripts/entrypoint.sh

# give files permissions to exec tests
RUN chmod +x $APP_HOME/scripts/*.sh
RUN find $APP_HOME -name "*.py" -exec chmod +x {} \;

EXPOSE 8000
CMD ["/bin/sh", "-c", "/home/app/web/scripts/entrypoint.sh && gunicorn zexeltest.wsgi:application --workers 3 --threads 100 --max-requests 1000 --bind 0.0.0.0:8000 --log-level=DEBUG --reload"]
