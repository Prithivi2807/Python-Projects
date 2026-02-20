def freq(strings):
    words_in_list =[]
    words_in_list = strings.split()
    dict_in_list = {}
    for key in words_in_list: 
        dict_in_list[key] = words_in_list.count(key)

    print(dict_in_list)


freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go")