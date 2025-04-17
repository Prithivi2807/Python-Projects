message = input("> ")
words = message.split(' ')
emojis ={
    ":)" : "😊",
    ":(": "😞"
}
output=""
for symbol in words:
    output += emojis.get(symbol, symbol) + " "
print(output)