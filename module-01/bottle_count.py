#chanceller Waters
#12-6-25
#module 1: Beer count
#the purpose of this program is to receive and count down in song, a user provided bottle count


def bottle_countdown(num_bottles):
    """controls countdown of bottles of beer in song"""
    while num_bottles > 1:
        print(f"{num_bottles} bottles of beer on the wall., {num_bottles} bottles of beer.")
        print(f"Take one down, pass it around, {num_bottles - 1}.bottles of beer on the wall.")
        print()
        num_bottles -= 1

    if num_bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("take one down, pass it around, no more bottles of beer on the wall.")
        print()

def main():
    """"
        program to prompt for and receive user input to initiate bottle countdown
    """
    while True:
        try:
            bottles_initial = int(input("How many bottles of beer are on the wall? "))
            if bottles_initial <= 0:
                print("Enter a positive number of bottles please.")
            else:
                break
        except ValueError:
         print("Invalid input, enter a whole number please")


    bottle_countdown(bottles_initial)
    print("Time to buy more beer!")

if __name__ == "__main__":
    main()
