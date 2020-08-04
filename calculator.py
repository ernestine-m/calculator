from math import ceil, floor, log, pow

def calculator():
    print('What do you want to calculate?\ntype "n" - for count of months,\ntype "a" - for annuity monthly payment,\ntype "p" - for credit principal: ')
    choice = input()
    if choice == 'n':
        repay_time()
    elif choice =='a':
        annuity_pay()
    else:
        principal()


def repay_time():
    '''Calculate repay period'''
    print('Enter credit principal:')
    cp = int(input())
    print('Enter monthly payment:')
    mp = int(input())
    print('Enter credit interest:')
    i = (float(input())/100)/12 #nominal interest rate
    periods = log(mp/(mp-i*cp),1+i)
    months = ceil(periods)
    if months <=12:
        if months ==1:
            print('It takes 1 month to repay the credit')
        else:
            print(f'It takes {months} months to repay the credit')
    else:
        years = floor(months / 12)
        months = months - 12 * years
        if months == 0:
            print(f'It takes {years} years to repay the credit')
        else:
            print(f'It takes {years} years and {months} months to repau the credit')


def annuity_pay():
    '''Calculate annuity payment'''
    print('Enter credit principal:')
    cp = int(input())
    print('Enter count of periods:')
    periods = int(input())
    print('Enter credit interest:')
    i = (float(input()) / 100) / 12  # nominal interest rate
    A = cp * ((i * pow(1+i,periods)) / (pow(1+i,periods) - 1))
    print(f'Your annuity payment = {ceil(A)}!')

def principal():
    '''Calculate credit principal'''
    print('Enter monthly payment:')
    mp = float(input())
    print('Enter count of periods:')
    periods = int(input())
    print('Enter credit interest:')
    i = (float(input()) / 100) / 12  # nominal interest rate
    cp = mp / ((i * pow(1+i,periods))/ (pow(1+i,periods)-1))
    print(f'Your credit principal = {round(cp)}!')

calculator()
