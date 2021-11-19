

def outputter(list_input):

    input_data_array = []

    for x in list_input:
        
        three_x = ''
        three_dig = ''
        dec = 0
        mil_place = ''

        # check for number of periods in string
        # if no periods in str, add '.x.x'
        period = '.'
        if period in x:
            x = x + '.x'
            print('period')
        else:
            print('else')
        # if 1 period in str, add '.x'


        # decrement from num of 'x'

        # convert three_x to three_dig , replace x with 0

        # find mil_place from three_dig
        # split on period
        # fill left index with 0 to three places
        # rejoin
        
        # perform decrement operation

        # sort list_input by mil_place


        new_entry = [x, three_dig, dec, mil_place]


        input_data_array.append(new_entry)


    output = input_data_array
    print(output)




outputter(['1', '1.2', '0.3.2'])






