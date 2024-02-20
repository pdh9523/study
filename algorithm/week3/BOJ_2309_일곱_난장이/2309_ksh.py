dwarf = [int(input()) for _ in range(9)]

for fir in range(9):   # 첫번째 난쟁이 제외
    dwarf2 = dwarf[:fir] + dwarf[(fir + 1):]
    if sum(dwarf2) > 100:   # 두번째 난쟁이 찾기
        sec = sum(dwarf2) - 100
        if sec in dwarf2:
            dwarf.pop(fir)
            dwarf.pop(dwarf.index(sec))
            dwarf.sort()
            for i in range(7):   # 출
                print(dwarf[i])
            break력