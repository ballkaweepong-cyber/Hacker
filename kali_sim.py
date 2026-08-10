#!/usr/bin/env python3
"""
kali_sim.py
-----------
App จำลองสไตล์ Kali Linux สำหรับ Termux
*** ทุกฟังก์ชันเป็นการจำลองล้วน ๆ ไม่มีการโจมตีหรือเชื่อมต่อจริงใด ๆ ***

รันใน Termux: python kali_sim.py
"""

import random
import sys
import time
import os

# สี
R  = "\033[91m"   # แดง
G  = "\033[92m"   # เขียว
Y  = "\033[93m"   # เหลือง
C  = "\033[96m"   # ฟ้าไซแอน
B  = "\033[94m"   # น้ำเงิน
W  = "\033[97m"   # ขาว
D  = "\033[90m"   # เทาเข้ม
RST = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("clear")

def slow(text, delay=0.012, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RST)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sleep(ms):
    time.sleep(ms / 1000)

def progress(label, ms=2000, color=G):
    steps = 40
    for i in range(steps + 1):
        pct = int(i / steps * 100)
        filled = int(30 * i / steps)
        bar = "█" * filled + "░" * (30 - filled)
        sys.stdout.write(f"\r{D}[{RST}{color}{bar}{RST}{D}]{RST} {label} {pct}%")
        sys.stdout.flush()
        time.sleep((ms / 1000) / steps)
    print()

# ===== BOOT =====
def boot():
    clear()
    lines = [
        (f"{D}[    0.000000] kali-sim kernel loading...{RST}", 0.04),
        (f"{D}[    0.041203] mounting /dev/sim0 as read-only{RST}", 0.04),
        (f"{D}[    0.198441] loading network simulation modules{RST}", 0.04),
        (f"{Y}[    0.412009] WARNING: this is a simulation — no real attack occurs{RST}", 0.04),
        (f"{G}[    0.812233] kali-sim ready{RST}", 0.04),
    ]
    for text, delay in lines:
        print(text)
        time.sleep(delay)
    time.sleep(0.4)

# ===== BANNER =====
BANNER = f"""{C}{BOLD}
  ██╗  ██╗ █████╗ ██╗     ██╗    ███████╗██╗███╗   ███╗
  ██║ ██╔╝██╔══██╗██║     ██║    ██╔════╝██║████╗ ████║
  █████╔╝ ███████║██║     ██║    ███████╗██║██╔████╔██║
  ██╔═██╗ ██╔══██║██║     ██║    ╚════██║██║██║╚██╔╝██║
  ██║  ██╗██║  ██║███████╗██║    ███████║██║██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚═╝     ╚═╝
{RST}"""

def show_banner():
    clear()
    print(BANNER)
    print(f"  {D}┌{'─'*50}┐{RST}")
    print(f"  {D}│{RST}  {C}Kali Simulator v1.0{RST} {D}//  simulation only{RST}  {D}│{RST}")
    print(f"  {D}└{'─'*50}┘{RST}")
    print()

# ===== MENU =====
def main_menu():
    print(f"  {W}{BOLD}MAIN MENU{RST}")
    print(f"  {D}{'─'*38}{RST}")
    print(f"  {C}[1]{RST} Information Gathering  {D}(จำลอง){RST}")
    print(f"  {C}[2]{RST} Network Scanner        {D}(จำลอง){RST}")
    print(f"  {C}[3]{RST} Password Analyzer      {D}(จำลอง){RST}")
    print(f"  {C}[4]{RST} Exploit Finder         {D}(จำลอง){RST}")
    print(f"  {C}[5]{RST} System Monitor Live    {D}(จำลอง){RST}")
    print(f"  {C}[6]{RST} Log Viewer             {D}(จำลอง){RST}")
    print(f"  {R}[0]{RST} ออกจากโปรแกรม")
    print()
    print(f"  {D}┌──(kali㉿sim)-[~]{RST}")
    return input(f"  {D}└─${RST} ").strip()

# ===== MODULES =====

def info_gather():
    target = input(f"\n  {C}[?]{RST} ระบุ target (จำลอง, อะไรก็ได้): ").strip() or "target.example"
    print()
    slow(f"  [*] เริ่ม information gathering: {target}", color=D)
    progress("resolving DNS", 1200, C)
    progress("scanning ports", 1800, G)
    results = [
        f"  {G}[+]{RST} IP จำลอง       : 192.168.{random.randint(0,255)}.{random.randint(1,254)}",
        f"  {G}[+]{RST} OS จำลอง       : Linux Ubuntu 22.04",
        f"  {G}[+]{RST} Open ports      : 22, 80, 443, 8080",
        f"  {G}[+]{RST} Web server      : nginx/1.24 (simulated)",
        f"  {Y}[!]{RST} หมายเหตุ        : ข้อมูลทั้งหมดเป็นข้อมูลสุ่มจำลอง",
    ]
    print()
    for r in results:
        print(r)
        time.sleep(0.25)

