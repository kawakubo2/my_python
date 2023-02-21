name_list = ['山田太郎', '横山花子', '田中一郎', '鈴木次郎']
sales_list = [[30, 10, 15, 40], [20, 20, 30], [50, 10, 10], [30, 15]]

sales_dic = { name: sum(sales) for name, sales in zip(name_list, sales_list)}
print(sales_dic)