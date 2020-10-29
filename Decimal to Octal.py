def dec_to_octal(nmbr):
    if nmbr == 0:
        return 0
    else:
        return nmbr % 8 + 10 * dec_to_octal(int(nmbr // 8))

# take the T (test_cases) input
print("enter test_cases")
test_cases = int(input("T = "))
if 1 <= test_cases <= 25:
    lizt = []
    for case in range(1, test_cases + 1):
        n = int(input("Number: "))
        if 1 < n < 255:
            lizt.append(n)
    for ans in lizt:
        octal_num = dec_to_octal(ans)
        x = str(octal_num)
        if len(x) <= 8:
            s = "0" * (8 - len(x)) + x
            print("Binary value for case",ans,":"  + s)
else:
    print("Gone beyond constraints. Rerun code.")
