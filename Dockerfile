FROM ubuntu:16.04

MAINTAINER Dockerfiles

# 部署python3.5 以及 nginx 服务
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y && \
    git \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    supervisor \
    sqlite3 && \
    pip3 install -U pip setuptools &&
    rm -rf /var/lib/apt/lists/*

# 安装uwsgi 组件
RUN pip3 install uwsgi

# 配置nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-naboo.conf /etc/nginx/sites-acailable/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# 部署项目代码到docker中
COPY . /home/docker/src/

# 安装项目依赖项
RUN pip3 install -r /home/docker/src/requirements.txt

# yun
