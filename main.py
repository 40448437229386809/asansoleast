import time
import sys
import urllib.request
import urllib.parse
import urllib.error
import re
import os
import random
import string
from datetime import datetime

# Advanced Terminal Colors
C_RED = '\033[38;5;196m'
C_GREEN = '\033[38;5;46m'
C_DARK_GREEN = '\033[38;5;22m'
C_YELLOW = '\033[38;5;226m'
C_BLUE = '\033[38;5;39m'
C_CYAN = '\033[38;5;51m'
C_WHITE = '\033[38;5;231m'
C_GRAY = '\033[38;5;240m'
C_PURPLE = '\033[38;5;135m'
RESET = '\033[0m'

# Current folder path automatic nikalne ke liye
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def slow_print(text, speed=0.02):
    """Terminal par text ko ek-ek letter karke type karne ka effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def hex_dump_stream(lines=25):
    """Memory address aur hex code ka fast Hollywood matrix scroll"""
    for _ in range(lines):
        address = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
        hex_data = " ".join([f"{random.randint(0, 255):02X}" for _ in range(8)])
        ascii_chars = "".join([random.choice(string.ascii_letters + string.digits + "....") for _ in range(8)])
        print(f"{C_DARK_GREEN}{address}  {hex_data}  |{ascii_chars}|{RESET}")
        time.sleep(random.uniform(0.005, 0.015))

def horizontal_ls_matrix_scroll(duration_seconds):
    """ls command dene par hex code left-to-right aur ultra-fast run karega"""
    start_time = time.time()
    try:
        while time.time() - start_time < duration_seconds:
            address = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
            hex_data = " ".join([f"{random.randint(0, 255):02X}" for _ in range(8)])
            ascii_chars = "".join([random.choice(string.ascii_letters + string.digits + "._-$@#") for _ in range(8)])
            line_stream = f"{C_DARK_GREEN}{address}  {hex_data}  |{ascii_chars}|  "
            
            sys.stdout.write(line_stream)
            sys.stdout.flush()
            if random.randint(1, 4) == 4:
                sys.stdout.write("\n")
            time.sleep(random.uniform(0.001, 0.008))
            
        print(f"\n{C_GREEN}[+] DATA STREAM OVERFLOW SOLVED. INDEX BUFFER SYNCHRONIZED.{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Matrix scanning paused by terminal operator.{RESET}\n")

def server_hacked_blink_animation(blinks=3):
    """Bada sa 'SERVER HACKED' text jo 1-1 second ke interval par blink karega"""
    hacked_text = f"""
{C_RED} ██████╗███████╗██████╗ ██╗   ██╗███████╗██████╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
╚█████╗ █████╗  ██████╔╝██║   ██║█████╗  ██████╔╝     ███████║███████║██║     █████╔╝ █████╗  ██╔══██╗
 ╚═══██╗██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║
