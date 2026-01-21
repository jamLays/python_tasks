#21.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours per week: '))
rate = int(input('Enter rate per hour: '))
weekly_earning = hours*rate
print(weekly_earning)

#22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter years: '))
live_in_secs = years*31536000
print(live_in_secs)
