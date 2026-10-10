def hello():
    print("Привет!")

hello()
hello()
hello()

def greet(name):
    print("Привет,", name, "!")

greet("Иван")
greet("Алексей")
greet("Димитрий")

def add(a, b):
    result = a + b
    print("Сумма:", result)

add(3, 5)
add(10, 20)

def apply_damage(health, damage):
    print("Ты получаешь урон", damage, "!")
    return health - damage

def heal(health, amount):
    print("Ты восстанавливаешь", amount, "здоровья.")
    return health + amount

health = 100
print("Начальное здоровье:", health)

health = apply_damage(health, 30)
print("После удара:", health)

health = heal(health, 20)
print("После лечения:", health)

apply_damage(health, 10)
