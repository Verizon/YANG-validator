FROM python:3

WORKDIR /app

RUN pip install nameko
RUN pip install pyang
RUN pip install pyangbind

copy transformer/*.py ./
copy transformer/mappings ./mappings
copy config.yaml ./

CMD ["nameko", "run", "toYangJsonSvc", "--config", "config.yaml"]
