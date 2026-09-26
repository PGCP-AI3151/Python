
def make_ing_form(verb):
    words = {}
    for i in verb:

        if i.endswith('ie'):
            words[i] = i[:len(i)-2] + 'ying'

        elif i.endswith('e'):
            words[i] = i[:len(i) - 1] + 'ing'

        else :
            words[i] = i + 'ing'

    return words

if __name__ == '__main__':
    verbs = ['Evaluate','wake','carrie','go']
    print(make_ing_form(verbs))