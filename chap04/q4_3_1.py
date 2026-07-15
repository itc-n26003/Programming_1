def concat_words(*args, separator='.'):
    '''任意の数の位置引数と区切り文字を受け取り、区切り文字でつなげる'''
    return separator.join(args)

print(concat_words('a', 'b', 'c', 'd', separator='_'))
print(concat_words('4_choume', 'Minatoku', 'Tokyo', 'Japan', separator=' '))
