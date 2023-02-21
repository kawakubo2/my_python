langs = "Python:Java:Go:Ruby:Rust:C++"

lang_list = langs.split(":")
print(type(lang_list))
print(lang_list)

s = ",".join(lang_list)
print(s)