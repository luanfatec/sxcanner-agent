#!/bin/bash

echo""
	PROGRAMA=( "cut" "grep" "cat" "sed" "curl" "wget" "python3-pip" "python3-mysqldb" )
	for prog in "${PROGRAMA[@]}";do
        echo -ne "\033[00;32m               ----------------| $prog for dependencies "
		if ! hash "$prog" 2>/dev/null;then
			echo -e "\033[00;31m<<<Not installed!>>>\033[00;37m"
		else
			echo -e "\033[00;32m<<<Installed!>>>\033[00;37m"
		fi
		sleep 1
		
    done
        
    for prog_inst in "${PROGRAMA[@]}";do
        if ! hash "$prog_inst" 2>/dev/null;then
            echo -e "\n\033[00;32mTrying to install dependencies...\033[00m"
            apt update && sleep 3 && apt install -y $prog_inst
            sleep 0.5
        else
            sleep 0.5
            continue
        fi
    done