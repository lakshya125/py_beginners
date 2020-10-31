def reverseWords(s):
    result = ""
    words = []
    curr_word = ""
    
    for i in range(len(s)):
        if(s[i] == '.'):
            words.append(curr_word)
            curr_word = ""
        else:
            curr_word += s[i]
    
    words.append(curr_word)
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if(i):
            result += "."

    return result
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))
    
    
