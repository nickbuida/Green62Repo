n = int(input())
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        a = "##.." * (x // 2)
        b = "..##" * (x // 2)
    else:
        a = "##.." * (x // 2) + "##"
        b = "..##" * (x // 2) + ".."

    for i in range(x):
        if i % 2 == 0:
            print(a)
            print(a)
        else:
            print(b)
            print(b)

# n = int(input())
# for _ in range(n):
#     x = int(input())
#     for i in range(x):
#         if x % 2 == 0:
#             if i % 2 == 0:
#                 print("##.." * (x // 2))
#                 print("##.." * (x // 2))
#             else:
#                 print("..##" * (x // 2))
#                 print("..##" * (x // 2))
#         else:
#             if i % 2 == 0:
#                 print("##.." * (x // 2) + "##")
#                 print("##.." * (x // 2) + "##")
#             else:
#                 print("..##" * (x // 2) + "..")
#                 print("..##" * (x // 2) + "..")

