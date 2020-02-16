def bmi(weight, height):
    bmi_calc = weight / height ** 2
    
    return {bmi_calc > 30 : "Obese",
            bmi_calc <= 30.0 : "Overweight",
            bmi_calc <= 25.0 : "Normal",
            bmi_calc <= 18.5 : "Underweight"
            }[True]


# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]