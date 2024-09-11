#Food Item class
class foodItem:
    def __init__(self, CarbsPer100gm, ProteinPer100gm, FatsPer100gm, VitaminAPer100gm, VitaminB1Per100gm, VitaminB2Per100gm, VitaminB3Per100gm, VitaminB6Per100gm, VitaminB12Per100gm, VitaminCPer100gm, VitaminDPer100gm, VitaminEPer100gm, VitaminKPer100gm, CalciumPer100gm, IronPer100gm):
        self.carbsPer100gm = float(CarbsPer100gm)
        self.proteinPer100gm = float(ProteinPer100gm)
        self.fatsPer100gm = float(FatsPer100gm)
        self.vitaminAPer100gm = float(VitaminAPer100gm)
        self.vitaminB1Per100gm = float(VitaminB1Per100gm)
        self.vitaminB2Per100gm = float(VitaminB2Per100gm)
        self.vitaminB3Per100gm = float(VitaminB3Per100gm)
        self.vitaminB6Per100gm = float(VitaminB6Per100gm)
        self.vitaminB12Per100gm = float(VitaminB12Per100gm)
        self.vitaminCPer100gm = float(VitaminCPer100gm)
        self.vitaminDPer100gm = float(VitaminDPer100gm)
        self.vitaminEPer100gm = float(VitaminEPer100gm)
        self.vitaminKPer100gm = float(VitaminKPer100gm)
        self.calciumPer100gm = float(CalciumPer100gm)
        self.ironPer100gm = float(IronPer100gm)

"""
food = foodItem(
    <CarbsPer100gm>,     # Replace with actual value for carbs in 100 grams
    <ProteinPer100gm>,   # Replace with actual value for protein in 100 grams
    <FatsPer100gm>,      # Replace with actual value for fats in 100 grams
    <VitaminAPer100gm>,  # Replace with actual value for Vitamin A in 100 grams
    <VitaminB1Per100gm>, # Replace with actual value for Vitamin B1 in 100 grams
    <VitaminB2Per100gm>, # Replace with actual value for Vitamin B2 in 100 grams
    <VitaminB3Per100gm>, # Replace with actual value for Vitamin B3 in 100 grams
    <VitaminB6Per100gm>, # Replace with actual value for Vitamin B6 in 100 grams
    <VitaminB12Per100gm>,# Replace with actual value for Vitamin B12 in 100 grams
    <VitaminCPer100gm>,  # Replace with actual value for Vitamin C in 100 grams
    <VitaminDPer100gm>,  # Replace with actual value for Vitamin D in 100 grams
    <VitaminEPer100gm>,  # Replace with actual value for Vitamin E in 100 grams
    <VitaminKPer100gm>,  # Replace with actual value for Vitamin K in 100 grams
    <CalciumPer100gm>,   # Replace with actual value for Calcium in 100 grams
    <IronPer100gm>       # Replace with actual value for Iron in 100 grams
)

"""

