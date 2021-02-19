FROM  httpd:latest

WORKDIR /usr/local/apache2/htdocs
COPY ["web", "./"]

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 CMD ["curl", "--head", "http://0.0.0.0:80"]

