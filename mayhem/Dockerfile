FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        clang \
        python3-dev \
        libfuzzer-19-dev \
        patchelf \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang CXX=clang++

RUN python3 -m pip install --no-cache-dir atheris

# Build
ADD . /src
WORKDIR /src
RUN python3 -m pip install --no-cache-dir .

CMD ["/src/mayhem/fuzz_check.py"]