egg = foodItem(1.1, 12.6, 10.6, 0.140, 0.066, 0.500, 0.075, 0.170, 0.0011, 0.0, 0.002, 1.1, 0.0, 0.050, 1.2)
apple = foodItem(14, 0.3, 0.2, 0.0054, 0.00017, 0.00026, 0.00391, 0.000041, 0.00000, 0.0, 0.0, 0.00033, 0.0021, 0.006, 0.12)
banana = foodItem(22.8, 1.1, 0.3, 0.00064, 0.00031, 0.000073, 0.000665, 0.000367, 0.000001, 0.0, 0.0, 0.0010, 0.0005, 0.005, 0.26)
broccoli = foodItem(6.6, 2.8, 0.4, 0.00031, 0.000071, 0.000117, 0.000639, 0.000145, 0.0000002, 0.0892, 0.000009, 0.0008, 0.0001, 0.047, 0.73)
carrot = foodItem(9.6, 0.9, 0.2, 0.017, 0.000066, 0.000058, 0.00098, 0.000138, 0.000000, 0.057, 0.000001, 0.00066, 0.0001, 0.033, 0.30)
chickenBreast = foodItem(0.0, 31, 3.6, 0.000017, 0.000068, 0.000058, 0.014, 0.00056, 0.0000005, 0.0, 0.000002, 0.0002, 0.000002, 0.016, 0.90)
milk = foodItem(5.0, 3.4, 3.3, 0.000028, 0.000045, 0.000183, 0.000089, 0.000039, 0.0000004, 0.001, 0.000001, 0.00009, 0.000015, 0.113, 0.03)
orange = foodItem(12, 0.9, 0.1, 0.000225, 0.000087, 0.00004, 0.000429, 0.000060, 0.000000, 0.053, 0.0000001, 0.00018, 0.000001, 0.043, 0.10)
rice = foodItem(28, 2.7, 0.3, 0.000000, 0.000017, 0.000047, 0.0013, 0.00016, 0.000000, 0.000, 0.000001, 0.00004, 0.000001, 0.010, 1.2)
spinach = foodItem(3.6, 2.9, 0.4, 0.000469, 0.000078, 0.000189, 0.000724, 0.000195, 0.0000001, 0.028, 0.000007, 0.002, 0.000482, 0.099, 2.7)
strawberry = foodItem(7.7, 0.8, 0.3, 0.000012, 0.000024, 0.000022, 0.000386, 0.000047, 0.000000, 0.059, 0.000000, 0.00058, 0.00002, 0.016, 0.41)
tomato = foodItem(3.9, 0.9, 0.2, 0.000085, 0.000037, 0.000019, 0.000594, 0.000081, 0.000000, 0.138, 0.000000, 0.00054, 0.000007, 0.010, 0.27)
potato = foodItem(17, 2.0, 0.1, 0.000000, 0.000081, 0.000032, 0.0014, 0.000302, 0.000000, 0.0, 0.000000, 0.00001, 0.000002, 0.010, 0.81)
salmon = foodItem(0.0, 20.4, 13.4, 0.000043, 0.00022, 0.000109, 0.0086, 0.00104, 0.0000032, 0.0, 0.000018, 0.0025, 0.000004, 0.012, 0.34)
almonds = foodItem(21.7, 21.2, 49.9, 0.000002, 0.00024, 0.000713, 0.003743, 0.000137, 0.000000, 0.0, 0.000000, 0.025, 0.000007, 0.264, 3.7)
beef = foodItem(0.0, 26.1, 20.0, 0.000000, 0.00006, 0.000201, 0.0035, 0.000373, 0.0000026, 0.0, 0.000006, 0.0007, 0.000001, 0.012, 2.6)
cheese = foodItem(1.3, 24.9, 33.1, 0.000264, 0.000031, 0.000421, 0.0008, 0.000074, 0.000001, 0.0, 0.000000, 0.0003, 0.000021, 0.721, 0.70)
chickpeas = foodItem(27.4, 8.9, 2.6, 0.000027, 0.000228, 0.000212, 0.000493, 0.000139, 0.000000, 0.0, 0.000000, 0.0008, 0.000003, 0.105, 6.2)
peanuts = foodItem(16.1, 25.8, 49.2, 0.000001, 0.00008, 0.000135, 0.0135, 0.000274, 0.000000, 0.0, 0.000000, 0.0083, 0.000006, 0.092, 2.5)
walnuts = foodItem(13.7, 15.2, 65.2, 0.000001, 0.000341, 0.000151, 0.001125, 0.000537, 0.000000, 0.0, 0.000000, 0.0026, 0.000003, 0.098, 2.91)
yogurt = foodItem(3.6, 10.0, 3.3, 0.000013, 0.000034, 0.00017, 0.00031, 0.000035, 0.0000005, 0.0, 0.0000001, 0.00005, 0.000001, 0.121, 0.1)


