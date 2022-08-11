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
            count = 1
            for j in range(0, len(LLC)):
                LLC.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'CDP':
            count = 1
            for j in range(0, len(CDP)):
                CDP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'RIPV2':
            count = 1
            for j in range(0, len(RIPV2)):
                RIPV2.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'LOOP':
            count = 1
            for j in range(0, len(LOOP)):
                LOOP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'NTP':
            count = 1
            for j in range(0, len(NTP)):
                NTP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'DNS':
            count = 1
            for j in range(0, len(DNS)):
                DNS.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'TCP':
            count = 1
            for j in range(0, len(TCP)):
                TCP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'FINGER':
            count = 1
            for j in range(0, len(FINGER)):
                FINGER.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'SMTP':
            count = 1
            for j in range(0, len(SMTP)):
                SMTP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'SMTP_IMF':
            count = 1
            for j in range(0, len(SMTP_IMF)):
                SMTP_IMF.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'ARP':
            count = 1
            for j in range(0, len(ARP)):
                ARP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'ICMP':
            count = 1
            for j in range(0, len(ICMP)):
                ICMP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'IRC':
            count = 1
            for j in range(0, len(IRC)):
                IRC.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'HTTP':
            count = 1
            for j in range(0, len(HTTP)):
                HTTP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'FTP':
            count = 1
            for j in range(0, len(FTP)):
                FTP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'FTP_DATA':
            count = 1
            for j in range(0, len(FTP_DATA)):
                FTP_DATA.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'SNMP':
            count = 1
            for j in range(0, len(SNMP)):
                SNMP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'LLAP':
            count = 1
            for j in range(0, len(LLAP)):
                LLAP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'TELNET':
            count = 1
            for j in range(0, len(TELNET)):
                TELNET.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'TIME':
            count = 1
            for j in range(0, len(TIME)):
                TIME.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'SSHV1':
            count = 1
            for j in range(0, len(SSHV1)):
                SSHV1.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'POP':
            count = 1
            for j in range(0, len(POP)):
                POP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'NBNS':
            count = 1
            for j in range(0, len(NBNS)):
                NBNS.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'SMTP_IMF_IMF':
            count = 1
            for j in range(0, len(SMTP_IMF_IMF)):
                SMTP_IMF_IMF.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1

        elif i == 'GTP':
            count = 1
            for j in range(0, len(GTP)):
                GTP.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1
        elif i == 'TPM':
            count = 1
            for j in range(0, len(TPM)):
                TPM.iloc[j, 3] = count
                if count == 300:
                    count = 0
                count += 1


