FROM python:3.9

ARG USER=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt update -y && apt install -y sudo
RUN groupadd --gid $USER_GID $USER && \
    useradd --uid $USER_UID --gid $USER_GID -m $USER && \
    echo ${USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    chsh ${USER} -s /bin/bash

RUN mkdir -p /commandhistory
RUN chown -R ${USER} /commandhistory

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && \
  echo $SNIPPET >> "/home/${USER}/.bashrc"

RUN apt update -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN apt install -y \
    build-essential \
    curl \
    git



RUN mkdir -p /code
RUN chown -R ${USER} /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN pip install nbdev jupyter
# RUN pip install fastai
# RUN pip install openai
# RUN pip install pre-commit
RUN nbdev_install_quarto

USER ${USER}
ENV git config user.name ${GITHUB_NAME}
ENV git config user.email ${GITHUB_EMAIL}
# USER root
ENV PATH "${PATH}:/home/${USER}/.local/bin"

# RUN pre-commit install

ADD . .