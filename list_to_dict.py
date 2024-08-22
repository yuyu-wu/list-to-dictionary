# List to Dictionary Exercise
# Given a person variable:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 

# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value: {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'} 

answer = {}
for i in person:
    k = i[0]
    # print(k)
    v = i[1]
    # print(v)
    answer.update({k: v})

print(answer)

# Using a dictionary comprehension:
# answer = {thing[0]: thing[1] for thing in person}

# An alternate solution using a dict comprehension, without any references to list indexes:
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}

# Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = dict(person)