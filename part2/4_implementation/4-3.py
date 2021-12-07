input_data = input()
row = input_data[1]

#ord('a'): 특정한 한 문자를 아스키 코드 값(=숫자형태)으로 변환해 주는 함수 
#a -> 97, b -> 98, c -> 99
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if next_row >= 1 and next_row <= 8 and  next_col >= 1 and next_col <= 8:
        count += 1

print(count)