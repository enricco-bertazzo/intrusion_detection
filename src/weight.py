import pandas as pd
from functions import add_weight, save, apply_multi

LLC = pd.read_csv('./Public/Protocol/LLC.csv')
CDP = pd.read_csv('./Public/Protocol/CDP.csv')
RIPV2 = pd.read_csv('./Public/Protocol/RIPv2.csv')
LOOP = pd.read_csv('./Public/Protocol/LOOP.csv')
NTP = pd.read_csv('./Public/Protocol/NTP.csv')
DNS = pd.read_csv('./Public/Protocol/DNS.csv')
TCP = pd.read_csv('./Public/Protocol/TCP.csv')
FINGER = pd.read_csv('./Public/Protocol/FINGER.csv')
SMTP = pd.read_csv('./Public/Protocol/SMTP.csv')
SMTP_IMF = pd.read_csv('./Public/Protocol/SMTP_IMF.csv')
ARP = pd.read_csv('./Public/Protocol/ARP.csv')
ICMP = pd.read_csv('./Public/Protocol/ICMP.csv')
IRC = pd.read_csv('./Public/Protocol/IRC.csv')
HTTP = pd.read_csv('./Public/Protocol/HTTP.csv')
FTP = pd.read_csv('./Public/Protocol/FTP.csv')
FTP_DATA = pd.read_csv('./Public/Protocol/FTP_DATA.csv')
SNMP = pd.read_csv('./Public/Protocol/SNMP.csv')
LLAP = pd.read_csv('./Public/Protocol/LLAP.csv')
TELNET = pd.read_csv('./Public/Protocol/TELNET.csv')
TIME = pd.read_csv('./Public/Protocol/TIME.csv')
SSHV1 = pd.read_csv('./Public/Protocol/SSHv1.csv')
POP = pd.read_csv('./Public/Protocol/POP.csv')
NBNS = pd.read_csv('./Public/Protocol/NBNS.csv')
SMTP_IMF_IMF = pd.read_csv('./Public/Protocol/SMTP_IMF_IMF.csv')
GTP = pd.read_csv('./Public/Protocol/GTP.csv')
TPM = pd.read_csv('./Public/Protocol/TPM.csv')

add_weight(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP,
           FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM)
apply_multi(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC,
            HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM)
save(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP,
     FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM)
