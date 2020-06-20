FROM ubuntu:20.04
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y locales curl python3-distutils \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && apt-get install -y nodejs \
    && apt-get install -y npm \
    && npm install -g n \
    && n 12.13.0 \
    && export PATH=$PATH:/usr/local/bin/node \
    && python3 get-pip.py \
    && pip install -U pip \
    && mkdir /code \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN node -v \
    && npm -v
ENV LANG en_US.utf8
WORKDIR /code
ADD haruuback/ /code/
RUN ls
RUN pip install -r requirements.txt    # requirements.txtからパッケージのインストール
WORKDIR /code/customers/webpackconfig
RUN npm install
RUN npx webpack
WORKDIR /code/