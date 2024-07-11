#!/bin/bash

# Remove files from trash bins
find /var/www/html/data/*/files_trashbin/ -type f -exec rm -f {} \;

# Remove file versions
find /var/www/html/data/*/files_versions/ -type f -exec rm -f {} \;

# Optionally, remove logs
find /var/www/html -type f -name "*.log" -exec rm -f {} \;

echo "Cleanup completed at $(date)" >> /var/log/cleanup.log

