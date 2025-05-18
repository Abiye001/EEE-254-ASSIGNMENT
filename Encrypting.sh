#!/bin/bash

echo "Choose operation: (1) Encrypt or (2) Decrypt"
read -p "Enter 1 or 2: " choice

if [[ "$choice" == "1" ]]; then
    read -p "Enter path to the input file to encrypt: " input_file
    read -p "Enter output file name (e.g., file.enc): " output_file
    read -s -p "Enter encryption password: " password
    echo ""
    openssl enc -aes-256-cbc -salt -in "$input_file" -out "$output_file" -pass pass:"$password"
    echo "✅ File encrypted successfully as '$output_file'."

elif [[ "$choice" == "2" ]]; then
    read -p "Enter path to the encrypted file: " input_file
    read -p "Enter output file name for decrypted data: " output_file
    read -s -p "Enter decryption password: " password
    echo ""
    openssl enc -d -aes-256-cbc -in "$input_file" -out "$output_file" -pass pass:"$password"
    echo "✅ File decrypted successfully as '$output_file'."

else
    echo "❌ Invalid option. Please enter 1 for encryption or 2 for decryption."
fi
