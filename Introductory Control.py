'''
Problem Statement- I

Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.
'''

team_runs_scored = int(input("Enter the total runs scored by the team: "))
team_overs_faced = float(input("Enter the total overs faced by the team: "))
team_runs_conceded = int(input("Enter the total runs conceded by the team: "))
team_overs_bowled = float(input("Enter the total overs bowled by the team: "))

# Calculate the net run rate
team_net_run_rate = ((team_runs_scored / team_overs_faced) - (team_runs_conceded / team_overs_bowled))

print("The team's net run rate is:", team_net_run_rate)

other_team_net_run_rate = 5.0 
if team_net_run_rate > other_team_net_run_rate:
    print("The team is ahead in net run rate and tops the points table.")
elif team_net_run_rate < other_team_net_run_rate:
    print("The team is behind in net run rate and does not top the points table.")
else:
    print("The teams have the same net run rate. The tie-breaker will depend on other factors.")

'''
Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2
'''

Nint = 28
Div = 1
sum1 = 0

while Div < Nint:
    if Nint % Div == 0:
        sum1 += Div
    Div += 1
    
if sum1 > Nint:
    print(Nint,"is an abundant number")
elif sum1 < Nint:
    print(Nint,"is a deficient number")
else:
    print(Nint,"is a perfect number")