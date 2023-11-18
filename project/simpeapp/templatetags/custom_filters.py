from django import template


register = template.Library()



@register.filter()
def censor(text):
    variants = ['усь', 'кот', 'пони', 'сочи', 'балка', 'просто']

    ln = len(variants)
    filtred_text = ''
    string = ''
    for i in text:
        string += i
        string2 = string.lower()

        flag = 0
        for j in variants:
            if not string2 in j:
                flag += 1
            if string2 == j:
                filtred_text += j[0] + "*" * (len(string)-1)
                flag -= 1
                string = ''

        if flag == ln:
            filtred_text += string
            string = ''

    if string2 != '' and string2 not in variants:
        filtred_text += string
    elif string2 != '':
        filtred_text += "*" * (len(string)-1)

    return filtred_text
