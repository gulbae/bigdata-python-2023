from faker import Faker

dummy = Faker('ko-KR')
print(dummy.name())
print(dummy.address())
print(dummy.company())

dummy_data = [(dummy.name(), dummy.postcode(), dummy.address(),
               dummy.phone_number(), dummy.email()) for i in range(100)]

print(dummy_data)