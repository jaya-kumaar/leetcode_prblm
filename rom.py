def decimal_to_roman(decimal):
    roman_numerals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
    (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    roman=' '
    for value,numeral in roman_numerals:
        while decimal >=value:
            roman+=numeral
            decimal-=value
    return(roman)
decimal=int(input("enter the decimal number:"))
s=decimal_to_roman(decimal)


print("the roman value of the",decimal," is ",s)

