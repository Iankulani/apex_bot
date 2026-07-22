#!/bin/bash
# APEX-BOT v5.0.0 Linux/macOS Installation Script
# Author: Ian Carter Kulani, MSc

set -e

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                   APEX-BOT v5.0.0 Installation Script                       ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${BLUE}[INFO] Starting installation of APEX-BOT v5.0.0${NC}"

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     OS_TYPE="Linux";;
    Darwin*)    OS_TYPE="macOS";;
    *)          OS_TYPE="UNKNOWN";;
esac

echo -e "${BLUE}[INFO] Detected OS: ${OS_TYPE}${NC}"

# Check Python version
echo -e "${BLUE}[INFO] Checking Python version...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 is not installed. Please install Python 3.7 or higher.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if [[ "$(echo "$PYTHON_VERSION" | cut -d. -f1)" -lt 3 ]] || [[ "$(echo "$PYTHON_VERSION" | cut -d. -f2)" -lt 7 ]]; then
    echo -e "${RED}[ERROR] Python 3.7 or higher is required. Found: ${PYTHON_VERSION}${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Python ${PYTHON_VERSION} found${NC}"

# Install system dependencies
echo -e "${BLUE}[INFO] Installing system dependencies...${NC}"
case "${OS_TYPE}" in
    Linux)
        if command -v apt-get &> /dev/null; then
            echo -e "${BLUE}[INFO] Using APT package manager${NC}"
            sudo apt-get update
            sudo apt-get install -y \
                python3-pip python3-dev \
                build-essential libpcap-dev \
                nmap nikto whois dnsutils \
                traceroute netcat-openbsd \
                tcpdump iptables \
                curl wget git \
                libssl-dev libffi-dev \
                chromium-browser chromium-chromedriver \
                chromium \
                sudo
        elif command -v yum &> /dev/null; then
            echo -e "${BLUE}[INFO] Using YUM package manager${NC}"
            sudo yum install -y \
                python3 python3-pip python3-devel \
                gcc gcc-c++ make libpcap-devel \
                nmap nikto whois bind-utils \
                traceroute nc tcpdump iptables \
                curl wget git \
                openssl-devel libffi-devel \
                chromium chromium-headless
        elif command -v dnf &> /dev/null; then
            echo -e "${BLUE}[INFO] Using DNF package manager${NC}"
            sudo dnf install -y \
                python3 python3-pip python3-devel \
                gcc gcc-c++ make libpcap-devel \
                nmap nikto whois bind-utils \
                traceroute nc tcpdump iptables \
                curl wget git \
                openssl-devel libffi-devel \
                chromium chromium-headless
        elif command -v pacman &> /dev/null; then
            echo -e "${BLUE}[INFO] Using Pacman package manager${NC}"
            sudo pacman -S --needed \
                python python-pip python-virtualenv \
                base-devel libpcap \
                nmap nikto whois dnsutils \
                traceroute netcat tcpdump iptables \
                curl wget git \
                openssl libffi \
                chromium chromium-extension
        fi
        ;;
    macOS)
        if command -v brew &> /dev/null; then
            echo -e "${BLUE}[INFO] Using Homebrew${NC}"
            brew install python3 nmap nikto whois dnsutils traceroute netcat tcpdump curl wget git openssl libpcap chromium
            pip3 install --upgrade pip
        else
            echo -e "${YELLOW}[WARN] Homebrew not found. Please install manually:${NC}"
            echo "  python3, nmap, nikto, whois, dnsutils, traceroute, netcat, tcpdump, curl, wget, git, chromium"
        fi
        ;;
    *)
        echo -e "${YELLOW}[WARN] Unsupported OS. Please install dependencies manually:${NC}"
        echo "  python3, nmap, nikto, whois, dnsutils, traceroute, netcat, tcpdump, curl, wget, git"
        ;;
esac

# Create virtual environment
echo -e "${BLUE}[INFO] Creating Python virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo -e "${BLUE}[INFO] Upgrading pip...${NC}"
pip install --upgrade pip setuptools wheel

# Install Python dependencies
echo -e "${BLUE}[INFO] Installing Python dependencies...${NC}"
pip install -r requirements.txt

# Install additional tools
echo -e "${BLUE}[INFO] Installing additional Python tools...${NC}"
pip install pyinstaller bandit safety pylint black

# Create necessary directories
echo -e "${BLUE}[INFO] Creating directories...${NC}"
mkdir -p .apex_bot apex_reports temp logs
mkdir -p .apex_bot/payloads .apex_bot/workspaces .apex_bot/scans
mkdir -p .apex_bot/phishing_pages .apex_bot/captured_credentials
mkdir -p .apex_bot/ssh_keys .apex_bot/traffic_logs
mkdir -p .apex_bot/nikto_results .apex_bot/keylogs
mkdir -p .apex_bot/spear_phishing .apex_bot/agents
mkdir -p .apex_bot/exe_payloads .apex_bot/pdf_payloads
mkdir -p .apex_bot/docx_payloads .apex_bot/link_payloads
mkdir -p .apex_bot/network_payloads .apex_bot/ip_monitor

# Set permissions
echo -e "${BLUE}[INFO] Setting permissions...${NC}"
chmod +x *.sh *.py 2>/dev/null || true

