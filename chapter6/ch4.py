string_to_split = "Where now? Who now? When now?"
splited_string_in_a_list = string_to_split.split("? ")
splited_string_in_a_list[0] = splited_string_in_a_list[0]+"?"
splited_string_in_a_list[1] = splited_string_in_a_list[1]+"?"
print(splited_string_in_a_list)