#!/bin/bash

while true; do (docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemPerc}}"| tail -2); sleep 1; done > $1
