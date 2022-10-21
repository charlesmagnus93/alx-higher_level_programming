#!/bin/bash
# Add header to GET request & display reponse body
curl -sb -X GET -H "X-School-User-Id: 98" "$1"
