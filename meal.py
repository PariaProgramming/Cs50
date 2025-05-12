def main ():
    time = input("What time is it? ")

    hours = convert(time)

    if 07.00 <= hours < 08.00:
        print("breakfast time")
    elif 12.00 <= hours < 13.00:
        print("lunch time")
    elif 18.00 <= hours < 19.00:
        print("dinner time")
    else:
        print()        

def convert(time):
    hours, minutes = time.split(":")
    
    hours = float(hours)
    minutes = float(minutes)

    decimal_hours = hours + minutes/60
    return decimal_hours 

if __name__ == '__main__':
    main()