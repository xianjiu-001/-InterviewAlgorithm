s1 = '11110001010001'
s2 = ""
s3 = "1"

def func(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        count = 1
        pre = s[0]
        for i in s:
            if i != pre:
                pre = i
                count += 1
        return count


print(func(s3))
