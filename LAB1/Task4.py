tense = str(input())
tense_arr = tense.split( )
for j in tense_arr:
    if len(j) >= 7:
        print(j + ", ")
    elif len(j) > 4:
        if len(j) < 7:
            print(j + ", ")
