#!/bin/bash
# display request body size
curl -so /dev/null "$1" -w '%{size_download}\n'
