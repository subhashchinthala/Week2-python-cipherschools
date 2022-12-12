# functions practice
def last_char(name):
    return name[-1]

print(last_char("dhoni sachin"))
# # last_char(9) # error

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_even(9))