def sum_weight(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):
    pass
    sum_periods = []
    sum_periods = pd.DataFrame(sum_periods)

    sum_weight = []
    sum_weight = pd.DataFrame(sum_weight)

    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC',
                'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']
    for i in protocol:
        if i == 'LLC':
            total = LLC.iloc[:, 3].sum()
            sum_periods.insert(0, 'LLC', [total])

            total_weight = LLC.iloc[:, 4].sum()
            sum_weight.insert(0, 'LLC', [total_weight])
        elif i == 'CDP':
            total = CDP.iloc[:, 3].sum()
            sum_periods.insert(1, 'CDP', [total])

            total_weight = CDP.iloc[:, 4].sum()
            sum_weight.insert(1, 'CDP', [total_weight])
        elif i == 'RIPV2':
            total = RIPV2.iloc[:, 3].sum()
            sum_periods.insert(2, 'RIPV2', [total])

            total_weight = RIPV2.iloc[:, 4].sum()
            sum_weight.insert(2, 'RIPV2', [total_weight])
        elif i == 'LOOP':
            total = LOOP.iloc[:, 3].sum()
            sum_periods.insert(3, 'LOOP', [total])

            total_weight = LOOP.iloc[:, 4].sum()
            sum_weight.insert(3, 'LOOP', [total_weight])
        elif i == 'NTP':
            total = NTP.iloc[:, 3].sum()
            sum_periods.insert(4, 'NTP', [total])

            total_weight = NTP.iloc[:, 4].sum()
            sum_weight.insert(4, 'NTP', [total_weight])
        elif i == 'DNS':
            total = DNS.iloc[:, 3].sum()
            sum_periods.insert(5, 'DNS', [total])

            total_weight = DNS.iloc[:, 4].sum()
            sum_weight.insert(5, 'DNS', [total_weight])
        elif i == 'TCP':
            total = TCP.iloc[:, 3].sum()
            sum_periods.insert(6, 'TCP', [total])

            total_weight = TCP.iloc[:, 4].sum()
            sum_weight.insert(6, 'TCP', [total_weight])
        elif i == 'FINGER':
            total = FINGER.iloc[:, 3].sum()
            sum_periods.insert(7, 'FINGER', [total])

            total_weight = FINGER.iloc[:, 4].sum()
            sum_weight.insert(7, 'FINGER', [total_weight])
        elif i == 'SMTP':
            total = SMTP.iloc[:, 3].sum()
            sum_periods.insert(8, 'SMTP', [total])

            total_weight = SMTP.iloc[:, 4].sum()
            sum_weight.insert(8, 'SMTP', [total_weight])
        elif i == 'SMTP_IMF':
            total = SMTP_IMF.iloc[:, 3].sum()
            sum_periods.insert(9, 'SMTP_IMF', [total])

            total_weight = SMTP_IMF.iloc[:, 4].sum()
            sum_weight.insert(9, 'SMTP_IMF', [total_weight])
        elif i == 'ARP':
            total = ARP.iloc[:, 3].sum()
            sum_periods.insert(10, 'ARP', [total])

            total_weight = ARP.iloc[:, 4].sum()
            sum_weight.insert(10, 'ARP', [total_weight])
        elif i == 'ICMP':
            total = ICMP.iloc[:, 3].sum()
            sum_periods.insert(11, 'ICMP', [total])

            total_weight = ICMP.iloc[:, 4].sum()
            sum_weight.insert(11, 'ICMP', [total_weight])
        elif i == 'IRC':
            total = IRC.iloc[:, 3].sum()
            sum_periods.insert(12, 'IRC', [total])

            total_weight = IRC.iloc[:, 4].sum()
            sum_weight.insert(12, 'IRC', [total_weight])
        elif i == 'HTTP':
            total = HTTP.iloc[:, 3].sum()
            sum_periods.insert(13, 'HTTP', [total])

            total_weight = HTTP.iloc[:, 4].sum()
            sum_weight.insert(13, 'HTTP', [total_weight])
        elif i == 'FTP':
            total = FTP.iloc[:, 3].sum()
            sum_periods.insert(14, 'FTP', [total])

            total_weight = FTP.iloc[:, 4].sum()
            sum_weight.insert(14, 'FTP', [total_weight])
        elif i == 'FTP_DATA':
            total = FTP_DATA.iloc[:, 3].sum()
            sum_periods.insert(15, 'FTP_DATA', [total])

            total_weight = FTP_DATA.iloc[:, 4].sum()
            sum_weight.insert(15, 'FTP_DATA', [total_weight])
        elif i == 'SNMP':
            total = SNMP.iloc[:, 3].sum()
            sum_periods.insert(16, 'SNMP', [total])

            total_weight = SNMP.iloc[:, 4].sum()
            sum_weight.insert(16, 'SNMP', [total_weight])
        elif i == 'LLAP':
            total = LLAP.iloc[:, 3].sum()
            sum_periods.insert(17, 'LLAP', [total])

            total_weight = LLAP.iloc[:, 4].sum()
            sum_weight.insert(17, 'LLAP', [total_weight])
        elif i == 'TELNET':
            total = TELNET.iloc[:, 3].sum()
            sum_periods.insert(18, 'TELNET', [total])

            total_weight = TELNET.iloc[:, 4].sum()
            sum_weight.insert(18, 'TELNET', [total_weight])
        elif i == 'TIME':
            total = TIME.iloc[:, 3].sum()
            sum_periods.insert(19, 'TIME', [total])

            total_weight = TIME.iloc[:, 4].sum()
            sum_weight.insert(19, 'TIME', [total_weight])
        elif i == 'SSHV1':
            total = SSHV1.iloc[:, 3].sum()
            sum_periods.insert(20, 'SSHV1', [total])

            total_weight = SSHV1.iloc[:, 4].sum()
            sum_weight.insert(20, 'SSHV1', [total_weight])
        elif i == 'POP':
            total = POP.iloc[:, 3].sum()
            sum_periods.insert(21, 'POP', [total])

            total_weight = POP.iloc[:, 4].sum()
            sum_weight.insert(12, 'POP', [total_weight])
        elif i == 'NBNS':
            total = NBNS.iloc[:, 3].sum()
            sum_periods.insert(22, 'NBNS', [total])

            total_weight = NBNS.iloc[:, 4].sum()
            sum_weight.insert(22, 'NBNS', [total_weight])
        elif i == 'SMTP_IMF_IMF':
            total = SMTP_IMF_IMF.iloc[:, 3].sum()
            sum_periods.insert(23, 'SMTP_IMF_IMF', [total])

            total_weight = SMTP_IMF_IMF.iloc[:, 4].sum()
            sum_weight.insert(23, 'SMTP_IMF_IMF', [total_weight])
        elif i == 'GTP':
            total = GTP.iloc[:, 3].sum()
            sum_periods.insert(24, 'GTP', [total])

            total_weight = GTP.iloc[:, 4].sum()
            sum_weight.insert(24, 'GTP', [total_weight])
        elif i == 'TPM':
            total = TPM.iloc[:, 3].sum()
            sum_periods.insert(25, 'TPM', [total])

            total_weight = TPM.iloc[:, 4].sum()
            sum_weight.insert(25, 'TPM', [total_weight])

    sum_periods.to_csv("Public/sum_periods.csv", sep=",", index=False)

    sum_weight.to_csv("Public/sum_weight.csv", sep=",", index=False)


