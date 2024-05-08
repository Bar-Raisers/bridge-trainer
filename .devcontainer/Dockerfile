FROM python:3.12-bookworm

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Python Development Tooling
RUN python3 -m pip install --no-cache-dir pipx && \
    python3 -m pipx ensurepath && \
    python3 -m pip install --no-cache-dir poetry

# Create Developer User
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV PATH /home/$USERNAME:/home/$USERNAME/.local/bin:$PATH

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install --no-install-recommends -y sudo \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER developer
WORKDIR /home/developer

# Install Trunk
RUN curl -fsSL https://get.trunk.io | bash -s -- -y;
