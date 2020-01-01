FROM gitpod/workspace-full
                    
RUN apt-get -q update && \
    apt-get install -y python3-dev libxml2-utils librsvg2-bin && \
    pip install ensurepath standardebooks && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
# Missing: libimage-exiftool-perl, default-jre, calibre
# Skipped for now: inkscape

USER gitpod

# Install required fonts.
#mkdir -p $HOME/.local/share/fonts/
#cp $HOME/.local/pipx/venvs/standardebooks/lib/python3.*/site-packages/se/data/fonts/*/*.otf $HOME/.local/share/fonts/

# Refresh the local font cache.
#sudo fc-cache -f

# Optional: Bash users can install tab completion.
#sudo ln -s $HOME/.local/pipx/venvs/standardebooks/lib/python3.*/site-packages/se/completions/bash/se /usr/share/bash-completion/completions/se
