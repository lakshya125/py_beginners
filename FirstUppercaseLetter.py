def firstUpperCase(str):
    for i in range(0, len(str)):
        if (str[i].istitle()):
            print(str[i])
            return str[i]
    print("No uppercase letter")
    return 0

if __name__ == "__main__":
    word = "helloWorld"
    result = firstUpperCase(word)
