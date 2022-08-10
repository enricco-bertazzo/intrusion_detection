import pandas as pd

from functions import share_protocol, save

LLC = []
CDP = []
RIPV2 = []
LOOP = []
NTP = []
DNS = []
TCP = []
FINGER = []
SMTP = []
SMTP_IMF = []
ARP = []
ICMP = []
IRC = []
HTTP = []
FTP = []
FTP_DATA = []
SNMP = []
LLAP = []
TELNET = []
TIME = []
SSHV1 = []
POP = []
NBNS = []
SMTP_IMF_IMF = []
GTP = []
TPM = []


main_data = pd.read_csv('./Public/outside_monday.csv')
pd.DataFrame(main_data)

main_data = main_data.drop(columns=['No.', 'Info'])
main_data.insert(5, 'Weight', 'number')

share_protocol(main_data, LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM)

save(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM)