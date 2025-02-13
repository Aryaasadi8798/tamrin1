hour = int(input("لطفا ساعت فعلی را وارد کنید: "))

if 0 <= hour < 6:
    print("nime sab bekhir")
elif 6 <= hour < 12:
    print("sobh be khir")
elif 12 <= hour < 18:
    print("zohr be khir")
elif 18 <= hour <= 24:
    print("sab bekhir")
else:
    print(asteba)
