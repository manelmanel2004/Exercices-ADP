print('Welcome to the texi application, please answer the following quesstions')

ppl_ride=int(input('how many people need a ride ?'))
ppl_nbr=int(input('how amny people can fit in the taxi?'))

if(ppl_ride % ppl_nbr == 0):
    taxi=ppl_nbr
else:
    taxi=ppl_ride//ppl_nbr

print('the number of taxis neede is : '+str(taxi))
    