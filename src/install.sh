#/bin/bash

#Setup the script it must be start on startup and auto restart

# Creare un file di servizio systemd
echo "[Unit]
Description=My Script

[Service]
ExecStart=$(pwd)/main.py

# Restarta il servizio dopo che si è interrotto
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/proxmox_tsensor.service

# Abilitare il servizio per avviarsi all'avvio
systemctl enable proxmox_tsensor.service

# Avviare il servizio ora
systemctl start proxmox_tsensor.service