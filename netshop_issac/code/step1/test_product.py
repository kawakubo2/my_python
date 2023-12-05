from netshop import Product

def test_constructor():
    product = Product("A100", "洗濯機", "5kg高速洗浄", 50000)
    assert product.code == "A100"
    assert product.name == "洗濯機"
    assert product.desc == "5kg高速洗浄"
    assert product.unit_price == 50000