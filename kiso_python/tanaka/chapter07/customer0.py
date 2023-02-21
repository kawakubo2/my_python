class Customer:
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
if __name__ == '__main__':
    c1 = Customer(120, '山田太郎', 168);
    print(f"会員番号: {c1.number} 名前: {c1.name} 身長: {c1.height}cm")
    c2 = Customer(121, '横山花子', 158);
    print(f"会員番号: {c2.number} 名前: {c2.name} 身長: {c2.height}cm")
    print(f"会員番号: {c1.number} 名前: {c1.name} 身長: {c1.height}cm")

    c1.height = 170
    print(f"会員番号: {c1.number} 名前: {c1.name} 身長: {c1.height}cm")