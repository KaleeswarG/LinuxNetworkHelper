#!/bin/bash

# Clear the screen
clear

while true; do
    echo "====== UBUNTU NETWORKING TOOL ====="
    echo "1. SHOW IP ADDRESS"
    echo "2. PING A WEBSITE"
    echo "3. SHOW DEFAULT GATEWAY"
    echo "4. CHECK INTERNET CONNECTIVITY"
    echo "5. EXIT"
    echo
    read -p "ENTER CHOICE: " ch

    case $ch in
        1)
            echo "YOUR IP:"
            hostname -I
            ;;
        2)
            read -p "ENTER WEBSITE: " site
            ping -c 4 "$site"
            ;;
        3)
            echo "GATEWAY:"
            ip route | grep default
            ;;
        4)
            echo "NETWORK CONNECTION:"
            if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
                echo "Connection working."
            else
                echo "Not connected to the internet."
            fi
            ;;
        5)
            echo "THANK YOU"
            break
            ;;
        *)
            echo "INVALID INPUT"
            ;;
    esac

    echo
done
