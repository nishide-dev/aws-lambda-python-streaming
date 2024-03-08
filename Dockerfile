# Base image
FROM public.ecr.aws/docker/library/python:3.12.0-slim-bullseye
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# copy the dependencies file to the working directory 
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# install dependencies and clean up in one layer
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# copy the content of the local src directory to the working directory 
COPY . ./

# command to run on container start 
CMD ["poetry", "run", "python", "src/app.py"]