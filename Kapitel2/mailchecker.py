email = 'kermit.der.frosch@thu.de'
# print(len(email))
# print(email.index('@'))
# print(email.index('.'))
# print(email.rindex('.'))
# print('f' in email)
# print('F' in email)


def localpart(email):
    if '@' in email:
        index_at = email.index('@')
        localpart = email[0:index_at]
        return localpart
    else:
        return ''

def tld(email):
    index_letzer_punkt = email.rindex('.')
    tld = email[index_letzer_punkt+1:]
    return tld

def lld(email):
    if '@' in email:
        index_at = email.index('@')
        index_letzter_punkt = email.rindex('.')
        lld = email[index_at+1:index_letzter_punkt]
        return lld
    else:
        return ''



def email_gueltig(email):
    vorkommen_at = 0
    for c in email:
        if c == '@':
            vorkommen_at+=1
    vorkommen_punkt = 0
    if '@' in email:
        for c in email[email.index('@'):]:
            if c == '.':
                vorkommen_punkt += 1
    try:
        bedingung_1 = (vorkommen_at == 1) and (vorkommen_punkt >= 1)
        bedingung_2 = len(localpart(email)) != 0
        bedingung_3 = len(lld(email)) != 0
        bedingung_4 = len(tld(email)) != 0
        bedingung_5 = (localpart(email)[0] != '.') and (localpart(email)[-1] != '.')
    except Exception:
        return False
    
    if bedingung_1 and bedingung_2 and bedingung_3 and bedingung_4 and bedingung_5:
        return True
    else:
        return False
 

ada_mail = 'ada@lovelace.co.uk'

   
print(email_gueltig(ada_mail))
    
    