FROM ubuntu:24.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG PYTHON_VERSION=3.12.7

# Install Ubuntu Dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        libbz2-dev \
        libffi-dev \
        liblzma-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxmlsec1-dev \
        llvm \
        make \
        sudo \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Delete Default Ubuntu User
RUN touch /var/mail/ubuntu && \
    chown ubuntu /var/mail/ubuntu && \
    userdel -r ubuntu

# Create Container User
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -G sudo -m $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > "/etc/sudoers.d/$USERNAME" && \
    chmod 0440 "/etc/sudoers.d/$USERNAME"

USER $USERNAME
WORKDIR "/home/$USERNAME"

ENV PYENV_ROOT="/home/$USERNAME/.pyenv"
ENV USER_HOME="/home/$USERNAME"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
ENV PATH="$USER_HOME:$USER_HOME/.local/bin:$PATH"

# Install Python
RUN curl https://pyenv.run | bash && \
    pyenv install $PYTHON_VERSION && \
    pyenv global $PYTHON_VERSION && \
    pyenv local $PYTHON_VERSION

# Install Rust for Pydantic Dependency
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y

# Install Python Development Tooling
RUN python3 -m pip install --no-cache-dir pipx && \
    python3 -m pipx ensurepath && \
    python3 -m pipx install poetry

# Install Trunk
RUN curl -fsSL https://get.trunk.io | bash -s -- -y;

# Grant GitPod User Permissions
RUN chmod 0755 /usr/local/bin/trunk
