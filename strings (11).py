str1 = input('Enter the string 1 :')
str2 = input('Enter the string 2 :')

res = [i for i in range(len(str1)) if str1.startswith(str2, i)]
print("The start indices of the substrings are : " , str(res))