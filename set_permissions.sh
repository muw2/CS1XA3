#!/bin/bash

chown -R "$USER:$USER" "$HOME/CS1XA3"

chmod -R 755 "$HOME/CS1XA3/public_html"
chmod 770 "$HOME/CS1XA3/private"
chmod -rw-r-r- README.md
