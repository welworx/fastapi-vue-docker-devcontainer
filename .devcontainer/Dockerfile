# DEV-Container environment for python and vue
FROM python:3.12-slim

ARG POETRY_VERSION="none"

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN apt-get update 
RUN apt-get install --no-install-recommends -y software-properties-common

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl

# Install NVM and Node
RUN mkdir /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 20.16.0 
RUN curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Poetry
RUN pip3 install poetry=="${POETRY_VERSION}"
RUN if [ "${POETRY_VERSION}" != "none" ]; then \
    pip3 install poetry==${POETRY_VERSION}; \
fi
