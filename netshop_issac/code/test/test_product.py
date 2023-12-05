from netshop import Product

def test_constructor():
    product = Product("A100", "洗濯機", "5kg高速洗浄", 50000)
    assert product.code == "A100"
    assert product.name == "洗濯機"
    assert product.desc == "5kg高速洗浄"
    assert product.unit_price == 50000

def test_equality():
    p1 = Product("XPS8950", "DELL製デスクトップパソコン", "メモ32G  CPU Intel Core i7", 298000);
    p2 = Product("XPS8950", "DELL製デスクトップパソコン", "メモ32G  CPU Intel Core i7", 298000);
    assert p1 == p2

def test_inequality():
    p1 = Product("XPS8950", "DELL製デスクトップパソコン", "メモ32G  CPU Intel Core i7", 298000);
    p2 = Product("XPS8950", "DELL製デスクトップパソコン", "メモ32G  CPU Intel Core i7", 398000);
    assert p1 != p2
    