def dec_to_bin(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

def dec_to_hex(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = hex_chars[n % 16] + result
        n = n // 16
    return result

# 主程式
try:
    num = int(input("請輸入0-255: "))
    
    if num < 0 or num > 255:
        print("請輸入0到255之間的數字")
    else:
        print("Binary:", dec_to_bin(num))
        print("Decimal:", num)
        print("Hex:", dec_to_hex(num))

except:
    print("輸入錯誤")
