import pandas as pd


def share_protocol(main_data, LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):
    for i in range(0, len(main_data)):
        data = main_data.iloc[i, 1]
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


def add_weight(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):

    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC',
                'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']
    for i in protocol:

        if i == 'LLC':
            count = 0
            for j in range(0, len(LLC)):
                LLC.iloc[j, 3] = count
                count += 1

        elif i == 'CDP':
            count = 0
            for j in range(0, len(CDP)):
                CDP.iloc[j, 3] = count
                count += 1

        elif i == 'RIPV2':
            count = 0
            for j in range(0, len(RIPV2)):
                RIPV2.iloc[j, 3] = count
                count += 1

        elif i == 'LOOP':
            count = 0
            for j in range(0, len(LOOP)):
                LOOP.iloc[j, 3] = count
                count += 1

        elif i == 'NTP':
            count = 0
            for j in range(0, len(NTP)):
                NTP.iloc[j, 3] = count
                count += 1

        elif i == 'DNS':
            count = 0
            for j in range(0, len(DNS)):
                DNS.iloc[j, 3] = count
                count += 1

        elif i == 'TCP':
            count = 0
            for j in range(0, len(TCP)):
                TCP.iloc[j, 3] = count
                count += 1

        elif i == 'FINGER':
            count = 0
            for j in range(0, len(FINGER)):
                FINGER.iloc[j, 3] = count
                count += 1

        elif i == 'SMTP':
            count = 0
            for j in range(0, len(SMTP)):
                SMTP.iloc[j, 3] = count
                count += 1

        elif i == 'SMTP_IMF':
            count = 0
            for j in range(0, len(SMTP_IMF)):
                SMTP_IMF.iloc[j, 3] = count
                count += 1

        elif i == 'ARP':
            count = 0
            for j in range(0, len(ARP)):
                ARP.iloc[j, 3] = count
                count += 1

        elif i == 'ICMP':
            count = 0
            for j in range(0, len(ICMP)):
                ICMP.iloc[j, 3] = count
                count += 1

        elif i == 'IRC':
            count = 0
            for j in range(0, len(IRC)):
                IRC.iloc[j, 3] = count
                count += 1

        elif i == 'HTTP':
            count = 0
            for j in range(0, len(HTTP)):
                HTTP.iloc[j, 3] = count
                count += 1

        elif i == 'FTP':
            count = 0
            for j in range(0, len(FTP)):
                FTP.iloc[j, 3] = count
                count += 1

        elif i == 'FTP_DATA':
            count = 0
            for j in range(0, len(FTP_DATA)):
                FTP_DATA.iloc[j, 3] = count
                count += 1

        elif i == 'SNMP':
            count = 0
            for j in range(0, len(SNMP)):
                SNMP.iloc[j, 3] = count
                count += 1

        elif i == 'LLAP':
            count = 0
            for j in range(0, len(LLAP)):
                LLAP.iloc[j, 3] = count
                count += 1

        elif i == 'TELNET':
            count = 0
            for j in range(0, len(TELNET)):
                TELNET.iloc[j, 3] = count
                count += 1

        elif i == 'TIME':
            count = 0
            for j in range(0, len(TIME)):
                TIME.iloc[j, 3] = count
                count += 1

        elif i == 'SSHV1':
            count = 0
            for j in range(0, len(SSHV1)):
                SSHV1.iloc[j, 3] = count
                count += 1

        elif i == 'POP':
            count = 0
            for j in range(0, len(POP)):
                POP.iloc[j, 3] = count
                count += 1

        elif i == 'NBNS':
            count = 0
            for j in range(0, len(NBNS)):
                NBNS.iloc[j, 3] = count
                count += 1

        elif i == 'SMTP_IMF_IMF':
            count = 0
            for j in range(0, len(SMTP_IMF_IMF)):
                SMTP_IMF_IMF.iloc[j, 3] = count
                count += 1

        elif i == 'GTP':
            count = 0
            for j in range(0, len(GTP)):
                GTP.iloc[j, 3] = count
                count += 1
        elif i == 'TPM':
            count = 0
            for j in range(0, len(TPM)):
                TPM.iloc[j, 3] = count
                count += 1


