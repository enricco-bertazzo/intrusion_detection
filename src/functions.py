import pandas as pd

def share_protocol(main_data, LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):
    for i in range(0, len(main_data)):
        data = main_data.iloc[i, 3]
        if data == "LLC":
          LLC.append(main_data.iloc[i])
        elif data == "CDP":
          CDP.append(main_data.iloc[i])
        elif data == "RIPv2":
          RIPV2.append(main_data.iloc[i])
        elif data == "LOOP":
          LOOP.append(main_data.iloc[i])
        elif data == "NTP":
          NTP.append(main_data.iloc[i])
        elif data == "DNS":
          DNS.append(main_data.iloc[i])
        elif data == "TCP":
          TCP.append(main_data.iloc[i])
        elif data == "FINGER":
          FINGER.append(main_data.iloc[i])
        elif data == "SMTP":
          SMTP.append(main_data.iloc[i])
        elif data == "SMTP/IMF":
          SMTP_IMF.append(main_data.iloc[i])
        elif data == "ARP":
          ARP.append(main_data.iloc[i])
        elif data == "ICMP":
          ICMP.append(main_data.iloc[i])
        elif data == "IRC":
          IRC.append(main_data.iloc[i])
        elif data == "HTTP":
          HTTP.append(main_data.iloc[i])
        elif data == "FTP":
          FTP.append(main_data.iloc[i])
        elif data == "FTP-DATA":
          FTP_DATA.append(main_data.iloc[i])
        elif data == "SNMP":
          SNMP.append(main_data.iloc[i])
        elif data == "LLAP":
          LLAP.append(main_data.iloc[i])
        elif data == "TELNET":
          TELNET.append(main_data.iloc[i])
        elif data == "TIME":
          TIME.append(main_data.iloc[i])
        elif data == "SSHv1":
          SSHV1.append(main_data.iloc[i])
        elif data == "POP":
          POP.append(main_data.iloc[i])
        elif data == "NBNS":
          NBNS.append(main_data.iloc[i])
        elif data == "SMTP/IMF/IMF":
          SMTP_IMF_IMF.append(main_data.iloc[i])
        elif data == "GTP":
          GTP.append(main_data.iloc[i])
        elif data == "TPM":
          TPM.append(main_data.iloc[i])

def weight(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):

    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC', 'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']
    for i in protocol:
        
        if i == 'LLC':
            count = 0
            for j in range(0 , len(LLC)):
                LLC.iloc[j, 5] = count
                count += 1

        elif i == 'CDP':
            count = 0
            for j in range(0 , len(CDP)):
                CDP.iloc[j, 5] = count
                count += 1

        elif i == 'RIPV2':
            count = 0
            for j in range(0, len(RIPV2)):
                RIPV2.iloc[j, 5] = count
                count += 1
        
        elif i == 'LOOP':
            count = 0
            for j in range(0, len(LOOP)):
                LOOP.iloc[j, 5] = count
                count += 1
    
        elif i == 'NTP':
            count = 0
            for j in range(0, len(NTP)):
                NTP.iloc[j, 5] = count
                count += 1

        elif i == 'DNS':
            count = 0
            for j in range(0, len(DNS)):
                DNS.iloc[j, 5] = count
                count += 1

        elif i == 'TCP':
            count = 0
            for j in range(0, len(TCP)):
                TCP.iloc[j, 5] = count
                count += 1

        elif i == 'FINGER':
            count = 0
            for j in range(0, len(FINGER)):
                FINGER.iloc[j, 5] = count
                count += 1
          
        elif i == 'SMTP':
            count = 0
            for j in range(0, len(SMTP)):
                SMTP.iloc[j, 5] = count
                count += 1
    
        elif i == 'SMTP_IMF':
            count = 0
            for j in range(0, len(SMTP_IMF)):
                SMTP_IMF.iloc[j, 5] = count
                count += 1

        elif i == 'ARP':
            count = 0
            for j in range(0, len(ARP)):
                ARP.iloc[j, 5] = count
                count += 1

        elif i == 'ICMP':
            count = 0
            for j in range(0, len(ICMP)):
                ICMP.iloc[j, 5] = count
                count += 1
    
        elif i == 'IRC':
            count = 0
            for j in range(0, len(IRC)):
                IRC.iloc[j, 5] = count
                count += 1

        elif i == 'HTTP':
            count = 0
            for j in range(0, len(HTTP)):
                HTTP.iloc[j, 5] = count
                count += 1
    
        elif i == 'FTP':
            count = 0
            for j in range(0, len(FTP)):
                FTP.iloc[j, 5] = count
                count += 1

        elif i == 'FTP_DATA':
            count = 0
            for j in range(0, len(FTP_DATA)):
                FTP_DATA.iloc[j, 5] = count
                count += 1
     
        elif i == 'SNMP':
            count = 0
            for j in range(0, len(SNMP)):
                SNMP.iloc[j, 5] = count
                count += 1
    
        elif i == 'LLAP':
            count = 0
            for j in range(0, len(LLAP)):
                LLAP.iloc[j, 5] = count
                count += 1
    
        elif i == 'TELNET':
            count = 0
            for j in range(0, len(TELNET)):
                TELNET.iloc[j, 5] = count
                count += 1
          
        elif i == 'TIME':
            count = 0
            for j in range(0, len(TIME)):
                TIME.iloc[j, 5] = count
                count += 1
    
        elif i == 'SSHV1':
            count = 0
            for j in range(0, len(SSHV1)):
                SSHV1.iloc[j, 5] = count
                count += 1
        
        elif i == 'POP':
            count = 0
            for j in range(0, len(POP)):
                POP.iloc[j, 5] = count
                count += 1

        elif i == 'NBNS':
            count = 0
            for j in range(0, len(NBNS)):
                NBNS.iloc[j, 5] = count
                count += 1
        
        elif i == 'SMTP_IMF_IMF':
            count = 0
            for j in range(0, len(SMTP_IMF_IMF)):
                SMTP_IMF_IMF.iloc[j, 5] = count
                count += 1
        
        elif i == 'GTP':
            count = 0
            for j in range(0, len(GTP)):
                GTP.iloc[j, 5] = count
                count += 1
        elif i == 'TPM':
            count = 0
            for j in range(0, len(TPM)):
                TPM.iloc[j, 5] = count
                count += 1

