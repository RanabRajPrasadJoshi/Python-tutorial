from pyexpat.errors import messages


def emoji_store(messages):
    message_list = messages.split(" ")
    out = ""
    emojies = {
        ":)" : "😂",
        ":(" : "🥲"
    }
    for words in message_list:
        out += emojies.get(words,words) + " "

    return out



messages = input(">")
print(emoji_store(messages))