def check_empty(LLC, CDP, RIPV2, LOOP, NTP, DNS, TCP, FINGER, SMTP, SMTP_IMF, ARP, ICMP, IRC, HTTP, FTP, FTP_DATA, SNMP, LLAP, TELNET, TIME, SSHV1, POP, NBNS, SMTP_IMF_IMF, GTP, TPM):

    empty = [1, 1, 1, 1, 1, 1]
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
    LLC = pd.DataFrame(LLC, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    LLC.to_csv("Public/Protocol/LLC.csv", sep=",", index=False)
    CDP = pd.DataFrame(CDP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    CDP.to_csv("Public/Protocol/CDP.csv", sep=",", index=False)
    RIPV2 = pd.DataFrame(RIPV2, columns=[
                         'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    RIPV2.to_csv("Public/Protocol/RIPv2.csv", sep=",", index=False)
    LOOP = pd.DataFrame(LOOP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    LOOP.to_csv("Public/Protocol/LOOP.csv", sep=",", index=False)
    NTP = pd.DataFrame(NTP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    NTP.to_csv("Public/Protocol/NTP.csv", sep=",", index=False)
    DNS = pd.DataFrame(DNS, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    DNS.to_csv("Public/Protocol/DNS.csv", sep=",", index=False)
    TCP = pd.DataFrame(TCP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    TCP.to_csv("Public/Protocol/TCP.csv", sep=",", index=False)
    FINGER = pd.DataFrame(FINGER, columns=[
                          'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    FINGER.to_csv("Public/Protocol/FINGER.csv", sep=",", index=False)
    SMTP = pd.DataFrame(SMTP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    SMTP.to_csv("Public/Protocol/SMTP.csv", sep=",", index=False)
    SMTP_IMF = pd.DataFrame(SMTP_IMF, columns=[
                            'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    SMTP_IMF.to_csv("Public/Protocol/SMTP_IMF.csv", sep=",", index=False)
    ARP = pd.DataFrame(ARP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    ARP.to_csv("Public/Protocol/ARP.csv", sep=",", index=False)
    ICMP = pd.DataFrame(ICMP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    ICMP.to_csv("Public/Protocol/ICMP.csv", sep=",", index=False)
    IRC = pd.DataFrame(IRC, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    IRC.to_csv("Public/Protocol/IRC.csv", sep=",", index=False)
    HTTP = pd.DataFrame(HTTP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    HTTP.to_csv("Public/Protocol/HTTP.csv", sep=",", index=False)
    FTP = pd.DataFrame(FTP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    FTP.to_csv("Public/Protocol/FTP.csv", sep=",", index=False)
    FTP_DATA = pd.DataFrame(FTP_DATA, columns=[
                            'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    FTP_DATA.to_csv("Public/Protocol/FTP_DATA.csv", sep=",", index=False)
    SNMP = pd.DataFrame(SNMP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    SNMP.to_csv("Public/Protocol/SNMP.csv", sep=",", index=False)
    LLAP = pd.DataFrame(LLAP, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    LLAP.to_csv("Public/Protocol/LLAP.csv", sep=",", index=False)
    TELNET = pd.DataFrame(TELNET, columns=[
                          'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    TELNET.to_csv("Public/Protocol/TELNET.csv", sep=",", index=False)
    TIME = pd.DataFrame(TIME, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    TIME.to_csv("Public/Protocol/TIME.csv", sep=",", index=False)
    SSHV1 = pd.DataFrame(SSHV1, columns=[
                         'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    SSHV1.to_csv("Public/Protocol/SSHv1.csv", sep=",", index=False)
    POP = pd.DataFrame(POP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    POP.to_csv("Public/Protocol/POP.csv", sep=",", index=False)
    NBNS = pd.DataFrame(NBNS, columns=[
                        'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    NBNS.to_csv("Public/Protocol/NBNS.csv", sep=",", index=False)
    SMTP_IMF_IMF = pd.DataFrame(SMTP_IMF_IMF, columns=[
                                'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    SMTP_IMF_IMF.to_csv("Public/Protocol/SMTP_IMF_IMF.csv",
                        sep=",", index=False)
    GTP = pd.DataFrame(GTP, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    GTP.to_csv("Public/Protocol/GTP.csv", sep=",", index=False)
    TPM = pd.DataFrame(TPM, columns=[
                       'Time', 'Protocol', 'Length', 'Weight', 'Multiplication', 'Forecast'])
    TPM.to_csv("Public/Protocol/TPM.csv", sep=",", index=False)


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
        elif i == 'TCP':
            for j in range(0, len(TCP)):
                length = TCP.iloc[j, 2]
                weight = TCP.iloc[j, 3]
                result = length * weight
                TCP.iloc[j, 4] = result


def division_weight():
    protocol = ['LLC', 'CDP', 'RIPV2', 'LOOP', 'NTP', 'DNS', 'TCP', 'FINGER', 'SMTP', 'SMTP_IMF', 'ARP', 'ICMP', 'IRC',
                'HTTP', 'FTP', 'FTP_DATA', 'SNMP', 'LLAP', 'TELNET', 'TIME', 'SSHV1', 'POP', 'NBNS', 'SMTP_IMF_IMF', 'GTP', 'TPM']

    sum_weight = pd.read_csv('Public/sum_weight.csv')

    sum_periods = pd.read_csv('Public/sum_periods.csv')

    division_weight = []
    division_weight = pd.DataFrame(division_weight)

    for i in protocol:
        if i == "LLC":
            LLC_weight = sum_weight.iloc[:, 0]
            LLC_periods = sum_periods.iloc[:, 0]
            division = LLC_periods / LLC_weight
            division_weight.insert(0, 'LLC', division)

        elif i == "CDP":
            CDP_weight = sum_weight.iloc[:, 1]
            CDP_periods = sum_periods.iloc[:, 1]
            division = CDP_periods / CDP_weight
            division_weight.insert(1, 'CDP', division)

        elif i == "RIPV2":
            RIPV2_weight = sum_weight.iloc[:, 2]
            RIPV2_periods = sum_periods.iloc[:, 2]
            division = RIPV2_periods / RIPV2_weight
            division_weight.insert(2, 'RIPV2', division)

        elif i == "LOOP":
            LOOP_weight = sum_weight.iloc[:, 3]
            LOOP_periods = sum_periods.iloc[:, 3]
            division = LOOP_periods / LOOP_weight
            division_weight.insert(3, 'LOOP', division)

        elif i == "NTP":
            NTP_weight = sum_weight.iloc[:, 4]
            NTP_periods = sum_periods.iloc[:, 4]
            division = NTP_periods / NTP_weight
            division_weight.insert(4, 'NTP', division)

        elif i == "DNS":
            DNS_weight = sum_weight.iloc[:, 5]
            DNS_periods = sum_periods.iloc[:, 5]
            division = DNS_periods / DNS_weight
            division_weight.insert(5, 'DNS', division)

        elif i == "TCP":
            TCP_weight = sum_weight.iloc[:, 6]
            TCP_periods = sum_periods.iloc[:, 6]
            division = TCP_periods / TCP_weight
            division_weight.insert(6, 'TCP', division)

        elif i == "FINGER":
            FINGER_weight = sum_weight.iloc[:, 7]
            FINGER_periods = sum_periods.iloc[:, 7]
            division = FINGER_periods / FINGER_weight
            division_weight.insert(7, 'FINGER', division)

        elif i == "SMTP":
            SMTP_weight = sum_weight.iloc[:, 8]
            SMTP_periods = sum_periods.iloc[:, 8]
            division = SMTP_periods / SMTP_weight
            division_weight.insert(8, 'SMTP', division)

        elif i == "SMTP_IMF":
            SMTP_IMF_weight = sum_weight.iloc[:, 9]
            SMTP_IMF_periods = sum_periods.iloc[:, 9]
            division = SMTP_IMF_periods / SMTP_IMF_weight
            division_weight.insert(9, 'SMTP_IMF', division)

        elif i == "ARP":
            ARP_weight = sum_weight.iloc[:, 10]
            ARP_periods = sum_periods.iloc[:, 10]
            division = ARP_periods / ARP_weight
            division_weight.insert(10, 'ARP', division)

        elif i == "ICMP":
            ICMP_weight = sum_weight.iloc[:, 11]
            ICMP_periods = sum_periods.iloc[:, 11]
            division = ICMP_periods / ICMP_weight
            division_weight.insert(11, 'ICMP', division)

        elif i == "IRC":
            IRC_weight = sum_weight.iloc[:, 12]
            IRC_periods = sum_periods.iloc[:, 12]
            division = IRC_periods / IRC_weight
            division_weight.insert(12, 'IRC', division)

        elif i == "HTTP":
            HTTP_weight = sum_weight.iloc[:, 13]
            HTTP_periods = sum_periods.iloc[:, 13]
            division = HTTP_periods / HTTP_weight
            division_weight.insert(13, 'HTTP', division)

        elif i == "FTP":
            FTP_weight = sum_weight.iloc[:, 14]
            FTP_periods = sum_periods.iloc[:, 14]
            division = FTP_periods / FTP_weight
            division_weight.insert(14, 'FTP', division)

        elif i == "FTP_DATA":
            FTP_DATA_weight = sum_weight.iloc[:, 15]
            FTP_DATA_periods = sum_periods.iloc[:, 15]
            division = FTP_DATA_periods / FTP_DATA_weight
            division_weight.insert(15, 'FTP_DATA', division)

        elif i == "SNMP":
            SNMP_weight = sum_weight.iloc[:, 16]
            SNMP_periods = sum_periods.iloc[:, 16]
            division = SNMP_periods / SNMP_weight
            division_weight.insert(16, 'SNMP', division)

        elif i == "LLAP":
            LLAP_weight = sum_weight.iloc[:, 17]
            LLAP_periods = sum_periods.iloc[:, 17]
            division = LLAP_periods / LLAP_weight
            division_weight.insert(17, 'LLAP', division)

        elif i == "TELNET":
            TELNET_weight = sum_weight.iloc[:, 18]
            TELNET_periods = sum_periods.iloc[:, 18]
            division = TELNET_periods / TELNET_weight
            division_weight.insert(18, 'TELNET', division)

        elif i == "TIME":
            TIME_weight = sum_weight.iloc[:, 19]
            TIME_periods = sum_periods.iloc[:, 19]
            division = TIME_periods / TIME_weight
            division_weight.insert(0, 'TIME', division)

        elif i == "SSHV1":
            SSHV1_weight = sum_weight.iloc[:, 20]
            SSHV1_periods = sum_periods.iloc[:, 20]
            division = SSHV1_periods / SSHV1_weight
            division_weight.insert(20, 'SSHV1', division)

        elif i == "POP":
            POP_weight = sum_weight.iloc[:, 21]
            POP_periods = sum_periods.iloc[:, 21]
            division = POP_periods / POP_weight
            division_weight.insert(21, 'POP', division)

        elif i == "NBNS":
            NBNS_weight = sum_weight.iloc[:, 22]
            NBNS_periods = sum_periods.iloc[:, 22]
            division = int(NBNS_periods) / int(NBNS_weight)
            division_weight.insert(22, 'NBNS', division)

        elif i == "SMTP_IMF_IMF":
            SMTP_IMF_IMF_weight = sum_weight.iloc[:, 23]
            SMTP_IMF_IMF_periods = sum_periods.iloc[:, 23]
            division = SMTP_IMF_IMF_periods / SMTP_IMF_IMF_weight
            division_weight.insert(23, 'SMTP_IMF_IMF', division)

        elif i == "GTP":
            GTP_weight = sum_weight.iloc[:, 24]
            GTP_periods = sum_periods.iloc[:, 24]
            division = GTP_periods / GTP_weight
            division_weight.insert(24, 'GTP', division)

        elif i == "TPM":
            TPM_weight = sum_weight.iloc[:, 25]
            TPM_periods = sum_periods.iloc[:, 25]
            division = TPM_periods / TPM_weight
            division_weight.insert(25, 'TPM', division)

    division_weight.to_csv("Public/division_weight.csv", sep=",", index=False)
