Dictionary={'Rohit':75,'Virat':90,'Rani':66,'Surajit':81, 'Dip':94 }
name=input('Enter the students name: ')

marks=(Dictionary.get(name))
if marks is not None:
    print(f"{name}'s marks: {marks}")
else:
    print(f"{name} not found")
