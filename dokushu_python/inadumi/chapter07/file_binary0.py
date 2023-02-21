with open('./dokushu_python/inadumi/chapter07/cat2.jpg', 'rb') as reader, \
    open('./dokushu_python/inadumi/chapter07/output.jpg', 'wb') as writer: 
    while d := reader.read(1): 
        writer.write(d)