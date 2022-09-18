
def find_sigfigs(num):
    num = repr(float(num))
    parts = num.split('.')
    whole_num = parts[0].lstrip('0')

    if len(parts) == 2:
        decimal_num = parts[1].rstrip('0')
        return len(whole_num) + len(decimal_num)

    return len(whole_num)


print('38.4258: %a' % find_sigfigs(38.4258))
print('0.66385: %a' % find_sigfigs(0.66385))