██████╔╝███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝
╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝{RESET}
    """
    for _ in range(blinks):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n" + hacked_text)
        time.sleep(1.0)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1.0)

def kali_rainbow_get_scroll(duration_seconds):
    """get command par multicolored big size @kali codes waterfall scroll honge"""
    start_time = time.time()
    colors = [C_RED, C_WHITE, C_BLUE, C_YELLOW, C_GREEN]
    
    kali_templates = [
        " ☠️  [ @kali @kali @kali ] ☠️ ",
        " ===> !! @kali_injection_matrix !! <===",
        " [ CRITICAL_NODE: @kali ] -- BUFFER_OVERFLOW",
        " ☢️  STAGER_LOADED: @kali @kali @kali ☢️ ",
        " >>> CORE_BYPASS_ENABLED_FOR_@kali <<<"
    ]
    
    try:
        while time.time() - start_time < duration_seconds:
            chosen_color = random.choice(colors)
            base_text = random.choice(kali_templates)
            
            hex_part1 = f"0x{random.randint(0x1000, 0xFFFF):04X}::{random.randint(10,99)}"
            hex_part2 = "".join(random.choices(string.hexdigits.upper(), k=12))
            
            row_stream = f"{chosen_color}[{hex_part1}]  {base_text}  [{hex_part2}]{RESET}"
            print(row_stream)
            time.sleep(random.uniform(0.002, 0.015))
            
    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Rainbow cascade stream interrupted by admin.{RESET}\n")

def masterclass_hacking_scroll(duration_seconds):
    """Target set hone par endless software aur exploits logs cascade view"""
    start_time = time.time()
    log_templates = [
        lambda: f"{C_CYAN}[NMAP] Scanning target TCP/UDP ports... Stealth mode enabled.{RESET}",
        lambda: f"{C_RED}[EXPLOIT] Injecting reverse_tcp meterpreter stager into memory buffer...{RESET}",
        lambda: f"{C_YELLOW}[BRUTEFORCE] Trying credentials payload line: admin:{''.join(random.choices(string.ascii_lowercase, k=6))}{RESET}",
        lambda: f"{C_PURPLE}[SQLMap] Testing injection vector 'id' -> Parameter looks exploitable (DBMS: MySQL){RESET}",
        lambda: f"{C_BLUE}[METASPLOIT] Payload handler bound to local interface tunnel at port {random.randint(1024,65535)}{RESET}",
        lambda: f"{C_GREEN}[CVE-{random.randint(2018,2026)}-{random.randint(1000,9999)}] Vulnerability stack matched! Executing remote code execution (RCE).{RESET}",
        lambda: f"{C_WHITE}[PACKET] INBOUND TCP_FLAG_SYN from {random.randint(1,255)}.{random.randint(1,255)}.0.1 -> Packet Size: {random.randint(64,1500)} bytes{RESET}",
        lambda: f"{C_DARK_GREEN}0x{random.randint(0x10000000, 0xFFFFFFFF):08X}  " + " ".join([f"{random.randint(0, 255):02X}" for _ in range(8)]) + f"  |{''.join(random.choices(string.ascii_letters + string.digits, k=8))}|{RESET}"
    ]
    try:
        while time.time() - start_time < duration_seconds:
            log_line = random.choice(log_templates)()
            print(log_line)
            time.sleep(random.uniform(0.001, 0.012))
    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Hacking stream bypass triggered by user.{RESET}")

def fake_hash_crack():
    """System me ghusne ka fake RSA decryption animation"""
    slow_print(f"{C_BLUE}[*] Overriding Kali Firewall Protocols...{RESET}", 0.01)
    target_hash = "KALI-NODE-9X21"
    for i in range(20):
        random_hash = "".join(random.choices(string.hexdigits.upper(), k=14))
        sys.stdout.write(f"\r{C_RED}[~] BYPASSING SECURITY LAYER: {random_hash}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{C_GREEN}[+] WORKSTATION ACCESS:      {target_hash}{RESET}    \n")
    sys.stdout.flush()
    time.sleep(0.4)

def pro_banner():
    """Kali Workstation Banner with Massive Animated Blinking Red Human Eyes & Big Red Title"""
    open_eyes = f"""
{C_RED}      _.---**""**---._                 _.---**""**---._
{C_RED}   .-'                '-.           .-'                '-.
{C_RED} .'                      `.       .'                      `.
{C_RED}/         {C_WHITE}.-""""-.{C_RED}         \\     /         {C_WHITE}.-""""-.{C_RED}         \\ 
{C_RED}|        {C_WHITE}/  {C_RED}██{C_WHITE}  \\{C_RED}        |   |        {C_WHITE}/  {C_RED}██{C_WHITE}  \\{C_RED}        |
{C_RED}|        {C_WHITE}|  {C_RED}██{C_WHITE}  |{C_RED}        |   |        {C_WHITE}|  {C_RED}██{C_WHITE}  |{C_RED}        |
{C_RED}\\         {C_WHITE}'-....-'{C_RED}         /     \\         {C_WHITE}'-....-'{C_RED}         /
{C_RED} `._                    _.'       `._                    _.'
{C_RED}    `--..,,______,,..--'             `--..,,______,,..--'{RESET}"""

    closed_eyes = f"""
{C_RED}      _.---**""**---._                 _.---**""**---._
{C_RED}   .-'                '-.           .-'                '-.
{C_RED} .'                      `.       .'                      `.
{C_RED}/                          \\     /                          \\ 
{C_RED}|                          |   |                          |
{C_RED}============================     ============================
{C_RED}\\                          /     \\                          /
{C_RED} `._                    _.'       `._                    _.'
{C_RED}    `--..,,______,,..--'             `--..,,______,,..--'{RESET}"""
    
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(open_eyes)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(closed_eyes)
        time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = f"""{open_eyes}
{C_RED} ██╗  ██╗ █████╗ ██╗     ██╗    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗   ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
 ██║  ██║██╔══██╗██║     ██║    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝   ██║    ██║██╔══██╗██╔══██╗██║  ██║██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗  ██║
 █████═╝ ███████║██║     ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝    ██║ █╗ ██║██║  ██║██████╔╝███████║███████╗   ██║   ███████║   ██║   ██║██║  ██║██╔██╗ ██║
 ██╔═██╗ ██╔══██║██║     ██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗    ██║███╗██║██║  ██║██╔══██╗██╔══██║╚════██║   ██║   ██╔══██║   ██║   ██║██║  ██║██║╚██╗██║
 ██║  ██╗██║  ██║███████╗██║    ███████╗██║██║ ╚████║╚██████╔╝██║  ██╗   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██║███████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{RESET}

 {C_GRAY}============================================================================================================================================================={RESET}
 {C_PURPLE} [ WORKSTATION: SECURE ] {C_GRAY}|{C_PURPLE} [ SHELL: KALI-ROOT ] {C_GRAY}|{C_PURPLE} [ PARSER: DYNAMIC HTTP ] {C_GRAY}|{C_PURPLE} [ MATRIX OVERLAY: ACTIVE ] {RESET}
 {C_GRAY}============================================================================================================================================================={RESET}
    """
    print(banner)

