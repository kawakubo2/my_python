# -*- coding: utf-8 -*-

def mail_template(name, year, month, sama = "様"):
    template = """
{}{}

本日は「コロナに負けるな」の{}年{}月号が発売となりました。

今月号の特集は
"""
    print(template.format(name, sama, year, month))
    
    
name = "山田太郎"
year = 2020
month = 7

mail_template(name, year, month, "さん")

print("Python", "Java", "PHP", sep="-")