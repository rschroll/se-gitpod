FROM gitpod/workspace-full

USER root

RUN apt-get -q update && \
    apt-get install -y python3-dev libxml2-utils && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
# Missing: libimage-exiftool-perl, default-jre, calibre
# Skipped for now: inkscape, librsvg2-bin (brings in GUI)

USER gitpod

RUN python3 -m pip install standardebooks

# Install required fonts.
RUN mkdir -p $HOME/.local/share/fonts/ && \
    cp /home/gitpod/.pyenv/versions/3.*/lib/python3.*/site-packages/se/data/fonts/*/*.otf $HOME/.local/share/fonts/ && \
    sudo fc-cache -f

# Bash users can install tab completion.
RUN sudo ln -s /home/gitpod/.pyenv/versions/3.*/lib/python3.*/site-packages/se/completions/bash/se /usr/share/bash-completion/completions/se
