FROM jenkins/jenkins:lts

LABEL TAG="falcon/jenkins-dind:latest"
LABEL VERSION="0.0.1"
LABEL MAINTAINER="Sergey Sokolov"

ARG HOST_UID=1001
ARG HOST_GID=997

USER root

RUN apt-get update -qq && apt-get install -qqy apt-transport-https ca-certificates lsb-release curl gnupg-agent && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor | tee /usr/share/keyrings/docker-ce-archive-keyring.gpg > /dev/null && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-ce-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker-ce.list > /dev/null && \
    apt-get update && \
    apt-get install docker-ce docker-ce-cli containerd.io -y && \
    rm -rf /var/lib/apt/lists/*


RUN curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
 && chmod +x /usr/local/bin/docker-compose \
 && ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose \
 && usermod -u $HOST_UID jenkins \
 && groupmod -g $HOST_GID docker \
 && usermod -aG docker jenkins

EXPOSE 8080

USER jenkins
