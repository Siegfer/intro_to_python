unique_colors = ['red', 'yellow', 'red', 'green', 'red', 'red', 'yellow']
subscribed_emails = ['mary@gmail.com', 'opal@gmail.com',
                     'mary@gmail.com', 'sayed@gmail.com']
print(unique_colors)

unique_colors_set = {'green', 'yellow', 'red'}
subscribed_emails_set = {'mary@gmail.com', 'opal@gmail.com', 'sayed@gmail.com'}
print(unique_colors_set)

unique_colors_set = {'green', 'yellow', 'red'}
subscribed_emails_set = {'mary@gmail.com', 'opal@gmail.com', 'sayed@gmail.com'}
print(unique_colors_set)

# my_set = set(a_list_to_convert)
unique_colors_list = ['red', 'yellow', 'red', 'green', 'red', 'yellow']
unique_colors_set = set(unique_colors_list)
print(unique_colors_list)

# In a list:
clothing_list.append('red')

# In a set:
clothing_set.add('red')

# In a list:
clothing_list.pop()  # Removes and returns the last item in the list.
# Removes and returns a specific (here, the first) item in the list.
clothing_list.pop(0)

# In a set
clothing_set.pop()  # No! This is unreliable! The order is arbitrary.
clothing_set.pop(0)  # No! Python throws an error! You can't index sets.
clothing_set.remove('red')  # Do this! Call the element directly!
