ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


# A list is a mutable sequence
ft_list[1] = "World!"
# ft_list.remove("tata!")
# ft_list.append("World!")

# A tuple is an immutable sequence
ft_tuple = ("Hello", "France!")

# A set is an unordered collection of unique elements
# ft_set = {"Hello", "Paris!"}
ft_set.remove("tutu!")
ft_set.add("Paris!")

# A dict is an unordered collection of key/value pairs
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
