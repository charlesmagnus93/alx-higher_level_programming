#!/bin/bash
# POST request body
curl -sb -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
