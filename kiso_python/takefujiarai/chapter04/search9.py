# -*- coding: utf-8 -*-

email = 'tomo.kawakubo@gmail.com'

index = email.find('@')

if index != -1:
    local = email[:index] # @の位置を見つけ出し、その前の部分文字列を取り出す
    domain = email[index + 1:]
    print("{}のローカル部は{}で、ドメイン部は{}です".format(email, local, domain))

str2 = "    local = email[:index] # @の位置を見つけ出し、その前の部分文字列を取り出す"
index2 = str2.find('#')
comment = str2[index2+1:]
print(comment)
                   
                   