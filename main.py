import tkinter as tk

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

def convert():
    try:
        num = int(entry.get())
        
        if num < 0 or num > 255:
            result_label.config(text="請輸入0-255")
            return
        
        b = dec_to_bin(num)
        h = dec_to_hex(num)

        result_label.config(
            text=f"Binary: {b}\nDecimal: {num}\nHex: {h}"
        )
        
    except:
        result_label.config(text="輸入錯誤")

# 建立視窗
root = tk.Tk()
root.title("Binary / Decimal / Hex Converter")

# 輸入框
entry = tk.Entry(root)
entry.pack()

# 按鈕
btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

# 顯示結果
result_label = tk.Label(root, text="")
result_label.pack()

# 啟動程式
root.mainloop()
