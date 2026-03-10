


FROM python:3.13.12-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./src ./

RUN mkdir ./data

RUN python -m ensurepip --upgrade && \
    python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r ./requirements.txt

RUN chown -R 1001:0 ./ && \
    chmod -R a+rw ./
    
ENTRYPOINT [ "python", "main.py" ]
