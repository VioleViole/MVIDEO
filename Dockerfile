FROM python:3.10.11

# Рабочий каталог
WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# файл требований в контейнер
# python3 python3-pip python3-tk python3-dev python-xlib
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip python3-tk python3-dev \
    libpq-dev scrot xvfb xserver-xephyr tigervnc-standalone-server xfonts-base && \
    apt-get clean && apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# Установка Хрома
#================================================================================
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
#
#================================================================================

# остальные файлы проекта

COPY requirements.txt .

RUN pip install -r requirements.txt

# Установка модулей
COPY main.py .

COPY get_data.py .

COPY autoupdate.py .

COPY main_api.py .

COPY connect_db.py .

# порт
EXPOSE 5432

# запуск
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "5432"]


#RUN apt-get update && apt-get install --no-install-recommends -y \
#    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
#    libnspr4 libnss3 libgbm1 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
#    curl unzip wget bzip2 \
#    xvfb xauth libgl1-mesa-dev xz-utils && \
#    apt-get clean && apt-get -y autoremove && \
#    rm -rf /var/lib/apt/lists/*
#
#ARG CHROMEDRIVER_VERSION
#ARG CHROME_SETUP
#
#RUN CHROMEDRIVER_VERSION=$CHROMEDRIVER_VERSION && \
#    wget --no-verbose https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
#    unzip chromedriver_linux64.zip -d /usr/bin && \
#    chmod +x /usr/bin/chromedriver && \
#    rm chromedriver_linux64.zip && \
#    \
#    CHROME_SETUP=$CHROME_SETUP && \
#    wget --no-verbose -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
#    dpkg -i $CHROME_SETUP && \
#    apt-get install -y -f --no-install-recommends && \
#    rm $CHROME_SETUP