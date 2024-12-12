name = str(input('whats your name ?: '))
if(name!='VIP'):
    tickets_nbr=int(input('how many tickets would you buy: '))
    total=15.50*tickets_nbr
    print('the total is : '+str(total)+ ',enjoy the film!')

else:
    print('enjoy the show for free')