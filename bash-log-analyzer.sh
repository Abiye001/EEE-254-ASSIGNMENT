#!/bin/bash

# Log File Analyzer using grep

# Check if directory is provided
if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/logs"
  exit 1
fi

LOG_DIR="$1"

echo "🔍 Scanning logs in: $LOG_DIR"
echo

# Count different log levels
echo "📊 Log Level Summary:"
echo -n "INFO: "
grep -ri --exclude-dir={node_modules,__pycache__} "INFO" "$LOG_DIR" | wc -l
echo -n "WARNING: "
grep -ri --exclude-dir={node_modules,__pycache__} "WARNING" "$LOG_DIR" | wc -l
echo -n "ERROR: "
grep -ri --exclude-dir={node_modules,__pycache__} "ERROR" "$LOG_DIR" | wc -l
echo

# List all files with log activity
echo "📁 Files containing logs:"
grep -ril --exclude-dir={node_modules,__pycache__} "INFO\|WARNING\|ERROR" "$LOG_DIR"
echo

# Show ERROR logs with context
echo "❗ ERROR Logs with context:"
grep -rni --color=auto --exclude-dir={node_modules,__pycache__} -C 2 "ERROR" "$LOG_DIR"
