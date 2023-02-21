customers = [
    {"会社名": "福岡物産", "法人格": "株式会社", "前後": "後"},
    {"会社名": "博多運送", "法人格": "有限会社", "前後": "後"},
    {"会社名": "小倉製鉄", "法人格": "株式会社", "前後": "前"},
]

def get_formal_name(customer):
    if customer["前後"] == "前":
        return customer["法人格"] + customer["会社名"]
    else:
        return customer["会社名"] + customer["法人格"]
    
for customer in customers:
    print(get_formal_name(customer))
        
    