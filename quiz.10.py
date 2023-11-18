class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price


coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)


selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")


if selected_beverage == "커피":
    selected_object = coffee
elif selected_beverage == "녹차":
    selected_object = green_tea
elif selected_beverage == "아이스티":
    selected_object = ice_tea
else:
    print("잘못된 음료를 선택하셨습니다.")
    exit()


quantity = int(input("수량을 입력하세요: "))


total_price = selected_object.calculate(quantity)
print(f"{selected_beverage} {quantity}잔의 가격은 {total_price}원 입니다.")
