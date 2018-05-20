FROM python:3.6-alpine

RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo 'America/Sao_Paulo' > /etc/timezone
RUN apk add -U tzdata

ARG CWD=/opt/app
WORKDIR ${CWD}
COPY requirements.txt ${CWD}

RUN apk -U add gcc g++ make && \
    pip install --no-cache-dir -U -r requirements.txt && \
    apk -U del --purge gcc g++ make

COPY . ${CWD}

CMD ["python", "-m", "api"]
