#!/bin/bash

# bash-log-watcher-email.sh
# Author: Samuel Joseph Abiye
# Day 40 - #200DaysOfCode

LOG_FILE="/var/log/auth.log"
ALERT_FILE="suspicious_activity.log"
FAILED_LIMIT=5
ALERT_EMAIL="your_email@example.com"

echo "🔍 Monitoring suspicious login activity in $LOG_FILE..."
echo "Report will be saved in $ALERT_FILE"
echo "Sending alerts to: $ALERT_EMAIL"

# Empty alert file
> "$ALERT_FILE"

# Timestamp
echo -e "\n=== [ $(date) ] ===\n" >> "$ALERT_FILE"

# 1. Failed login attempts
echo "[!] Checking for failed login attempts..." >> "$ALERT_FILE"
grep "Failed password" "$LOG_FILE" | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | while read count ip
do
    if [ "$count" -gt "$FAILED_LIMIT" ]; then
        echo "⚠️  $count failed login attempts from IP: $ip" >> "$ALERT_FILE"
        ALERT=true
    fi
done

# 2. Successful root logins
echo -e "\n[+] Successful root logins:" >> "$ALERT_FILE"
grep "Accepted.*root" "$LOG_FILE" >> "$ALERT_FILE"

# 3. Invalid user attempts
echo -e "\n[+] Invalid user login attempts:" >> "$ALERT_FILE"
grep "Invalid user" "$LOG_FILE" >> "$ALERT_FILE"

# 4. Sudo usage
echo -e "\n[+] Sudo usage attempts:" >> "$ALERT_FILE"
grep "sudo" "$LOG_FILE" >> "$ALERT_FILE"

# Send email if ALERT flag was triggered
if grep -q "⚠️" "$ALERT_FILE"; then
    echo "📧 Sending alert email..."
    mail -s "🚨 Suspicious Activity Detected on $(hostname)" "$ALERT_EMAIL" < "$ALERT_FILE"
else
    echo "✅ No critical alerts found. No email sent."
fi

echo -e "\n✅ Analysis complete. See '$ALERT_FILE' for full details."