def check_empty(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):

    empty = ['Time', 'Protocol', 'Length', 'Weight', 'Multiplication']
    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC',
                'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']

    for i in protocol:
        if i == 'LLC' and len(LLC) == 0:
            LLC.append(empty)
        elif i == 'CDP' and len(CDP) == 0:
            CDP.append(empty)
        elif i == 'RIPV2' and len(RIPV2) == 0:
            RIPV2 .append(empty)
        elif i == 'LOOP' and len(LOOP) == 0:
            LOOP.append(empty)
        elif i == 'NTP' and len(NTP) == 0:
            NTP.append(empty)
        elif i == 'DNS' and len(DNS) == 0:
            DNS.append(empty)
        elif i == 'TCP' and len(TCP) == 0:
            TCP.append(empty)
        elif i == 'FINGER' and len(FINGER) == 0:
            FINGER.append(empty)
        elif i == 'SMTP' and len(SMTP) == 0:
            SMTP .append(empty)
        elif i == 'SMTP_IMF' and len(SMTP_IMF) == 0:
            SMTP_IMF.append(empty)
        elif i == 'ARP' and len(ARP) == 0:
            ARP.append(empty)
        elif i == 'ICMP' and len(ICMP) == 0:
            ICMP .append(empty)
        elif i == 'IRC' and len(IRC) == 0:
            IRC.append(empty)
        elif i == 'HTTP' and len(HTTP) == 0:
            HTTP .append(empty)
        elif i == 'FTP' and len(FTP) == 0:
            FTP.append(empty)
        elif i == 'FTP_DATA' and len(FTP_DATA) == 0:
            FTP_DATA.append(empty)
        elif i == 'SNMP' and len(SNMP) == 0:
            SNMP .append(empty)
        elif i == 'LLAP' and len(LLAP) == 0:
            LLAP.append(empty)
        elif i == 'TELNET' and len(TELNET) == 0:
            TELNET.append(empty)
        elif i == 'TIME' and len(TIME) == 0:
            TIME .append(empty)
        elif i == 'SSHV1' and len(SSHV1) == 0:
            SSHV1.append(empty)
        elif i == 'POP' and len(POP) == 0:
            POP.append(empty)
        elif i == 'NBNS' and len(NBNS) == 0:
            NBNS.append(empty)
        elif i == 'SMTP_IMF_IMF' and len(SMTP_IMF_IMF) == 0:
            SMTP_IMF_IMF.append(empty)
        elif i == 'GTP' and len(GTP) == 0:
            GTP.append(empty)
        elif i == 'TPM' and len(TPM) == 0:
            TPM.append(empty)


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
    SMTP_IMF_IMF.to_csv("public/Protocol/SMTP_IMF_IMF.csv",
                        sep=",", index=False)
    GTP = pd.DataFrame(GTP)
    GTP.to_csv("public/Protocol/GTP.csv", sep=",", index=False)
    TPM = pd.DataFrame(TPM)
    TPM.to_csv("public/Protocol/TPM.csv", sep=",", index=False)


