#!/bin/bash
# Displays only the status code of the response.
curl -so /dev/null -sw "%{http_code}" "$1"