# Create configuration file
echo -e "${BLUE}[INFO] Creating default configuration...${NC}"
cat > .apex_bot/config.json << EOF
{
    "version": "5.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "auto_block_threshold": 5,
    "scan_timeout": 30,
    "report_format": "html",
    "generate_graphics": true,
    "keylogger_enabled": true,
    "keylogger_port": 4444,
    "keylogger_interval": 30,
    "keylogger_screenshot_interval": 60,
    "payload_callback_host": "localhost",
    "payload_callback_port": 5555,
    "web": {
        "enabled": true,
        "port": 5000,
        "host": "0.0.0.0",
        "secret_key": "",
        "require_auth": true,
        "username": "admin",
        "password_hash": "",
        "theme": "gradient"
    },
    "discord": {
        "enabled": false,
        "token": "",
        "channel_id": "",
        "prefix": "!",
        "admin_role": "Admin"
    },
    "slack": {
        "enabled": false,
        "bot_token": "",
        "app_token": "",
        "channel_id": "",
        "prefix": "!"
    },
    "telegram": {
        "enabled": false,
        "bot_token": "",
        "chat_id": "",
        "prefix": "/"
    },
    "signal": {
        "enabled": false,
        "phone_number": "",
        "group_id": "",
        "prefix": "!"
    },
    "whatsapp": {
        "enabled": false,
        "phone_number": "",
        "prefix": "!"
    },
    "google_chat": {
        "enabled": false,
        "webhook_url": "",
        "space_id": "",
        "prefix": "/"
    },
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "syn_flood_threshold": 100,
        "http_flood_threshold": 200,
        "scan_interval": 300,
        "max_ips": 10000
    },
    "traffic_generation": {
        "enabled": true,
        "max_duration": 300,
        "max_packet_rate": 1000,
        "allow_floods": false
    },
    "social_engineering": {
        "enabled": true,
        "default_port": 8080,
        "capture_credentials": true,
        "auto_shorten_urls": true
    },
    "ssh": {
        "enabled": true,
        "default_timeout": 30,
        "max_connections": 5
    },
    "ddos": {
        "enabled": true,
        "max_threads": 100,
        "default_duration": 30
    },
    "agent": {
        "enabled": false,
        "server": "localhost",
        "port": 5555,
        "heartbeat": 60
    },
    "payload": {
        "enabled": true,
        "default_callback": "localhost",
        "default_port": 4444,
        "exe_icon": "",
        "docx_template": "default"
    }
}
EOF

# Create sample .env file
echo -e "${BLUE}[INFO] Creating sample .env file...${NC}"
cat > .env << EOF
# APEX-BOT Environment Configuration
APEX_ENV=development
APEX_HOST=0.0.0.0
APEX_PORT=5000
APEX_DEBUG=true
APEX_SECRET_KEY=change_this_in_production

# Bot Tokens (optional)
DISCORD_TOKEN=
SLACK_TOKEN=
TELEGRAM_TOKEN=
WHATSAPP_PHONE=
SIGNAL_PHONE=
GOOGLE_CHAT_WEBHOOK=
EOF

# Create systemd service file (Linux only)
if [[ "${OS_TYPE}" == "Linux" ]]; then
    echo -e "${BLUE}[INFO] Creating systemd service file...${NC}"
    CURRENT_DIR=$(pwd)
    CURRENT_USER=$(whoami)
    cat > apex-bot.service << EOF
[Unit]
Description=APEX-BOT v5.0.0 Cybersecurity Platform
After=network.target docker.service
Wants=docker.service

[Service]
Type=simple
User=${CURRENT_USER}
WorkingDirectory=${CURRENT_DIR}
Environment="PATH=${CURRENT_DIR}/venv/bin:/usr/local/bin:/usr/bin:/bin"
Environment="PYTHONUNBUFFERED=1"
ExecStart=${CURRENT_DIR}/venv/bin/python3 ${CURRENT_DIR}/apex_bot.py
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

    echo -e "${YELLOW}[INFO] To install systemd service:${NC}"
    echo "  sudo cp apex-bot.service /etc/systemd/system/"
    echo "  sudo systemctl daemon-reload"
    echo "  sudo systemctl enable apex-bot"
    echo "  sudo systemctl start apex-bot"
fi

# Create startup script
echo -e "${BLUE}[INFO] Creating startup script...${NC}"
cat > start.sh << 'EOF'
#!/bin/bash
# APEX-BOT Startup Script

cd "$(dirname "$0")"
source venv/bin/activate
python3 apex_bot.py "$@"
EOF
chmod +x start.sh

# Create update script
echo -e "${BLUE}[INFO] Creating update script...${NC}"
cat > update.sh << 'EOF'
#!/bin/bash
# APEX-BOT Update Script

echo "Updating APEX-BOT..."
cd "$(dirname "$0")"
source venv/bin/activate
pip install --upgrade -r requirements.txt
echo "Update complete!"
EOF
chmod +x update.sh

# Cleanup
echo -e "${BLUE}[INFO] Cleaning up...${NC}"
deactivate

# Final message
echo -e ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                    APEX-BOT v5.0.0 INSTALLATION COMPLETE                  ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
echo -e ""
echo -e "${BLUE}📁 Installation Directory: $(pwd)${NC}"
echo -e "${BLUE}🐍 Virtual Environment: venv/bin/activate${NC}"
echo -e ""
echo -e "${YELLOW}🚀 To start APEX-BOT:${NC}"
echo -e "  ${GREEN}./start.sh${NC}"
echo -e "  ${GREEN}or${NC}"
echo -e "  ${GREEN}source venv/bin/activate && python3 apex_bot.py${NC}"
echo -e ""
echo -e "${BLUE}🌐 Web Dashboard: http://localhost:5000${NC}"
echo -e "${BLUE}⌨️ Keylogger port: 4444${NC}"
echo -e "${BLUE}🎣 Phishing server port: 8080${NC}"
echo -e ""
echo -e "${PURPLE}📚 Documentation: https://github.com/yourusername/apex-bot${NC}"
echo -e "${PURPLE}💬 Support: https://discord.gg/apex-bot${NC}"
echo -e ""
echo -e "${YELLOW}⚠️  For authorized security testing only${NC}"