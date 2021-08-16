string_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
string_from_list_using_join = " ".join(string_list)
string_correctly = string_from_list_using_join[0: -2] + "."
print(string_from_list_using_join)
print(string_correctly)