def save(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):
    LLC = pd.DataFrame(LLC)
    LLC.to_csv("public/Protocol/LLC.csv", sep=",", index=False)
    CDP = pd.DataFrame(CDP)
    CDP.to_csv("public/Protocol/CDP.csv", sep=",", index=False)
    RIPV2 = pd.DataFrame(RIPV2)
    RIPV2.to_csv("public/Protocol/RIPv2.csv", sep=",", index=False)
    LOOP = pd.DataFrame(LOOP)
    LOOP.to_csv("public/Protocol/LOOP.csv", sep=",", index=False)
    NTP = pd.DataFrame(NTP)
    NTP.to_csv("public/Protocol/NTP.csv", sep=",", index=False)
    DNS = pd.DataFrame(DNS)
    DNS.to_csv("public/Protocol/DNS.csv", sep=",", index=False)
    TCP = pd.DataFrame(TCP)
    TCP.to_csv("public/Protocol/TCP.csv", sep=",", index=False)
    FINGER = pd.DataFrame(FINGER)
    FINGER.to_csv("public/Protocol/FINGER.csv", sep=",", index=False)
    SMTP = pd.DataFrame(SMTP)
    SMTP.to_csv("public/Protocol/SMTP.csv", sep=",", index=False)
    SMTP_IMF = pd.DataFrame(SMTP_IMF)
    SMTP_IMF.to_csv("public/Protocol/SMTP_IMF.csv", sep=",", index=False)
    ARP = pd.DataFrame(ARP)
    ARP.to_csv("public/Protocol/ARP.csv", sep=",", index=False)
    ICMP = pd.DataFrame(ICMP)
    ICMP.to_csv("public/Protocol/ICMP.csv", sep=",", index=False)
    IRC = pd.DataFrame(IRC)
    IRC.to_csv("public/Protocol/IRC.csv", sep=",", index=False)
    HTTP = pd.DataFrame(HTTP)
    HTTP.to_csv("public/Protocol/HTTP.csv", sep=",", index=False)
    FTP = pd.DataFrame(FTP)
    FTP.to_csv("public/Protocol/FTP.csv", sep=",", index=False)
    FTP_DATA = pd.DataFrame(FTP_DATA)
    FTP_DATA.to_csv("public/Protocol/FTP_DATA.csv", sep=",", index=False)
    SNMP = pd.DataFrame(SNMP)
    SNMP.to_csv("public/Protocol/SNMP.csv", sep=",", index=False)
    LLAP = pd.DataFrame(LLAP)
    LLAP.to_csv("public/Protocol/LLAP.csv", sep=",", index=False)
    TELNET = pd.DataFrame(TELNET)
    TELNET.to_csv("public/Protocol/TELNET.csv", sep=",", index=False)
    TIME = pd.DataFrame(TIME)
    TIME.to_csv("public/Protocol/TIME.csv", sep=",", index=False)
    SSHV1 = pd.DataFrame(SSHV1)
    SSHV1.to_csv("public/Protocol/SSHv1.csv", sep=",", index=False)
    POP = pd.DataFrame(POP)
    POP.to_csv("public/Protocol/POP.csv", sep=",", index=False)
    NBNS = pd.DataFrame(NBNS)
    NBNS.to_csv("public/Protocol/NBNS.csv", sep=",", index=False)
    SMTP_IMF_IMF = pd.DataFrame(SMTP_IMF_IMF)
    SMTP_IMF_IMF.to_csv("public/Protocol/SMTP_IMF_IMF.csv", sep=",", index=False)
    GTP = pd.DataFrame(GTP)
    GTP.to_csv("public/Protocol/GTP.csv", sep=",", index=False)
    TPM = pd.DataFrame(TPM)
    TPM.to_csv("public/Protocol/TPM.csv", sep=",", index=False)

