finish = False
while finish == False:
    result = 'acceptable'
    pw = input()
    pw_lst = list(pw)
    if pw == 'end':
        finish = True
    else:

        # 1. 모음(a, e, i, o, u) 하나를 반드시 포함하여야 한다.
        vowel = ['a', 'e', 'i', 'o', 'u']
        for v in vowel:
            if v in pw:
                # 2, 3단계 검증
                # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
                mo = 0
                ja = 0
                while pw_lst != []:
                    if pw_lst.pop() in vowel:
                        mo += 1
                        ja = 0
                        if mo >= 3 or ja >= 3:
                            result = 'not acceptable'
                            print(f'<{pw}> is {result}.')
                            break
                    else:
                        mo = 0
                        ja += 1
                        if mo >= 3 or ja >= 3:
                            result = 'not acceptable'
                            print(f'<{pw}> is {result}.')
                            break

                else:
                    # 3단계 검증
                    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo 는 허용한다.
                    for i in range(len(pw) - 1):
                        if pw[i] == pw[i + 1]:
                            if pw[i] == 'e' or pw[i] == 'o':
                                pass
                            else:
                                result = 'not acceptable'
                                print(f'<{pw}> is {result}.')
                                break
                    else:
                        print(f'<{pw}> is {result}.')
                    break

                break
        else:
            result = 'not acceptable'
            print(f'<{pw}> is {result}.')