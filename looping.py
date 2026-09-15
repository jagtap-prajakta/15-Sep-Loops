# 15 Sep 2026
# ---------------------------------------------- LOOPS  ----------------------------------------------
# # 1.
# while True:
#     string = input("Enter a String: ")
#     print(string)


# # 2. 
# correct_pass = "some_pass"
# not_found = True

# while not_found:
#     passw = input("Enter pass: ")
#     if passw == correct_pass:   #breaking condition
#         not_found = False
# print("Password Matched!")


# 3. above code in other way:



# # 4. 
# i = 0
# while i < 10:
#     print(i)
#     i += 1


# # 5. print table of 5:
# i = 1
# while i <= 10:
#     print(f"5 × {i} = {5*i}")
#     i += 1


# # 6. break statement 
# correct_pass = "some_pass"
# not_found = True

# while not_found:
#     passw = input("Enter pass: ")
#     if passw == correct_pass:   #breaking condition
#         break
# print("Password Matched!")


# # 7. continue statement : 
# i = 0
# while i < 10:
#     if i == 5:
#         continue
#     print(i)
#     i += 1    #output: 0 1 2 3 4 skip
# # there's a bug in above program that will cause an infinite loop because when i == 5, the continue statement will skip the increment of i, so i will always be 5 and the loop will never terminate.
# # difference between bug and error: bug is a logical error in the program which doesn't give the expected output but error is a syntax error which doesn't allow the program to run.

# # to solve bug, we can increment i before the continue statement:
# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1    #output: 0 1 2 3 4 6 7 8 9



