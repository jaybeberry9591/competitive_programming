s = str.lower(input())

replace_dict = {
    
    'a' : '',
    'b' : '.b',
    'c' : '.c',
    'd' : '.d',
    'e' : "",
    'f' : '.f',
    'g' : '.g',
    'h' : '.h',
    'i' : "",
    'j' : ".j",
    'k' : '.k',
    'l' : '.l',
    'm' : '.m',
    'n' : ".n",
    'o' : '',
    'p' : '.p',
    'q' : '.q',
    'r' : '.r',
    's' : '.s',
    't' : '.t',
    'u' : '',
    'v' : '.v',
    'w' : '.w',
    'x' : '.x',
    'y' : '',
    'z' : '.z'
}
s_list = []
for i in s:
#     print(i)
#     print(replace_dict[i])
    s_list.append(replace_dict[i])
#     s_new = s_new.join(replace_dict[i])
# #     s.replace(i, replace_dict[i])
    
# print(s_new)

# print(s_list)
print(''.join(s_list))
