import os

# An application that shows any number in abacus form

### FUNCTIONS ###


def header(base):
    os.system('clear')

    print("\t***************************************")
    print("\t**********  Abacus - base %d **********" % base)
    print("\t***************************************")


def change_base_line():
    print("\n\tIf you would like to change base type b.\n")


def construct_abacus(number, base):
    # Convert number into four-digit number with leading zeros if necessary
    number = "{:04d}".format(int(number))
    # Constructs the picture of the abacus.
    for i in range(len(number)):
        abacus_bar_i = '|'
        abacus_bar_i += 'x' * int(number[i])
        abacus_bar_i += '-----'
        abacus_bar_i += 'x' * (base - int(number[i]))
        abacus_bar_i += '|'
        print(abacus_bar_i)


def abacus(base):
    number = ''
    while number != 'q':
        header(base)
        change_base_line()
        print('An empty abacus...')
        construct_abacus('0', base)
        number = input('Please enter a base %d number up to four-digits (or type q to quit): ' % base)
        if number == 'b':
            base = int(input('What base would you like the abacus to be?'))
        elif number == 'q':
            header(base)
            print('Goodbye')
        else:
            header(base)
            change_base_line()
            print('On an abacus, the number %s looks like this:' % number)
            construct_abacus(number, base)
            input('Press enter to try another...')


### MAIN PROGRAM ###
# Start at base 10
base = 10
abacus(base)
