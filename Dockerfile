# name=Dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y curl ca-certificates gnupg
# add llvm apt repo and install pinned version (example llvm-14)
RUN curl -sSL https://apt.llvm.org/llvm.sh | bash -s -- 14
RUN apt-get update && apt-get install -y libclang-14-dev llvm-14 nodejs npm python3 python3-venv python3-pip cmake build-essential jq
# optional: install pip deps
COPY requirements.txt /tmp/
RUN python3 -m venv /opt/venv && . /opt/venv/bin/activate && pip install --upgrade pip && pip install -r /tmp/requirements.txt
# Copy project after building image in CI usage
WORKDIR /workspace
ENTRYPOINT ["/bin/bash"]
