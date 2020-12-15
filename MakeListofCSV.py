def format_words(words):
    #first remove commas if any
    for item in words or []:
        if item == ',':
            for item in range(words.count(',')):
               words.remove(',')
        else:
            pass
    #then remove spaces if any
    for item in words or []:
        if item == '':
            for item in range(words.count('')):
                words.remove('')
        else:
            pass
    if not words:
        return ''
    else:
        result = ''
        y = len(words)
        count = 0
        for x in words:
            if y == 1:
                result += x
            #adding first word to result if it's not the only word
            elif count == 0 and count < y-1:     
                result += str(x)
                count += 1
            elif count > 0 and count < y-1 and x != ',': 
                #result += ', '.join(map(str, words))
                result += ', ' + str(x)
                count += 1
            else:
                result += ' and ' + str(words[y-1])
        return (result)
print (format_words(['ninja', 'samurai', 'ronin']))