#Fn to calculate required calories using BMR and activity level.
def requiredCaloriesFn(value, BMR):
    if value == 1:
        return BMR*(1.2)
    elif value == 2:
        return BMR*(1.375)
    elif value == 3:
        return BMR*(1.55)
    elif value == 4:
        return BMR*(1.725)
    elif value == 5:
        return BMR*(1.9)

#Inputing values   
gender = input("Enter Gender(M/F): ")

age = int(input("Enter Age: "))
weight = int(input("Enter Weight(in kgs): "))
height = int(input("Enter Height(in cms): "))
activityLevel = int(input("Enter Activity Level(1/2/3/4/5)"))
basalMetabolicRate = 0

#Calculating BMR and required calories.
if (gender == "M"):
    basalMetabolicRate = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    basalMetabolicRate = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

requiredCalories = requiredCaloriesFn(activityLevel, basalMetabolicRate)

#Calculating the amount of macro Nutrients
requiredProtein = ((requiredCalories * 0.1),(requiredCalories * 0.35))
requiredCarbs = ((requiredCalories * 0.45),(requiredCalories * 0.65))
requiredFats = ((requiredCalories * 0.2),(requiredCalories * 0.35))

if (age>= 18):
    if (gender == "M"):
        requiredVitaminA = 0.0009  # 900 µg/day (0.9 mg/day)
        requiredVitaminB1 = 0.0012  # 1.2 mg/day
        requiredVitaminB2 = 0.0013  # 1.3 mg/day
        requiredVitaminB3 = 0.016  # 16 mg/day
        requiredVitaminB6 = 0.0013  # 1.3 mg/day
        requiredVitaminB12 = 0.0000024  # 2.4 µg/day (0.0024 mg/day)
        requiredVitaminC = 0.09  # 90 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.015  # 15 mg/day
        requiredVitaminK = 0.00012  # 120 µg/day (0.12 mg/day)
        
        requiredCalcium = 1.0  # 1000 mg/day (1 g/day)
        requiredIron = 0.008  # 8 mg/day

    if (gender == "F"):
        requiredVitaminA = 0.0007  # 700 µg/day (0.7 mg/day)
        requiredVitaminB1 = 0.0011  # 1.1 mg/day
        requiredVitaminB2 = 0.0011  # 1.1 mg/day
        requiredVitaminB3 = 0.014  # 14 mg/day
        requiredVitaminB6 = 0.0013  # 1.3 mg/day
        requiredVitaminB12 = 0.0000024  # 2.4 µg/day (0.0024 mg/day)
        requiredVitaminC = 0.075  # 75 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.015  # 15 mg/day
        requiredVitaminK = 0.00009  # 90 µg/day (0.09 mg/day)

        requiredCalcium = 1.0  # 1000 mg/day (1 g/day)
        requiredIron = 0.018  # 18 mg/day

if (age < 1):
    requiredVitaminA = 0.0005  # 500 µg/day (0.5 mg/day)
    requiredVitaminB1 = 0.0002  # 0.2 mg/day
    requiredVitaminB2 = 0.0003  # 0.3 mg/day
    requiredVitaminB3 = 0.002  # 2 mg/day
    requiredVitaminB6 = 0.0003  # 0.3 mg/day
    requiredVitaminB12 = 0.0000004  # 0.4 µg/day (0.0004 mg/day)
    requiredVitaminC = 0.05  # 50 mg/day
    requiredVitaminD = 0.01  # 10 µg/day (0.01 mg/day)
    requiredVitaminE = 0.005  # 5 mg/day
    requiredVitaminK = 0.0000025  # 2.5 µg/day (0.0025 mg/day)

    requiredCalcium = 0.26  # 260 mg/day
    requiredIron = 0.011  # 11 mg/day

