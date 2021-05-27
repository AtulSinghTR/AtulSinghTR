def is_isogram(string):
    # con=[]
    # msg=True
    # for d in list(string.lower().replace('-', '').replace(' ', '')):
    #     if d in con:
    #         msg=False
    #         break
    #     else:
    #         con.append(d)
    st=string.lower().replace('-', '').replace(' ', '')
    msg = True if len(set(st)) == len(st) else False
    return msg