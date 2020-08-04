import datetime


def checkSumCal(srecIn):
    # Motorla srec checksum calculator

    srec = srecIn

    hexSum = 0
    for i in range(2, len(srec), 2):
        currentByte = srec[i:i+2]
        currentByte = int(currentByte, 16)
        hexSum = hexSum + currentByte
        # print(hex(currentByte))

    print(hex(hexSum))

    dummyHex = 0xFF

    # last significant dig
    lsgHex = str(hex(hexSum))[-2:]
    lsgHex = int(lsgHex, 16)

    # check sum Hex
    csHex = dummyHex - lsgHex
    csHex = str(hex(csHex))
    csHex = csHex[2:].zfill(2).upper()
    print('CheckSum: ' + csHex)

    return csHex


def char2hex(charIn):
    # convert ASCII char to hex format
    letter = charIn
    # letter = hex(ord(charIn))
    letter = letter.encode('utf-8')
    return letter.hex().upper()


def dateString():
    # date string gen function
    dateToday = datetime.date.today()
    dateTodayUS = dateToday.strftime("%m%d%Y")
    dateTodaySTD = dateToday.strftime("%Y%m%d")

    return dateTodayUS


# debug section
# checkSumCal("S315A032C02000000000000040400000A04000004040")
# checkSumCal("S315A032C01047414835303000000000000012345678")
# print(dateString())
