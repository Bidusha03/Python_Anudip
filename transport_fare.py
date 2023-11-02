"""A transport company charges the fare according to following table:
Distance Charges
1-50 8 Rs./Km
51-100 10 Rs./Km
> 100 12 Rs/Km"""

distance = float(input("Enter distance of how many kilometers travelled: "))
if distance <= 50:
    fare1 = distance * 8
    print("Total fare is", fare1, 'Rs.')
elif distance <= 100:
    fare2 = distance * 10
    print("Total fare is", fare2, 'Rs.')
elif distance > 100:
    fare3 = distance * 12
    print("Total fare is", fare3, 'Rs.')

"""Output:
Enter distance of how many kilometers travelled: 15
Total fare is 120.0 Rs.
"""
