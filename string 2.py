#srring are immutable
a='Abhishek from IIT  madras'
print(len(a))
print(a.upper())
print(a.lower())
#another exampale
b='abhishek ???????'
c='??????abhishek ?????'
d="ram is goning to school so that he is not going to school.his parents is worry about why he is not going to school."
print(b.rstrip("?"))#output=abhishek
print(c.rstrip('?'))#output=??????abhishek
print(b.replace('abhishek','atul'))
print(a.replace('Abhishek','nit'))
#print(b.split(""))#doubt because not run
print(d.capitalize())#first litter become capital and other letter is smaller
print(c.center(50))
print(len(c.center(50)))
print(d.count('going'))
print(c.center(50)[25])
print(c.center(50)[20:30])
str1="wel come to console !!!"
# print(e.endwith("!!!"))#gives true and false value
# print(str1.endwith("to",4,10))
print(str1.find("come"))#find then output is first index of carrector is 4
print(str1.find("is"))#output is because is not present-1
#print(str1.index("is"))
print(str1.isalnum())#identyfy alpha numaric like- !@#$ present or not 
str2="welcome"
print(str2.isalpha())#true
str3="wel123"
print(str3.isalpha())#false because number also present
print(str3.islower())#identyfy lower present or not if lower present then valu=true if not then return false
str4="raam is going to moves for shoping"
print(str4.isprintable())#return true 
str5="ram is \n going to home"
print(str5.isprintable())# return flse due to \n is not printable 
srt6="RAM   kumar"#in between ram and kumar space 
print(srt6.isspace)
print(srt6.istitle())
print(srt6.swapcase())#convert upper case to lower case and lower to upper
print(str4.title())#first letter of all wort convert into capital letter