if (age >= 1 and age <= 3):
    requiredVitaminA = 0.0003  # 300 µg/day (0.3 mg/day)
    requiredVitaminB1 = 0.0005  # 0.5 mg/day
    requiredVitaminB2 = 0.0005  # 0.5 mg/day
    requiredVitaminB3 = 0.006  # 6 mg/day
    requiredVitaminB6 = 0.0005  # 0.5 mg/day
    requiredVitaminB12 = 0.0000009  # 0.9 µg/day (0.0009 mg/day)
    requiredVitaminC = 0.015  # 15 mg/day
    requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
    requiredVitaminE = 0.006  # 6 mg/day
    requiredVitaminK = 0.00003  # 30 µg/day (0.03 mg/day)

    requiredCalcium = 0.7  # 700 mg/day
    requiredIron = 0.007  # 7 mg/day

if (age >= 4 and age <= 8):
    requiredVitaminA = 0.0004  # 400 µg/day (0.4 mg/day)
    requiredVitaminB1 = 0.0006  # 0.6 mg/day
    requiredVitaminB2 = 0.0006  # 0.6 mg/day
    requiredVitaminB3 = 0.008  # 8 mg/day
    requiredVitaminB6 = 0.0006  # 0.6 mg/day
    requiredVitaminB12 = 0.0000012  # 1.2 µg/day (0.0012 mg/day)
    requiredVitaminC = 0.025  # 25 mg/day
    requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
    requiredVitaminE = 0.007  # 7 mg/day
    requiredVitaminK = 0.000055  # 55 µg/day (0.055 mg/day)

    requiredCalcium = 1.0  # 1000 mg/day (1 g/day)
    requiredIron = 0.01  # 10 mg/day

if (age >= 9 and age <= 13):
    if (gender == "M"):
        requiredVitaminA = 0.0006  # 600 µg/day (0.6 mg/day)
        requiredVitaminB1 = 0.0009  # 0.9 mg/day
        requiredVitaminB2 = 0.0009  # 0.9 mg/day
        requiredVitaminB3 = 0.012  # 12 mg/day
        requiredVitaminB6 = 0.001  # 1 mg/day
        requiredVitaminB12 = 0.0000018  # 1.8 µg/day (0.0018 mg/day)
        requiredVitaminC = 0.045  # 45 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.011  # 11 mg/day
        requiredVitaminK = 0.00006  # 60 µg/day (0.06 mg/day)

        requiredCalcium = 1.3  # 1300 mg/day (1.3 g/day)
        requiredIron = 0.008  # 8 mg/day

    if (gender == "F"):
        requiredVitaminA = 0.0006  # 600 µg/day (0.6 mg/day)
        requiredVitaminB1 = 0.0009  # 0.9 mg/day
        requiredVitaminB2 = 0.0009  # 0.9 mg/day
        requiredVitaminB3 = 0.012  # 12 mg/day
        requiredVitaminB6 = 0.001  # 1 mg/day
        requiredVitaminB12 = 0.0000018  # 1.8 µg/day (0.0018 mg/day)
        requiredVitaminC = 0.045  # 45 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.011  # 11 mg/day
        requiredVitaminK = 0.00006  # 60 µg/day (0.06 mg/day)

        requiredCalcium = 1.3  # 1300 mg/day (1.3 g/day)
        requiredIron = 0.008  # 8 mg/day

