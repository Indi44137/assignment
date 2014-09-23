#Indi Knighton
#22/09/2014
#Currecy extension

print("This proram will tell ou how much £20, £10, £5, £2, £1's go into the amount you select and display the least out of them")
amount = int(input("Please enter the amount here: "))
div_result1 = amount//20
mod_result = amount%20
div_result2 = mod_result//10
mod_result = mod_result%10
div_result3 = mod_result//5
mod_result = mod_result%5
div_result4 = mod_result//2
mod_result = mod_result%2
div_result5 = mod_result//1

print("The amount of £20's that go into the amount is {0}. The amount of £10 is {1}. The amount of £5 is {2}. The amount of £2 is {3} and the amount  of £1's is {4}!".format(div_result1, div_result2, div_result3, div_result4, div_result5))