def network_scan():
    print()
    slow("  [*] เริ่มจำลอง network scan...", color=D)
    progress("scanning subnet", 2000, C)
    hosts = [
        ("192.168.1.1",   "router",   "online"),
        ("192.168.1.5",   "desktop",  "online"),
        ("192.168.1.12",  "phone",    "online"),
        ("192.168.1.20",  "laptop",   "filtered"),
        ("192.168.1.99",  "unknown",  "timeout"),
    ]
    print(f"\n  {W}{'IP':<18}{'TYPE':<12}{'STATUS'}{RST}")
    print(f"  {D}{'─'*38}{RST}")
    for ip, typ, status in hosts:
        color = G if status=="online" else (Y if status=="filtered" else D)
        print(f"  {ip:<18}{typ:<12}{color}{status}{RST}")
        time.sleep(0.3)
    print(f"\n  {D}สแกนจำลองเสร็จสิ้น — ข้อมูลทั้งหมดสมมติ{RST}")

def password_analyzer():
    pwd = input(f"\n  {C}[?]{RST} ใส่รหัสผ่านที่อยากทดสอบ: ")
    print()
    slow("  [*] วิเคราะห์ความแข็งแรง...", color=D)
    progress("analyzing", 1500, Y)
    score = 0
    tips = []
    if len(pwd) >= 8:  score += 25
    else: tips.append("ความยาวน้อยกว่า 8 ตัว — ควรเพิ่ม")
    if any(c.isupper() for c in pwd): score += 25
    else: tips.append("ไม่มีตัวพิมพ์ใหญ่ — ควรเพิ่ม")
    if any(c.isdigit() for c in pwd): score += 25
    else: tips.append("ไม่มีตัวเลข — ควรเพิ่ม")
    if any(c in "!@#$%^&*" for c in pwd): score += 25
    else: tips.append("ไม่มีอักขระพิเศษ — ควรเพิ่ม")
    color = G if score >= 75 else (Y if score >= 50 else R)
    print(f"  {color}คะแนนความแข็งแรง: {score}/100{RST}")
    for t in tips:
        print(f"  {D}• {t}{RST}")

def exploit_finder():
    svc = input(f"\n  {C}[?]{RST} ระบุ service (เช่น openssh, nginx): ").strip() or "openssh"
    print()
    slow(f"  [*] ค้นหา CVE จำลองสำหรับ: {svc}", color=D)
    progress("searching exploit-db (simulated)", 1800, R)
    fake_cves = [
        ("CVE-2024-XXXX", svc, "Remote Code Execution (จำลอง)"),
        ("CVE-2023-YYYY", svc, "Privilege Escalation (จำลอง)"),
    ]
    print()
    for cve, svc_name, desc in fake_cves:
        print(f"  {R}{cve}{RST}  {svc_name}  {D}{desc}{RST}")
        time.sleep(0.3)
    print(f"\n  {Y}[!] CVE ทั้งหมดเป็นข้อมูลสมมติเพื่อการจำลองเท่านั้น{RST}")

def system_monitor():
    print()
    slow("  [*] เปิด system monitor จำลอง (กด Ctrl+C เพื่อหยุด)...", color=D)
    time.sleep(0.5)
    try:
        for tick in range(99):
            clear()
            print(BANNER)
            print(f"  {W}{BOLD}SYSTEM MONITOR — SIMULATED{RST}  {D}(Ctrl+C หยุด){RST}\n")
            cpu = random.randint(10, 90)
            mem = random.randint(20, 80)
            net = random.randint(5, 100)
            for label, val, color in [("CPU", cpu, C), ("MEM", mem, Y), ("NET", net, G)]:
                bar = "█" * int(30 * val / 100) + "░" * (30 - int(30 * val / 100))
                print(f"  {label}  {color}{bar}{RST} {val}%")
            print(f"\n  {D}processes (simulated):{RST}")
            procs = ["kali-sim", "python3", "bash", "sshd(sim)", "nginx(sim)"]
            for p in procs:
                print(f"  {D}• {p:<15} PID:{random.randint(100,9999)}{RST}")
            time.sleep(1.0)
    except KeyboardInterrupt:
        print(f"\n  {R}[!] ปิด monitor{RST}")

def log_viewer():
    print()
    slow("  [*] กำลังโหลด log จำลอง...", color=D)
    time.sleep(0.5)
    logs = [
        (G, "INFO",  "session started — user: sim_user"),
        (C, "INFO",  "network interface up (simulated)"),
        (Y, "WARN",  "connection attempt from 10.0.0.1 (simulated)"),
        (G, "INFO",  "port scan completed — 5 hosts found"),
        (Y, "WARN",  "weak password detected on service (simulated)"),
        (G, "INFO",  "report generated successfully"),
        (D, "DEBUG", "cache cleared"),
    ]
    print()
    for color, level, msg in logs:
        ts = time.strftime("%H:%M:%S")
        print(f"  {D}[{ts}]{RST} {color}[{level}]{RST} {msg}")
        time.sleep(0.3)

# ===== MAIN =====
def main():
    boot()
    while True:
        show_banner()
        choice = main_menu()
        if choice == "1":
            info_gather()
        elif choice == "2":
            network_scan()
        elif choice == "3":
            password_analyzer()
        elif choice == "4":
            exploit_finder()
        elif choice == "5":
            system_monitor()
        elif choice == "6":
            log_viewer()
        elif choice == "0":
            slow("\n  ออกจากโปรแกรม...", color=D)
            break
        else:
            print(f"\n  {R}เลือกไม่ถูกต้อง{RST}")
            time.sleep(0.8)
            continue
        print()
        input(f"  {D}กด Enter เพื่อกลับเมนู...{RST}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {R}[!] ออกโดย Ctrl+C{RST}\n")
