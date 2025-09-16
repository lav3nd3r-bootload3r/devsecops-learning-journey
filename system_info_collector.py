#!/usr/bin/env python3
"""
system information collector
A basic security audit script for gathering system information
Perfect for compliance documentation and security assessments
"""

import os
import platform
import socket
from datetime import datetime

def collect_system_info():
    """ Collect basic system information for security documentation """
    print ("""=== SYSTEM SECURITY AUDIT ===""")
    print (f"audit date: {datetime.now().strftime('%y-%m-%d %H:%M:%S')}")
    print("-" *40)
    
    #system information
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Python Version: {platform.python_version()}")
    #Current User Information
    print(f"Current User: {os.getenv('USER', 'Unknown')}")
    print(f"Working Directory: {os.getcwd()}")

    print("-" *40)
    print("Audit completed successfully!")


if __name__ == "__main__":
    collect_system_info()

#allyourbasearebelongtosus

