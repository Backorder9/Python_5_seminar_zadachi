'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc
'''

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

with open('compress.txt', 'r') as data:
    abracadabra = data.readline()

abr_encode = rle_encode(abracadabra)
write_file('decompress.txt', abr_encode)

with open('decompress.txt', 'r') as data:
    st3 = data.readlines()

print(f"{abracadabra} -> {st3}")
