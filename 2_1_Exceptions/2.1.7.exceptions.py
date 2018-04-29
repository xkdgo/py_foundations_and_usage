#!/usr/bin/python3.6

exc_range = input()
result_dict = {}

for i in range(int(exc_range)):
    exc = input().split(':')
    if len(exc) == 1:
        if exc[0] not in result_dict:
            result_dict[exc[0]] = []
    if len(exc) == 2:
        key_list = exc[1].split()
        for key in key_list:
            if key in result_dict:
                result_dict[key].append(exc[0].strip())
            else:
                result_dict[key] = [exc[0].strip()]
                
copy_dict = result_dict.copy()

for key in copy_dict:
    for item in copy_dict[key]:
        if item in copy_dict.keys():
            result_dict[key] += result_dict[item]


final_deny_list = []
deny_list = []


exc_range = input()
for i in range(int(exc_range)):
    exc = input()
    if exc in deny_list and exc not in final_deny_list:
        final_deny_list.append(exc)
        if exc in result_dict:
            deny_list += result_dict[exc]
    elif exc in result_dict:
        deny_list += result_dict[exc]
    else:
        pass
        #print("Hmm something wrong")

for item in final_deny_list:
    print(item)
