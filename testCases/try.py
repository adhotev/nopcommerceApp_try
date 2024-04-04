from faker import Faker

fake = Faker()

# check this out for everything we can generate with faker
# https://medium.com/@HeCanThink/faker-python-is-just-a-fake-away-ef626a0dcf8d

# print(fake.first_name())
#
# l=[]
# for i in range(100):
#     l.append(fake.unique.first_name())
# print(l)
# print(len(l))
# s=set(l)
# print(s)
# print(len(s))

print(fake.first_name())
print(fake.last_name())
print(fake.email())
print(fake.company_email())
print(fake.password())
print(fake.date(pattern='%d/%m/%Y'))
print(fake.date_of_birth(minimum_age=18,maximum_age=100).strftime("%d/%m/%Y"))
print(fake.company_email())
print(fake.company())
print(fake.text())




