# 모음 하나 포함 a, e, i, o, u
# 모음이나 자음이 연속 3개가 오면 안됨
# 같은 글자 연속 2개 x 단, ee와 oo는 허용
word = input()

if len(word) < 1 or len(word) > 20:
    print(f'<{word}> is not acceptable')
else:
    consecutive_vowels = False
    consecutive_letters = False
    prev_char = ''
    prev_vowel = False
    has_vowel = False

    for char in word:
        if char in 'aeiou':
            has_vowel = True
            if prev_vowel:
                consecutive_vowels = True
                break
            prev_vowel = True
        else:
            prev_vowel = False

        if char == prev_char and char not in 'eo':
            consecutive_letters = True
            break
        prev_char = char

    if not has_vowel or consecutive_vowels or consecutive_letters:
        print(f'<{word}> is not acceptable')
    else:
        print(f'<{word}> is acceptable')

