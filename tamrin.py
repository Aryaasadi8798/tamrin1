import random

secret_number = random.randint(1, 100)
guesses = [] 

print("به بازی حدس عدد خوش آمدید! عددی بین 1 تا 100 حدس بزنید.")

while True:
    try:
        guess = int(input("حدس شما: "))
        
        if guess < 1 or guess > 100:
            print("لطفاً عددی بین 1 تا 100 وارد کنید!")
            continue
        
        guesses.append(guess)  

        if guess < secret_number:
            print("عدد شما کوچکتر از مقدار صحیح است. دوباره تلاش کنید!")
        elif guess > secret_number:
            print("عدد شما بزرگتر از مقدار صحیح است. دوباره تلاش کنید!")
        else:
            print(f"تبریک! عدد {secret_number} را درست حدس زدید 🎉")
    
            break  # خروج از حلقه پس از حدس درست

    except ValueError:
        print("لطفاً فقط عدد وارد کنید!")
