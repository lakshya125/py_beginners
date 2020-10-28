
def dec_to_binary(nmbr):
    if nmbr == 0:
        return 0
    else:
        return nmbr % 2 + 10 * dec_to_binary(int(nmbr // 2))

# take the T (test_cases) input
print("enter test_cases")
test_cases = int(input("T = "))
if 1 <= test_cases <= 25:
  
    lizt = []
    for case in range(1, test_cases + 1):
        # take the n input values
        n = int(input("Number: "))
        if 1 < n < 255:
            lizt.append(n)
    for ans in lizt:
        bin_num = dec_to_binary(ans)
        x = str(bin_num)
        if len(x) <= 8:
            s = "0" * (8 - len(x)) + x
            print("Binary value for case",ans,":"  + s)

else:
    print("Gone beyond constraints. Rerun code.")
