def user_info(name, surname, b_year, city, email, cell):
    return f'User info: {name} {surname}, year of birth {b_year}, city {city}, email {email}, phone number {cell}'


name = input('input name:\n')
surname = input('input surname:\n')
b_year = input('input year of birth:\n')
city = input('input city:\n')
email = input('input email:\n')
cell = input('input cell number:\n')
info = user_info(name=name, surname=surname, b_year=b_year, city=city, email=email, cell=cell)
print(info)