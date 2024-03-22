user_phrase = input()
char = user_phrase[0]

if char in user_phrase:
    if user_phrase.count(char) > 2:
        print(f'{user_phrase.count(char)-1} {char}\'s')
    elif user_phrase.count(char) == 1:
        print(f'0 {char}\'s')
    else:
        print(f'{user_phrase.count(char)-1} {char}')