def get_files(url):
    """HTTP HTML Parse Method"""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            final_url = response.geturl()
            html = response.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href=["\'](.*?)["\']', html)
        clean_files = [urllib.parse.unquote(l) for l in links if not l.startswith('?') and l != '/' and not l.startswith('http')]
        return [f for f in clean_files if f not in ['../', '..']], final_url
    except Exception:
        return None, url

def advanced_download_animation(filename):
    """Download hone par packet extraction aur progress bar"""
    print(f"\n{C_PURPLE}[*] INTERCEPTING NODE STREAM: {filename}{RESET}")
    time.sleep(0.1)
    
    hex_dump_stream(15)
    
    print(f"{C_YELLOW}[~] DECRYPTING BINARY CHUNKS...{RESET}")
    bar_length = 50
    for i in range(101):
        time.sleep(0.005)
        filled_len = int(bar_length * i // 100)
        bar = '█' * filled_len + '-' * (bar_length - filled_len)
        sys.stdout.write(f'\r{C_CYAN}[{bar}] {i}%{RESET}')
        sys.stdout.flush()
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # --- MASTERCLASS HOLLYWOOD BOOT SEQUENCE ---
    hex_dump_stream(40)
    fake_hash_crack()
    pro_banner()
    
    # --- SETUP TARGET ---
    slow_print(f"{C_GRAY}[i] Enter remote Kali target or HTTP server address.{RESET}", 0.01)
    target_input = input(f"{C_RED}kali{C_WHITE}@{C_CYAN}workstation{C_WHITE}:~# {C_CYAN}set TARGET {C_WHITE}").strip()
    
    if not target_input:
        target_input = "http://192.0.0.8:8080/files"
        print(f"{C_GRAY}[*] Defaulting to active path: {target_input}{RESET}")
    
    url = target_input if target_input.startswith("http") else "http://" + target_input
    
    random_scroll_duration = random.randint(20, 40)
    print()
    slow_print(f"{C_RED}[!] SECURITY ALARM: DETECTING NETWORK ARCHITECTURE...{RESET}", 0.01)
    slow_print(f"{C_YELLOW}[*] EXECUTING EXPLOIT PIPELINE MODULES ({random_scroll_duration} SECONDS STRESS SCROLL)...{RESET}", 0.01)
    time.sleep(1.5)
    
    masterclass_hacking_scroll(random_scroll_duration)
    
    print()
    slow_print(f"{C_BLUE}[*] Synchronizing TCP handshake with workstation...{RESET}", 0.02)
    time.sleep(0.3)
    
    # --- CONNECTION CHECK ---
    files, final_url = get_files(url)
    if files is None:
        slow_print(f"{C_RED}[─] FATAL ERROR: Station offline or Kali firewall dropped request.{RESET}", 0.02)
        return

    slow_print(f"{C_GREEN}[+] ESTABLISHED LINK. Local network logs bypassed securely.{RESET}", 0.02)
    print(f"{C_GREEN}[+] Kali Root session spawned at {final_url}{RESET}\n")

    # --- MAIN SHELL ---
    while True:
        try:
            print(f"{C_BLUE}╭──[{C_RED}root⚡kali{C_BLUE}]──[{C_CYAN}{final_url}{C_BLUE}]{RESET}")
            cmd_input = input(f"{C_BLUE}╰─➤ {C_WHITE}").strip().split()
            
            if not cmd_input:
                continue
                
            cmd = cmd_input[0].lower()
            args = " ".join(cmd_input[1:])

            if cmd in ["exit", "quit", "disconnect"]:
                hex_dump_stream(15)
                print(f"\n{C_RED}[*] Clearing session logs...{RESET}")
                time.sleep(0.3)
                print(f"{C_RED}[*] Station disconnected safely.{RESET}")
                break
                
            elif cmd == "help":
                hex_dump_stream(10)
                print(f"\n{C_GRAY}================ KALI WORKSTATION MENU ================{RESET}")
                print(f"  {C_CYAN}ls{RESET}            : Scan remote file nodes (Matrix -> Server Hacked Blink -> Show Files)")
                print(f"  {C_CYAN}get <file>{RESET}    : Securely download a single file node (Rainbow Matrix)")
                print(f"  {C_CYAN}getall{RESET}        : [NEW] Securely download ALL files from the folder at once!")
                print(f"  {C_CYAN}clear{RESET}         : Refresh workstation terminal (Triggers Matrix)")
                print(f"  {C_CYAN}exit{RESET}          : Close terminal pipeline")
                print(f"{C_GRAY}======================================================{RESET}\n")
                
            elif cmd in ["ls", "dir"]:
                random_ls_duration = random.randint(30, 60)
                print(f"{C_PURPLE}[*] Decoding network inodes... Executing horizontal hex stream matrix ({random_ls_duration} Seconds)...{RESET}")
                time.sleep(1.0)
                
                horizontal_ls_matrix_scroll(random_ls_duration)
                server_hacked_blink_animation(blinks=3)
                pro_banner()
                
                print(f"{C_PURPLE}[*] Mapping target file nodes...{RESET}")
                current_files, final_url = get_files(url)
                if current_files:
                    print(f"\n{C_WHITE}INODE      PERMISSIONS   SIZE    FILENAME{RESET}")
                    print(f"{C_GRAY}--------------------------------------------------{RESET}")
                    for f in current_files:
                        fake_inode = random.randint(100000, 999999)
                        fake_size = f"{random.randint(1, 999)}MB" if '.' in f else "4.0KB"
                        perm = "-rw-r--r--" if '.' in f else "drwxr-xr-x"
                        color = C_WHITE if '.' in f else C_CYAN
                        time.sleep(0.01)
                        print(f"{C_DARK_GREEN}{fake_inode}{RESET}     {C_GRAY}{perm}{RESET}    {C_YELLOW}{fake_size:<5}{RESET}   {color}{f}{RESET}")
                else:
                    print(f"{C_RED}[!] Directory tree returned 0 nodes.{RESET}")
                print()
                
            elif cmd in ["download", "get"]:
                if not args:
                    print(f"{C_RED}[!] Command Error: Specify file node to download.{RESET}\n")
                    continue
                    
                current_files, final_url = get_files(url)
                if current_files and args in current_files:
                    quoted_args = urllib.parse.quote(args, safe='/')
                    file_url = urllib.parse.urljoin(final_url, quoted_args)
                    
                    base_filename = os.path.basename(args)
                    if not base_filename:
                        base_filename = "downloaded_file.bin"
                    
                    full_download_path = os.path.join(SCRIPT_DIR, base_filename)
                    
                    random_get_duration = random.randint(10, 40)
                    print(f"\n{C_YELLOW}[*] OVERLOADING FILE DATA INTERFACE... INJECTING STREAM CORRUPTOR ({random_get_duration} SECONDS)...{RESET}")
                    time.sleep(1.2)
                    
                    kali_rainbow_get_scroll(random_get_duration)
                    advanced_download_animation(args)
                    
                    try:
                        req = urllib.request.Request(file_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, timeout=15) as response, open(full_download_path, 'wb') as out_file:
                            chunk_size = 8192
                            while True:
                                chunk = response.read(chunk_size)
                                if not chunk:
                                    break
                                out_file.write(chunk)
                        slow_print(f"{C_GREEN}[+] SECURED: File locally saved inside main.py folder: {base_filename}{RESET}\n", 0.01)
                    except urllib.error.HTTPError as e:
                         print(f"\n{C_RED}[!] STATION ERROR: {e.code} - {e.reason}. Link rejected.{RESET}\n")
                    except Exception as e:
                        print(f"\n{C_RED}[!] CAPTURE FAILED: {e}{RESET}\n")
                else:
                    print(f"{C_RED}[─] ERROR: Remote node '{args}' not found on server.{RESET}\n")

            # FIX: Naya Command poor folder ki sabhi files ek sath download karne ke liye
            elif cmd in ["getall", "get-all", "downloadall"]:
                current_files, final_url = get_files(url)
                if not current_files:
                    print(f"{C_RED}[!] Error: Remote folder empty hai ya link unresponsive hai.{RESET}\n")
                    continue
                
                print(f"\n{C_RED}[⚡] TOTAL NODES DETECTED: {len(current_files)} files. INITIALIZING MASSIVE BULK EXTRACTOR...{RESET}\n")
                time.sleep(2.0)
                
                for index, f in enumerate(current_files, 1):
                    # Folder/Directory links ko skip karne ke liye safetynet
                    if not '.' in f:
                        continue
                        
                    quoted_args = urllib.parse.quote(f, safe='/')
                    file_url = urllib.parse.urljoin(final_url, quoted_args)
                    
                    base_filename = os.path.basename(f)
                    full_download_path = os.path.join(SCRIPT_DIR, base_filename)
                    
                    # Har file par matrix burst chalega (3 se 7 seconds ka fast cascade burst)
                    random_get_duration = random.randint(3, 7)
                    print(f"\n{C_PURPLE}[QUEUE: {index}/{len(current_files)}] INJECTING PAYLOAD ON: {base_filename} ({random_get_duration} Sec Burst)...{RESET}")
                    time.sleep(0.5)
                    
                    # Rainbow cascade trigger
                    kali_rainbow_get_scroll(random_get_duration)
                    
                    # Standard Progress bar animation
                    advanced_download_animation(f)
                    
                    # Core batch chunk downloader
                    try:
                        req = urllib.request.Request(file_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, timeout=15) as response, open(full_download_path, 'wb') as out_file:
                            chunk_size = 8192
                            while True:
                                chunk = response.read(chunk_size)
                                if not chunk:
                                    break
                                out_file.write(chunk)
                        print(f"{C_GREEN}[+] DOWNLOADED: '{base_filename}' successfully dumped into main.py folder!{RESET}\n")
                    except Exception as e:
                        print(f"{C_RED}[!] BULK ERROR ON '{base_filename}': {e}. Skipping to next file.{RESET}\n")
                
                print(f"{C_GREEN}==============================================================================={RESET}")
                slow_print(f"{C_GREEN}[+++] ALL PAYLOADS SECURED: Pure folder ka safe local dump complete ho gaya!{RESET}\n", 0.01)
                print(f"{C_GREEN}==============================================================================={RESET}\n")
                    
            elif cmd in ["clear", "cls"]:
                hex_dump_stream(25)
                pro_banner()
                
            else:
                print(f"{C_RED}[!] {cmd}: Command bypassed/unsupported by workstation.{RESET}\n")
                
        except KeyboardInterrupt:
            print(f"\n\n{C_RED}[!] EMERGENCY SYSTEM COOLDOWN INITIATED. Exiting...{RESET}")
            break
        except Exception as e:
            print(f"\n{C_RED}[!] WORKSTATION KERNEL ERROR: {e}{RESET}")
            break

if __name__ == "__main__":
    main()