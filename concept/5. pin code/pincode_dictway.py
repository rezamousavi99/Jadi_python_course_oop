def sum_argham(ramz_digit):
    sum_argham = 0
    for k in ramz_digit:
        sum_argham += ramz_digit[k] 
    return sum_argham

def ramz_is_ok(ramz_digit):
    condition1 = ramz_digit['se'] + ramz_digit['panj'] == 14
    condition2 = ramz_digit['yek'] == (2 * ramz_digit['do']) - 1
    condition3 = ramz_digit['chahar'] == ramz_digit['do'] + 1
    condition4 = ramz_digit['do'] + ramz_digit['se'] == 10
    condition5 = sum_argham(ramz_digit) == 30

    if condition1 and condition2 and condition3 and condition4 and condition5:
            return True



for i in range(0, 100000):
    ramz = str(i).zfill(5)

    ramz_dict = dict()
    ramz_dict['yek'] = int(ramz[0])
    ramz_dict['do'] = int(ramz[1])
    ramz_dict['se'] = int(ramz[2])
    ramz_dict['chahar'] = int(ramz[3])
    ramz_dict['panj'] = int(ramz[4])
    
    if ramz_is_ok(ramz_dict):
        print(i)
