

def solution(l):

    input_data_array = []

    for entry in l:

        original = entry
        decrement = 0
        mil_place = ''
        mil_place_list = []
        replace_char = 'x'
        output = ''
        period = '.'
        period_count = entry.count(period)
        if period_count == 1:
            entry = entry + '.x'
            decrement = 1
        elif period_count == 0:
            entry = entry + '.x.x'
            decrement = 1001
        else:
            pass

        entry = entry.replace(replace_char, '0')

        mil_place_split = entry.split('.')

        for x in mil_place_split:
            mil_place_list.append(x.zfill(3))

        mil_place = int(mil_place.join(mil_place_list)) - decrement
        
        new_entry = [original, entry, decrement, mil_place]

        input_data_array.append(new_entry)
        
    input_data_array.sort(key = lambda x: x[3])

    for x in range(len(input_data_array)):
        output = output + input_data_array[x][0] + ','

    output = output[:-1]

    print(input_data_array)

# END of document 
