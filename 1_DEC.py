####################day 1####################
#problem 1
def d1p1(filename):
    number_list = []
    number_list_2 = []
    with open(filename) as f:
        for line in f:
            number_list.append(int(line.strip()))
    number_list_2 = number_list
    for i in number_list:
         sub = 2020 - i
         for num in number_list_2:
             if num == sub:
                answer = num * i    
                return answer
#x = problem_1_('problem_1.txt')

#problem 2
def d1p2(filename):
    number_list = []
    number_list_2 = []
    number_list_3 = []
    with open(filename) as f:
        for line in f:
            number_list.append(int(line.strip()))
    number_list_2 = number_list
    number_list_3 = number_list
    for num_1 in number_list:
         for num_2 in number_list_2:
             for num_3 in number_list_3:
                 if num_1 + num_2 + num_3 == 2020:
                     return (num_1 * num_2 * num_3)
#x = problem_2_('day_1.txt')
####################day 2####################
#problem 1
def d2p1(filename):
    full_list = []
    total_count = 0
    with open(filename) as f:
        for line in f:
            stripped_line = line.strip()
            a,b,c,d = stripped_line.replace('-', ' ').replace(':', '').split()
            full_list.append([int(a), int(b), c, d])
    for password_check in full_list:
        counter = 0
        for i in password_check[3]:
            if i == password_check[2]:
                counter += 1
        if counter >= password_check[0] and counter <= password_check[1]:
            total_count +=1
    return total_count
# x = d2p1('day_2.txt')
# print(x)
#problem 2
def d2p2(filename):
    full_list = []
    new_counter = 0
    with open(filename) as f:
        for line in f:
            stripped_line = line.strip()
            a,b,c,d = stripped_line.replace('-', ' ').replace(':', '').split()
            full_list.append([int(a), int(b), c, d])
    for password_check in full_list:
        counter = 0
        new_list = []
        for i in password_check[3]:
            counter += 1
            if i == password_check[2]:
                new_list.append(counter) 
        if password_check[0] in new_list and password_check[1] in new_list:
            pass
        elif password_check[0] in new_list:
            new_counter += 1
        elif password_check[1] in new_list:
            new_counter += 1
        else:
            pass
    return new_counter
# x = d2p2('day_2.txt')
# print(x)
####################day 3####################
#problem 1
def d3p1(filename):
    slope = []
    with open(filename) as f:
        for line in f:
            line = line.strip()*200
            slope.append(line.strip())
    position = -3
    trees = 0
    for i in slope:
        position += 3
        if i[position] == '#':
                trees += 1
    return trees
# x = d3p1('day_3.txt')
# print(x)
#problem 2 #167, 53, 54,67, 23
def d3p2(filename):
    slope = []
    with open(filename) as f:
        for line in f:
            line = line.strip()*200
            slope.append(line.strip())
    position = -1          #change for each case
    trees = 0
    slope = slope[::2]       #down 2
    for i in slope:
        position += 1 #change for each case
        if i[position] == '#':
                trees += 1
    return trees
# w = 167*53*54*67*23
# print(w)
# x = d3p2('day_3.txt')
# print(x)
####################day 4####################
#problem 1
def d4p1(filename):
    all_passports = []
    with open(filename) as f:
        a_passport = []
        for line in f: 
            if line != '\n':
                line = line.strip().replace(':', ' ')
                a_passport.append(line.split())
            else:
                all_passports.append(a_passport)
                a_passport = []
        all_passports.append(a_passport)
    all_passports_new = []
    for big_list in all_passports:
        joined_list = []
        for small_list in big_list:
            joined_list += small_list
        all_passports_new.append(joined_list)
    total_valid = 0
    for full_characteristics in all_passports_new:
        running_count = 0
        for z in full_characteristics:
            if z == 'byr' or z =='iyr' or z =='eyr' or z =='hgt' or z =='hcl' or z =='ecl' or z =='pid':
                running_count += 2
            elif z == 'cid':
                running_count += 1
        if running_count >= 14:
            total_valid +=1
    return total_valid
