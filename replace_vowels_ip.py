s ='aetousp'

new_string = ''
vowels = 'AEIOUaeiou'
i =0
while i < len(s):
    if s[i] in vowels:
        new_string += str(i)
    else:
        new_string += s[i]

    i += 1
print(new_string)
