import os
import subprocess

print("🔒 [INFO] Initiating Controlled Penetration Testing & Penetration Simulation...")
# กำหนด IP ปลายทางของ OPNsense Firewall ตามรายงานบทที่ 3
TARGET_IP = "192.168.10.1" 

# การสั่งรันคำสั่ง Nmap เชิงซ้อนผ่าน Python Subprocess ดักพารามิเตอร์ตามหน้า 10 ของเล่มรายงาน
# -sS: Stealth Scan, -p-: All 65535 Ports, -T4: Aggressive Speed, -A: OS/Service Detection
nmap_command = f"nmap -sS -p- -T4 -A -v {TARGET_IP}"

print(f"🚀 [ATTACK SIMULATION] Executing Command: {nmap_command}")
print("⏳ Scanning in progress... Triggering OPNsense Firewall rulesets.")

try:
    # คำสั่งสั่งให้ระบบเริ่มยิงทราฟฟิกทดสอบและเก็บบันทึกค่า
    result = subprocess.run(nmap_command, shell=True, check=True, text=True, capture_output=True)
    print("\n✅ [SUCCESS] Scanning finished. OPNsense should have forwarded logs to Wazuh SIEM.")
    print("--- Scan Output Preview ---")
    print(result.stdout[:500]) # แสดงตัวอย่างผลลัพธ์ 500 ตัวอักษรแรก
except FileNotFoundError:
    print("❌ [ERROR] Nmap is not installed on this local system context.")
except subprocess.CalledProcessError as e:
    print(f"❌ [ERROR] Command execution failed: {e}")
