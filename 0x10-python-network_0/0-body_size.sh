#!/bin/bash
#Get the size of HTTP response in bytes
curl -s "$1" | wc -c