# y = d4p1('day_4_test.txt')
# print(y)
#problem 2
def d4p2(filename):
    all_passports = []
    with open(filename) as f:
        a_passport = []
        for line in f: 
            if line != '\n':
                a_passport.append(line.split())
            else:
                all_passports.append(a_passport)
                a_passport = []
        all_passports.append(a_passport)
    all_passports_new = []
    for big_list in all_passports:
        joined_list = []
        for small_list in big_list:
            joined_list += small_list
        all_passports_new.append(joined_list)
    dictionary_list = []
    for full_characteristics in all_passports_new:
        passport_dictionary = dict(s.split(':') for s in full_characteristics)
        dictionary_list.append(passport_dictionary)
        running_count = 0
    needed_characteristics = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hair_color= '0123456789abcdef'
    passport_id_numbers = '0123456789'
    total_valid = 0
    for each_dictionary in dictionary_list:
        running_count = 0
        new_valid = 0
        for key in each_dictionary.keys():
            if key in needed_characteristics:
                running_count += 2
            elif  key == 'cid':
                running_count += 1
        if running_count >= 14:
            hair_color_value = each_dictionary['hcl']
            height_value = each_dictionary['hgt']
            if int(each_dictionary['byr']) >= 1920 and int(each_dictionary['byr']) <= 2002:
                new_valid +=1
            if int(each_dictionary['iyr']) >= 2010 and int(each_dictionary['iyr']) <= 2020:
                new_valid +=1
            if int(each_dictionary['eyr']) >= 2020 and int(each_dictionary['eyr']) <= 2030:
                new_valid +=1
            if  len(each_dictionary['pid']) == 9 and each_dictionary['pid'][0] in passport_id_numbers and each_dictionary['pid'][1] in passport_id_numbers and each_dictionary['pid'][2] in passport_id_numbers and each_dictionary['pid'][3] in passport_id_numbers and each_dictionary['pid'][4] in passport_id_numbers and each_dictionary['pid'][5] in passport_id_numbers and each_dictionary['pid'][6] in passport_id_numbers and each_dictionary['pid'][7] in passport_id_numbers and each_dictionary['pid'][8] in passport_id_numbers: 
                new_valid +=1
            if each_dictionary['ecl'] in eye_color:
                new_valid +=1
            if len(hair_color_value) == 7 and hair_color_value[0] == '#' and hair_color_value[1] in hair_color and hair_color_value[2] in hair_color and hair_color_value[3] in hair_color and hair_color_value[4] in hair_color and hair_color_value[5] in hair_color and hair_color_value[6] in hair_color:
                new_valid +=1
            if height_value[-2:] == 'cm' and int(height_value[:-2]) >= 150 and int(height_value[:-2]) <= 193:
                new_valid +=1
            if height_value[-2:] == 'in' and int(height_value[:-2]) >= 59 and int(height_value[:-2]) <= 76:
                new_valid +=1
        if new_valid == 7:
            total_valid +=1
    return total_valid     
# x = d4p2('day_4.txt')
# print (x)
####################day 5####################
#problem 1

# def d5p1(filename):
#     row = list(range(0,128))
#     all_seats = []
#     with open(filename) as f:
#         for line in f:
#             all_seats.append(line.strip())
#     for seat in all_seats:
#         row = row
#         range_of_seats = int(len(row))
#         for character in seat[0:7]:
#             if character == 'F':
#                 range_of_seats = range_of_seats[0:range_of_seats//2]
#             elif character == 'B':
#                 range_of_seats = range_of_seats[range_of_seats//2:range_of_seats]
#         return range_of_seats
# x = d5p1('day_5_test.txt')
# print (x)
def d5p1(filename):
    row = list(range(0,128))
    all_seats = filename
    for seat in all_seats:
        row = row
        range_of_seats = len(row)
        for character in seat[0:7]:
            if character == 'F':
                range_of_seats = range_of_seats[0:range_of_seats//2]
            elif character == 'B':
                range_of_seats = range_of_seats[range_of_seats//2:range_of_seats]
        return range_of_seats
x = d5p1(['FFBBBFBLRL', 'BFFFBFBRRR', 'BFFFBFBLRL', 'BFFBFBBLRR', 'BBFFBFFRLL'])
print (x)