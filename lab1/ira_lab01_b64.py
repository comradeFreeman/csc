def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def to_b64 (num):
    # count = 0
    # count2 = 0
    bits = text_to_bits(num)
    ####
    len_po_8 = int(len(bits) / 8)
    ####
    print(len(bits)/6)
    # замена первым 11-ти строчкам внизу
    ####
    bysix = [bits[i:i + 6] # + ('0' * (len(bits) - i - 2) if len(bits) - i - 1 < 6 else '' ) # можно так ещё, но не нужно :)
              for i in range(0, len(bits), 6)]
    bysix[-1] += '0' * (6 - len(bysix[-1])) # так красивее, чем в закомм. куске выше. замена след. 4-ём строкам.
    ####

    # работает, но сложно. и мне кажется, что в таком коде возможны баги. можно гораздо проще
    # bysix = [[]]
    # for i in bits:
    #     if ((count2 == 0 and count == 6) or (count2 != 0 and count == 5)):
    #         bysix.append([])
    #         count = 0
    #         count2 +=1
    #         bysix[count2].append(i)
    #     else:
    #         bysix[count2].append(i)
    #         count +=1
    # for i in range(len(bysix)):
    #     bysix[i] = ''.join(map(str, bysix[i]))
    #
    # if len(bysix[len(bysix) - 1]) != 6:
    #     add = 6 - len(bysix[len(bysix) - 1])
    #     bysix[len(bysix) - 1] += '0'*add

    print(bysix)
    pull = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    ####
    cod = ''.join([pull[int(i, 2)] for i in bysix]) # так же короче.. замена 3-ём строкам ниже.
    ####

    #cod = ''
    #for i in bysix:
    #    cod += pull[int(i, 2)]

    ####
    add = 0
    while ((len_po_8 + add) % 3 != 0):
        add += 1
    ####


    #cod += '=' * (int(add / 2))
    # неверно! кол-во '=' не имеет никакого отношения к кол-ву добавленных нулей к посл. 6-ти битному набору
    #print(cod) покажем дальше
    return cod + '=' * add


file_name = input("Enter file name: ")
with open(file_name, 'r', encoding='utf-8') as text:
    with open('your_file_inb64.txt', 'w') as text2:
        string = text.read()
        base64 = to_b64(string)
        ####
        print(base64)
        ####
        text2.write(base64)
        print(len(string), len(base64))
