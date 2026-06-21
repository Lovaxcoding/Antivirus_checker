import subprocess

def verifier_antivirus():
    status = False
    print("[+] Antivirus check is running .. ")
    
    # Liste des exécutables antivirus à rechercher
    av_check = [
        "MsMpEng.exe", "AdAwareService.exe", "afwServ.exe", "avguard.exe", "AVGSvc.exe", 
        "bdagent.exe", "BullGuardCore.exe", "ekrn.exe", "fshoster32.exe", "GDScan.exe", 
        "avp.exe", "K7CrvSvc.exe", "McAPExe.exe", "NortonSecurity.exe", "PavFnSvr.exe", 
        "SavService.exe", "EnterpriseService.exe", "WRSA.exe", "ZAPrivacyService.exe"
    ]
    
    try:
        # Exécute la commande WMIC pour obtenir la liste des processus (comme en C#)
        # On ignore la première ligne d'en-tête et les lignes vides
        cmd = "wmic process get name"
        output = subprocess.check_output(cmd, shell=True, text=True)
        process_list = [line.strip() for line in output.splitlines() if line.strip()]
        
        # Parcours et comparaison
        for process in process_list:
            # On vérifie si le processus fait partie de notre liste (insensible à la casse)
            if process in av_check:
                print(f"--AV Found: {process}")
                status = True
                
        if not status:
            print("--AV software is not found!")
            
    except Exception as e:
        print(f"[-] Erreur lors de la récupération des processus : {e}")

if __name__ == "__main__":
    verifier_antivirus()
