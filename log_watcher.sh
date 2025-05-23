#!/bin/bash

# Configuration
LOG_FILE="/var/log/auth.log"  # Adjust path if needed
THRESHOLD=5                   # Number of failed attempts to trigger alert
TIME_WINDOW=10                # In minutes
ALERT_FILE="suspicious_ips.log"

# Color codes
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
NC="\e[0m" # No color

echo -e "${GREEN}Analyzing log for failed login attempts...${NC}"

# Get the current timestamp
NOW=$(date +%s)

# Extract failed login attempts
grep "Failed password" "$LOG_FILE" | awk '{print $1, $2, $3, $(NF)}' | while read -r month day time ip; do
    # Convert log timestamp to epoch
    LOG_DATE=$(date -d "$month $day $time" +%s 2>/dev/null)

    if [[ $LOG_DATE && $(($NOW - $LOG_DATE)) -le $(($TIME_WINDOW * 60)) ]]; then
        echo "$ip" >> temp_ips.log
    fi
done

# Count occurrences per IP
sort temp_ips.log | uniq -c | while read count ip; do
    if [[ $count -ge $THRESHOLD ]]; then
        echo -e "${RED}ALERT: $count failed attempts from $ip in last $TIME_WINDOW minutes${NC}"
        echo "$(date): $ip - $count failed attempts" >> "$ALERT_FILE"
    else
        echo -e "${YELLOW}NOTICE: $count attempts from $ip (under threshold)${NC}"
    fi
done

# Clean up
rm -f temp_ips.log

echo -e "${GREEN}Log scan complete.${NC}"
