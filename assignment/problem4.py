# 4. Write a python program for the requirement below. Notice the output must be in sorted order -
# Input  : x3b4U5i2
# Output : bbbbiiUUUUUxxx

s ="x3b4U5i2"
length = len(s)
output=""
for i in range(length-1):
    if (s[i].isdigit()!= True):
        if (s[i+1].isdigit()==True):
            number = int(s[i+1])
            for j in range(number):
                output+=s[i]
        else:
            output+=s[i]

result = ''.join(sorted(output.lower()))
print(result)
