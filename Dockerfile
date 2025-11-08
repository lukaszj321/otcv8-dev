FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential cmake git wget curl python3 python3-venv python3-pip \
  clang llvm libclang-dev nodejs npm jq ca-certificates \
  && rm -rf /var/lib/apt/lists/*
# nodejs in ubuntu may be older; you can add nodesource if you need v18+
WORKDIR /workspace
COPY . /workspace
# optional: install python clang binding in venv
RUN python3 -m venv /opt/venv && . /opt/venv/bin/activate && pip install --upgrade pip clang
ENV PATH="/opt/venv/bin:${PATH}"
CMD ["/bin/bash"]