if (age >= 14 and age <= 18):
    if (gender == "M"):
        requiredVitaminA = 0.0009  # 900 µg/day (0.9 mg/day)
        requiredVitaminB1 = 0.0012  # 1.2 mg/day
        requiredVitaminB2 = 0.0013  # 1.3 mg/day
        requiredVitaminB3 = 0.016  # 16 mg/day
        requiredVitaminB6 = 0.0013  # 1.3 mg/day
        requiredVitaminB12 = 0.0000024  # 2.4 µg/day (0.0024 mg/day)
        requiredVitaminC = 0.075  # 75 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.015  # 15 mg/day
        requiredVitaminK = 0.000075  # 75 µg/day (0.075 mg/day)

        requiredCalcium = 1.3  # 1300 mg/day (1.3 g/day)
        requiredIron = 0.011  # 11 mg/day

    if (gender == "F"):
        requiredVitaminA = 0.0007  # 700 µg/day (0.7 mg/day)
        requiredVitaminB1 = 0.001  # 1 mg/day
        requiredVitaminB2 = 0.001  # 1 mg/day
        requiredVitaminB3 = 0.014  # 14 mg/day
        requiredVitaminB6 = 0.0012  # 1.2 mg/day
        requiredVitaminB12 = 0.0000024  # 2.4 µg/day (0.0024 mg/day)
        requiredVitaminC = 0.065  # 65 mg/day
        requiredVitaminD = 0.015  # 15 µg/day (0.015 mg/day)
        requiredVitaminE = 0.015  # 15 mg/day
        requiredVitaminK = 0.000075  # 75 µg/day (0.075 mg/day)

        requiredCalcium = 1.3  # 1300 mg/day (1.3 g/day)
        requiredIron = 0.015  # 15 mg/day

consumedCarbs = 0
consumedProteins = 0
consumedFats = 0
consumedVitaminA = 0
consumedVitaminB1 = 0
consumedVitaminB2 = 0
consumedVitaminB3 = 0
consumedVitaminB6 = 0
consumedVitaminB12 = 0
consumedVitaminC = 0
consumedVitaminD = 0
consumedVitaminE = 0
consumedVitaminK = 0
consumedCalcium = 0
consumedIron = 0

while(True):
    foodItemName = input("Enter food Item")
    if (foodItemName == "null"):
        break
    else:
        foodItemObj = globals().get(foodItemName, "Item not found")
        if (foodItemObj == "Item not found"):
            print("Item not found")
        else:
            itemQty = float(input("Enter Qty (in gms)"))

            consumedCarbs = consumedCarbs + ((foodItemObj.carbsPer100gm) * itemQty / 100)
            consumedProteins = consumedProteins + ((foodItemObj.proteinPer100gm) * itemQty / 100)
            consumedFats = consumedFats + ((foodItemObj.fatsPer100gm) * itemQty / 100)
            consumedVitaminA = consumedVitaminA + ((foodItemObj.vitaminAPer100gm) * itemQty / 100)
            consumedVitaminB1 = consumedVitaminB1 + ((foodItemObj.vitaminB1Per100gm) * itemQty / 100)
            consumedVitaminB2 = consumedVitaminB2 + ((foodItemObj.vitaminB2Per100gm) * itemQty / 100)
            consumedVitaminB3 = consumedVitaminB3 + ((foodItemObj.vitaminB3Per100gm) * itemQty / 100)
            consumedVitaminB6 = consumedVitaminB6 + ((foodItemObj.vitaminB6Per100gm) * itemQty / 100)
            consumedVitaminB12 = consumedVitaminB12 + ((foodItemObj.vitaminB12Per100gm) * itemQty / 100)
            consumedVitaminC = consumedVitaminC + ((foodItemObj.vitaminCPer100gm) * itemQty / 100)
            consumedVitaminD = consumedVitaminD + ((foodItemObj.vitaminDPer100gm) * itemQty / 100)
            consumedVitaminE = consumedVitaminE + ((foodItemObj.vitaminEPer100gm) * itemQty / 100)
            consumedVitaminK = consumedVitaminK + ((foodItemObj.vitaminKPer100gm) * itemQty / 100)
            consumedCalcium = consumedCalcium + ((foodItemObj.calciumPer100gm) * itemQty / 100)
            consumedIron = consumedIron + ((foodItemObj.ironPer100gm) * itemQty / 100)

print(consumedCarbs)
print(consumedProteins)
print(consumedFats)
print(consumedVitaminA)
print(consumedVitaminB1)
print(consumedVitaminB2)
print(consumedVitaminB3)
print(consumedVitaminB6)
print(consumedVitaminB12)
print(consumedVitaminC)
print(consumedVitaminD)
print(consumedVitaminE)
print(consumedVitaminK)
print(consumedCalcium)
print(consumedIron)