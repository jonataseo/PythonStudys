string_to_slice_before_comma = "It was bright cold day in April, and the clocks were striking thriteen."
index_of_comma = string_to_slice_before_comma.index(",")
string_sliced = string_to_slice_before_comma[index_of_comma:]
print(string_sliced)