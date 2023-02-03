'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc
'''
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open('compressed.txt', 'r') as data:
    abr = data.readline()

abr_decode = rle_decode(abr)
write_file('decompressed.txt', abr_decode)

with open('decompressed.txt', 'r') as data:
    st3 = data.readlines()

print(f"{abr} -> {st3}")
