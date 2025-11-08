FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Basic tools
RUN apt-get update && apt-get install -y --no-install-recommends \
  curl ca-certificates gnupg lsb-release apt-transport-https

# Install Node 18 via NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_18.x -o /tmp/nodesource_setup.sh \
  && bash /tmp/nodesource_setup.sh \
  && apt-get install -y nodejs

# Add LLVM apt helper and install pinned LLVM/libclang (example: 14)
RUN curl -sSL https://apt.llvm.org/llvm.sh -o /tmp/llvm.sh \
  && bash /tmp/llvm.sh 14 \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
     libclang-14-dev llvm-14 cmake python3 python3-venv python3-pip build-essential jq pkg-config

# Python venv and pip deps can be installed here (optional)
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv && . /opt/venv/bin/activate \
  && pip install --upgrade pip \
  && pip install -r /tmp/requirements.txt

WORKDIR /workspace
ENTRYPOINT ["/bin/bash"]
