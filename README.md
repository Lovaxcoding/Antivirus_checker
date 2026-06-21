# Antivirus Checker 🛡️

Un petit script léger conçu pour les environnements de laboratoire (Lab/Pentest) permettant de détecter rapidement la présence de solutions antivirus et de logiciels de sécurité actifs sur un système.

Initialement développé en C#, ce projet propose des alternatives modernes en **Python** adaptées pour des audits locaux ou distants.

---

## 🚀 Fonctionnalités

*   **Mode Local (Windows) :** Interroge l'infrastructure WMI locale pour lister les processus et les comparer à une base de données d'antivirus connus (Defender, Kaspersky, Norton, etc.).
*   **Mode Distant (Pentest/Lab) :** Permet d'auditer une machine Windows cible à distance depuis une machine d'attaque (comme Kali Linux) via le protocole WMI avec la bibliothèque `impacket`.
*   **Mode Local (Linux) :** Option secondaire pour identifier les démons de sécurité courants sous Linux (ClamAV, Auditd, Falcon Sensor...).

---

## 📋 Prérequis

Pour la version Python distante (depuis Kali Linux) :
```bash
pip install impacket
```
Pour la version utilisant psutil (alternative locale) :

```bash
pip install psutil
```
💻 Utilisation
1. Audit distant (Depuis Kali Linux)

Pour scanner une machine Windows cible dans ton Lab :

```bash
python3 av_checker.py <Target_IP> <Username> <Password>
```
2. Audit local (Windows)

Exécute simplement le script sur la machine cible :
```bash

python av_checker.py
```
🔍 Liste des signatures supportées

Le script recherche activement les processus des solutions suivantes :

    Windows Defender (MsMpEng.exe)

    Kaspersky (avp.exe)

    Norton Security (NortonSecurity.exe)

    Avast / AVG / Bitdefender / ESET ...

⚠️ Avertissement (Disclaimer)

Ce script est partagé uniquement à des fins éducatives et de recherche en sécurité dans le cadre de laboratoires contrôlés. L'auteur n'est pas responsable d'une utilisation abusive ou hors du cadre légal.
