FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    git \
    wget \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3 /usr/bin/python

# создаем отдельное виртуальное окружение для python-пакетов
RUN python3 -m venv /opt/venv

# ставим пакеты внутрь venv, а не в системный python
RUN /opt/venv/bin/pip install --upgrade pip setuptools wheel && \
    /opt/venv/bin/pip install pytest selenium webdriver-manager

# чтобы python/pip брались из venv по умолчанию
ENV PATH="/opt/venv/bin:$PATH"

USER jenkins
