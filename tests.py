def summe(number1, number2):
    counter = 1
    #if number1 + number2 >= 10:
    while counter < 10:
        counter = counter + 1
        print(counter)
        #print('Summe ist gleich oder grösser als 10')
    else:
        print('counter ist bei 10 angelangt')
        #print('Summe ist kleiner als 10')


if __name__ == '__main__':
    summe(4,6)