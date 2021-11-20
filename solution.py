

def solution(l):

    input_data_array = []

    for entry in l:

        original = entry
        dec = 0
        mil_place = ''
        mil_place_list = []
        replace_char = 'x'
        output = ''
        period = '.'
        period_count = entry.count(period)
        if period_count == 1:
            entry = entry + '.x'
            dec = 1
        elif period_count == 0:
            entry = entry + '.x.x'
            dec = 1001
        else:
            pass

        entry = entry.replace(replace_char, '0')

        mil_place_split = entry.split('.')

        for x in mil_place_split:
            mil_place_list.append(x.zfill(3))

        mil_place = int(mil_place.join(mil_place_list)) - dec
        
        new_entry = [original, entry, dec, mil_place]

        input_data_array.append(new_entry)
        
    input_data_array.sort(key = lambda x: x[3])

    for x in range(len(input_data_array)):
        output = output + input_data_array[x][0] + ','

    output = output[:-1]

    print(output)



# solution(['1', '1.2', '0.3.2'])
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])