def apply_multi(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):
    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC',
                'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']

    for i in protocol:
        if i == 'LLC':
            for j in range(0, len(LLC)):
                length = LLC.iloc[j, 2]
                weight = LLC.iloc[j, 3]
                result = length * weight
                LLC.iloc[j, 4] = result
        elif i == 'CDP':
            for j in range(0, len(CDP)):
                length = CDP.iloc[j, 2]
                weight = CDP.iloc[j, 3]
                result = length * weight
                CDP.iloc[j, 4] = result
        elif i == 'RIPV2':
            for j in range(0, len(RIPV2)):
                length = RIPV2.iloc[j, 2]
                weight = RIPV2.iloc[j, 3]
                result = length * weight
                RIPV2.iloc[j, 4] = result
        elif i == 'LOOP':
            for j in range(0, len(LOOP)):
                length = LOOP.iloc[j, 2]
                weight = LOOP.iloc[j, 3]
                result = length * weight
                LOOP.iloc[j, 4] = result
        elif i == 'NTP':
            for j in range(0, len(NTP)):
                length = NTP.iloc[j, 2]
                weight = NTP.iloc[j, 3]
                result = length * weight
                NTP.iloc[j, 4] = result
        elif i == 'DNS':
            for j in range(0, len(DNS)):
                length = DNS.iloc[j, 2]
                weight = DNS.iloc[j, 3]
                result = length * weight
                DNS.iloc[j, 4] = result
        elif i == 'FINGER':
            for j in range(0, len(FINGER)):
                length = FINGER.iloc[j, 2]
                weight = FINGER.iloc[j, 3]
                result = length * weight
                FINGER.iloc[j, 4] = result
        elif i == 'SMTP':
            for j in range(0, len(SMTP)):
                length = SMTP.iloc[j, 2]
                weight = SMTP.iloc[j, 3]
                result = length * weight
                SMTP.iloc[j, 4] = result
        elif i == 'SMTP_IMF':
            for j in range(0, len(SMTP_IMF)):
                length = SMTP_IMF.iloc[j, 2]
                weight = SMTP_IMF.iloc[j, 3]
                result = length * weight
                SMTP_IMF.iloc[j, 4] = result
        elif i == 'ARP':
            for j in range(0, len(ARP)):
                length = ARP.iloc[j, 2]
                weight = ARP.iloc[j, 3]
                result = length * weight
                ARP.iloc[j, 4] = result
        elif i == 'ICMP':
            for j in range(0, len(ICMP)):
                length = ICMP.iloc[j, 2]
                weight = ICMP.iloc[j, 3]
                result = length * weight
                ICMP.iloc[j, 4] = result
        elif i == 'IRC':
            for j in range(0, len(IRC)):
                length = IRC.iloc[j, 2]
                weight = IRC.iloc[j, 3]
                result = length * weight
                IRC.iloc[j, 4] = result
        elif i == 'HTTP':
            for j in range(0, len(HTTP)):
                length = HTTP.iloc[j, 2]
                weight = HTTP.iloc[j, 3]
                result = length * weight
                HTTP.iloc[j, 4] = result
        elif i == 'FTP':
            for j in range(0, len(FTP)):
                length = FTP.iloc[j, 2]
                weight = FTP.iloc[j, 3]
                result = length * weight
                FTP.iloc[j, 4] = result
        elif i == 'FTP_DATA':
            for j in range(0, len(FTP_DATA)):
                length = FTP_DATA.iloc[j, 2]
                weight = FTP_DATA.iloc[j, 3]
                result = length * weight
                FTP_DATA.iloc[j, 4] = result
        elif i == 'SNMP':
            for j in range(0, len(SNMP)):
                length = SNMP.iloc[j, 2]
                weight = SNMP.iloc[j, 3]
                result = length * weight
                SNMP.iloc[j, 4] = result
        elif i == 'LLAP':
            for j in range(0, len(LLAP)):
                length = LLAP.iloc[j, 2]
                weight = LLAP.iloc[j, 3]
                result = length * weight
                LLAP.iloc[j, 4] = result
        elif i == 'TELNET':
            for j in range(0, len(TELNET)):
                length = TELNET.iloc[j, 2]
                weight = TELNET.iloc[j, 3]
                result = length * weight
                TELNET.iloc[j, 4] = result
        elif i == 'TIME':
            for j in range(0, len(TIME)):
                length = TIME.iloc[j, 2]
                weight = TIME.iloc[j, 3]
                result = length * weight
                TIME.iloc[j, 4] = result
        elif i == 'SSHV1':
            for j in range(0, len(SSHV1)):
                length = SSHV1.iloc[j, 2]
                weight = SSHV1.iloc[j, 3]
                result = length * weight
                SSHV1.iloc[j, 4] = result
        elif i == 'POP':
            for j in range(0, len(POP)):
                length = POP.iloc[j, 2]
                weight = POP.iloc[j, 3]
                result = length * weight
                POP.iloc[j, 4] = result
        elif i == 'NBNS':
            for j in range(0, len(NBNS)):
                length = NBNS.iloc[j, 2]
                weight = NBNS.iloc[j, 3]
                result = length * weight
                NBNS.iloc[j, 4] = result
        elif i == 'SMTP_IMF_IMF':
            for j in range(0, len(SMTP_IMF_IMF)):
                length = SMTP_IMF_IMF.iloc[j, 2]
                weight = SMTP_IMF_IMF.iloc[j, 3]
                result = length * weight
                SMTP_IMF_IMF.iloc[j, 4] = result
        elif i == 'GTP':
            for j in range(0, len(GTP)):
                length = GTP.iloc[j, 2]
                weight = GTP.iloc[j, 3]
                result = length * weight
                GTP.iloc[j, 4] = result
        elif i == 'TPM':
            for j in range(0, len(TPM)):
                length = TPM.iloc[j, 2]
                weight = TPM.iloc[j, 3]
                result = length * weight
                TPM.iloc[j, 4] = result
