FROM centos:8

RUN dnf update -y
RUN dnf install -y epel-release sqlite python3

RUN dnf upgrade -y

COPY src/requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

RUN yum install -y dnf-plugins-core
RUN dnf config-manager --set-enabled powertools
RUN yum install -y R
RUN R -e "install.packages(c('dplyr', 'jsonlite', 'RSQLite','DBI','ggplot2','shiny','shinydashboard'),dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN mkdir /app
COPY src /app
RUN chmod -R +rwx /app

WORKDIR /app

EXPOSE 5000
EXPOSE 5001

ENTRYPOINT ["/app/docker-entrypoint.sh"]
