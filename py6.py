def compute_pay(working_hours , hourly_rate):

    regular_hour=40
    overtime_hours=regular_hour-working_hours
    overtime_rate=1.5


    total_pay=(regular_hour * hourly_rate ) + (overtime_hours * hourly_rate * overtime_rate)
    return total_pay

print(" The pay for 45 hours at a rate of 10/hr" , + compute_pay(45 , 10) *1.5 , "$")

