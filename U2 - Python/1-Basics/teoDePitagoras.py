import math

cat1 = int(input("Ingresar cateto 1:"))
cat2 = int(input("Ingresar cateto 2:"))

# hipotenusa = math.sqrt(cat1**2 + cat2**2) 
hipotenusa = math.sqrt(pow(cat1, 2) + pow(cat2, 2))

print("La hipotenusa es:", hipotenusa)