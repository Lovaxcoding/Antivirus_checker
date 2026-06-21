import subprocess

def verifier_securite_linux():
    status = False
    print("[+] Security check running (Linux locale) .. ")
    
    # Processus de sécurité ou daemons typiques sous Linux
    linux_security = [
        "clamd", "freshclam", "auditd", "rkhunter", "lynis", 
        "fapolicyd", "ossec-syscheckd", "falcon-sensor"
    ]
    
    try:
        # Récupère la liste de tous les processus locaux (uniquement le nom)
        cmd = "ps -A -o comm="
        output = subprocess.check_output(cmd, shell=True, text=True)
        process_list = [line.strip() for line in output.splitlines() if line.strip()]
        
        for process in process_list:
            if process in linux_security:
                print(f"-- Security Software Found: {process}")
                status = True
                
        if not status:
            print("-- No common Linux security software found!")
            
    except Exception as e:
        print(f"[-] Erreur : {e}")

if __name__ == "__main__":
    verifier_securite_linux()
