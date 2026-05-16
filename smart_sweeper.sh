#!/bin/bash
THRESHOLD=80
CURRENT_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//')
if [ "$CURRENT_USAGE" -gt "$THRESHOLD" ]; then
    BEFORE=$(df / | grep / | awk '{ print $4 }')
    rm -rf /tmp/*
    find /var/lib/docker/containers/ -type f -name "*.log" -delete
    docker system prune -a -f
    AFTER=$(df / | grep / | awk '{ print $4 }')
    SAVED=$((AFTER - BEFORE))
    echo "يا معتز، قمتُ بتنظيف السيرفر تلقائياً ووفرتُ لك $SAVED ميجابايت" > /tmp/telegram_msg.txt
fi
