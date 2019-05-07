def wrap_text(text, symbol):
    return symbol + text + symbol

print(wrap_text("hello", "==="))

symbol = "---===###"
text = "new message"
print(f"{symbol}{text}###===---")