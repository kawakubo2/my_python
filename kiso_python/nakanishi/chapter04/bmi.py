weight = float(input("体重(kg): "))
height = float(input("身長(m): "))

def bmi(weight, height):
    return weight / height ** 2

print(f"体重が{weight:.1f}kg、身長が{height:.1f}mの場合BMI値は{bmi(weight, height):.1f}")

