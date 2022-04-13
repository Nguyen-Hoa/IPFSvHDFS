#!/bin/bash

while true; do (top -p $1 -b -n1 | tail -2); sleep 0.5; done > $2