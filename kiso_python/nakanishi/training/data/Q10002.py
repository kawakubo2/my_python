from input_utils import input_non_negative_float

def bmi(weight, height):
    return weight / (height / 100) ** 2

low = 18.5
high = 25


def result(bmi):
    if (bmi < low):
        return "低体重"
    elif (bmi < high):
        return "適正体重"
    else:
        return "肥満"

weight = input_non_negative_float("体重(kg)")
height = input_non_negative_float("身長(cm)")
bmi_value = bmi(weight, height)
print(f"判定: BMI値: {bmi_value:.1f} 結果: {result(bmi_value)}")