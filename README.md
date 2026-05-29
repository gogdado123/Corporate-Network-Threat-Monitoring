> 📄 **Academic Research Document:** This core architecture operates in direct synchronization with our comprehensive 5-chapter engineering report. For detailed system design topologies, analysis breakdowns, and rule configurations, access the [Full Project Report Document](https://docs.google.com/document/d/1GCoj764vZ-FgKQCud4WzOSliY9a-9AVZCV2OiMKLqlM/edit?usp=sharing).

# Corporate Network Threat Monitoring System (SIEM Implementation)

A security infrastructure project demonstrating the integration of **Wazuh SIEM** and **OPNsense Firewall** within a sandboxed virtual environment (VMware Workstation) to monitor, detect, and analyze corporate network threats in real time.

## 🗺️ Network Topology & Architecture
The entire testing environment was safely isolated under a closed `Host-Only` network context (Sandbox) to contain attack vectors:
* **Wazuh SIEM Central Server:** 192.168.10.156 (Central Log Collector & Analytics Engine)
* **OPNsense Firewall Gateway:** 192.168.10.1 (Perimeter Security & Syslog Forwarder)
* **Attacker Node (Kali Linux):** 192.168.10.50 (Penetration & Simulation Endpoint)

## ⚙️ Core Security Mechanism
1. **Data Collection & Normalization:** OPNsense filters network traffic via Top-Down ACLs (Stateful Inspection) and forwards network event payloads via Remote Syslog over Port `514 UDP`. Wazuh decodes and normalizes raw packets via custom parsing templates (`ossec.conf`).
2. **Correlation Engine Decision:** Real-time log validation automatically escalates threat alerts based on conditional patterns (e.g., matching 5 rapid login failures or structural anomalies).
3. **Endpoint Security (Host-based HIDS):** Extended monitoring capabilities using Wazuh Agents on active endpoints to continuously run **Security Configuration Assessments (SCA)** and flag configuration vulnerabilities.

## 🎛️ Cyber Attack Simulation Lab
The pipeline utilizes an automated python test wrapper (`attack_simulation.py`) executing an aggressive, multi-parameter stealth port scan via Nmap to validate security alertness:
```bash
nmap -sS -p- -T4 -A -v 192.168.10.1
```
* **Results:** OPNsense intercepted and blocked the brute-force scanning packets via the `filterlog` sub-program, instantly transmitting alerts to the central Wazuh Dashboard for instant security analysis.
