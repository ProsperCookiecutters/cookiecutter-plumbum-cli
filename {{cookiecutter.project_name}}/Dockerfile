FROM {{cookiecutter.docker_image}}

ARG VERSION
ARG SPECIAL_INSTALL

COPY . /opt/{{cookiecutter.project_name}}

WORKDIR /opt/{{cookiecutter.project_name}}
RUN sudo pip3 install .$SPECIAL_INSTALL
