string = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
total = sum(map(lambda x: 65-ord(x) + 4, string))

print(total)
