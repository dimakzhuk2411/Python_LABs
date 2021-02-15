def set_up(tense):
    tense = tense.split()
    for i, w in enumerate(tense):
        if w[0].isupper():
            tense[i] = w.upper() 
    return ' '.join(tense)

print(set_up('Dfkjd, dfsdf . Sdfs'))