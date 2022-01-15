# x.endswith sprawdza czy string konczy sie na
# x.islower sprawdza czy string jest z malych liter
# x.upper przekstałca string na duże litery
# find szuka stringa w stringu
# replace zamienia znak na inny
# split dzieli tekst za pomoca separatora i umieszcza w liscie




atext= 'tojest jest tekst'
print(atext)

t=atext.endswith('kst')
print(t)

r=atext.islower()
print(r)

print(atext.upper())

r=atext.upper()
print(r)

print(atext.find('jest',3))
print(atext.replace('jest','było'))
print(atext.replace('jest','było').replace('k',''))
print(atext.split(" "))

mynumber='1000'
print(mynumber+'1')


print(mynumber.isdigit())
print(mynumber.isalpha())
print(mynumber.isalnum())

print('++++++++++++++++TERAZ ZADANIA++++++++++++++++++++')
quote='A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one','1'))
print(quote.replace('one','1').replace('both','2'))
print(quote.split(' '))


