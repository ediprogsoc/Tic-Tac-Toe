# Please send us an email if there is anything you do not understand!

# Counting Characters
number_of_a = 0
for letter in 'supercalifragilisticexpialidocious':
    if letter == 'a':
        number_of_a += 1
print(number_of_a)

# FizzBuzz
for number in range(1,101):
    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
    
# Square List
sq_list = []
for number in range(1,21):
    sq_list.append(number**2)
for num in sq_list:
    if num % 2 == 1:
        print(num)
    
# Alternative (Don't worry if you don't understand this just yet!)
print(list(filter(lambda x : x % 2 == 1, [(i+1)**2 for i in range(20)])))

# Infinite Road
road = [0,0,0,1,0,1,1,0,0,1]
for i in range(10):
    road_copy = list(road)
    for c in range(10):
        road_copy[c] = road[(c-1) % 10]
    road = list(road_copy)
    print(road)
  
  # Simulating Radioactivity


p = - lamda*delta_t
atoms = [0 for i in range(1000)]
half_life = 0
decayed_count = 0
while decayed_count < 500:
    for atom in range(len(atoms)):
        if atoms[atom] == 0:
            rand = randomNumber()
            if rand <= p:
                atoms[atom] = 1
                decayed_count += 1
    half_life += delta_t
print(half_life)
