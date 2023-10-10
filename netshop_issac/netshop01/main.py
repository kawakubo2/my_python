import os
from product import Product, ProductsProducerFromFile, ProductsProducerFromHardcode, ProductsViewer
from customer import ConsoleCustomerInputHelper
from order import ConsoleOrderInputHelper
from invoice import Invoice, InvoiceCalculator, ConsoleInvoicePrinter

if __name__ == "__main__":
    # 製品リストの表示
    product_dict = ProductsProducerFromFile().get_products()
    ProductsViewer().view(product_dict)

    # 注文入力
    print("---注文(入力)開始---")
    customer = ConsoleCustomerInputHelper().create()
    order = ConsoleOrderInputHelper().create(customer)
    invoice = Invoice(order)
    invoice_printer = ConsoleInvoicePrinter(invoice, product_dict)

    # 請求書出力
    print("---請求書---")
    invoice_printer.print()