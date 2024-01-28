# Secret Code Game in Pythom
print("\n\n***** Welcome to Secret Code Game *****\n")
coding = input("\nEnter 1 for Coding or 0 for Decoding : ")
st = input("\nEnter the message : ")
words = st.split(" ")
coding = True if (coding == "1") else False
if coding:
    print("\nThe coded message is : ")
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "aix"
            r2 = "zof"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            try:
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            except IndexError as I:
                print("\nEnter a valid decoded message")
                exit()
        else:
            nwords.append(word[::-1])
    print("\nThe Decoded Message is : ")
    print(" ".join(nwords))

print("\nThanks for Playing Secret Code Game!\n")
