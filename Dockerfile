FROM python:3.9.16-slim-buster

WORKDIR /workspace

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    npm \
    nodejs \
    expect \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && chsh -s /bin/zsh

COPY requirements.txt .

# hadolint ignore=DL3013,DL3016
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && npm install -g atcoder-cli
