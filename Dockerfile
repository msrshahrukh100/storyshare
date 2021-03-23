FROM python:3.6.10-alpine3.11 as builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive


RUN mkdir -p /var/www/storyshare

WORKDIR /var/www/storyshare

# Copying requirements
COPY . .
RUN apk add --no-cache bash
RUN apk update && apk add --no-cache --virtual .build-deps bash \
    vim gcc linux-headers mariadb-dev musl-dev openssl git \
    sudo  py3-pip curl jpeg-dev  zlib-dev  freetype-dev  lcms2-dev  \
    openjpeg-dev  tiff-dev  tk-dev  tcl-dev  harfbuzz-dev  fribidi-dev\
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps
