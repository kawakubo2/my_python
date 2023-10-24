import datetime
from abc import abstractmethod, ABC
class Invoice():
    def __init__(self, order):
        self.__order = order
        
    def get_order(self):
        return self.__order

    order = property(get_order)

class InvoiceCalculator():
    SHIPPING_UNIT_COST = 1.0
    def __init__(self, invoice, product_dict):
        self.order_detail = invoice.order.order_detail
        self.product_dict = product_dict
        self.calc_dict = {}
        
    def calc(self):
        order_detail_dict = {}
        subtotal = 0.0
        VAT_RATE = 0.2
        vat = 0.0
        for code, quantity in self.order_detail.items():
            order_detail_dict[code] = self.order_detail[code] *  self.product_dict[code].unit_price
            subtotal += order_detail_dict[code]
        self.calc_dict["order_detail_price"] = order_detail_dict
        self.calc_dict["subtotal"] = subtotal
        self.calc_dict["shipping_cost"] = len(order_detail_dict) * InvoiceCalculator.SHIPPING_UNIT_COST
        self.calc_dict["vat"] = (self.calc_dict["subtotal"] + self.calc_dict["shipping_cost"]) * VAT_RATE
        self.calc_dict["total"] = \
                        self.calc_dict["subtotal"] + \
                        self.calc_dict["shipping_cost"] + \
                        self.calc_dict["vat"]
        return self.calc_dict

class InvoicePrinter(ABC):
    # Template method pattern適用
    @abstractmethod
    def __init__(self, invoice, product_dict):
        pass
    @abstractmethod
    def print_header(self):
        pass
    @abstractmethod
    def print_body(self):
        pass
    @abstractmethod
    def print_footer(self):
        pass
    # template method pattern
    def print(self):
        self.print_header()
        self.print_body()
        self.print_footer()
    
class ConsoleInvoicePrinter(InvoicePrinter):
    def __init__(self, invoice, product_dict):
        self.invoice = invoice
        self.product_dict = product_dict
        self.invoice_calculator = InvoiceCalculator(invoice, product_dict)
        
    def print_header(self):
        customer = self.invoice.order.customer
        print(f"氏名　　: {customer.name}")
        print(f"住所１　: {customer.address1}")
        print(f"住所２　: {customer.address2}")
        print(f"郵便番号: {customer.zipcode}")

    def print_body(self):
        calc_dict = self.invoice_calculator.calc()
        print("[注文内容]")
        print("コード  製品名              製品内容                  注文数    単価    金額")
        for code, quantity in self.invoice.order.order_detail.items():
            product = self.product_dict[code]
            print(f"{code:<8}{product.name:<20}{product.desc:<24}{quantity:>8}{product.unit_price:>8.2f}{calc_dict['order_detail_price'][code]:>8.2f}")
        print(f"{'小計':>50}{calc_dict['subtotal']:>24.2f}")
        print(f"{'送料':>50}{calc_dict['shipping_cost']:>24.2f}")
        print(f"{'VAT 20%':>55}{len(self.invoice.order.order_detail):5}{self.invoice_calculator.SHIPPING_UNIT_COST:>8.2f}{calc_dict['vat']:>8.2f}")
        print(f"{'合計':>50}{calc_dict['total']:>24.2f}")

        
    def print_footer(self):
        pass
        
    