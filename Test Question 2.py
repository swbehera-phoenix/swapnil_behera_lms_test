flight_no = "A1203" 
base_fare = "4500.75"
tax_percent= "5"
seat_numbers = "12A,12B,14C,15D" 
is_international = "True"

final_fare = float(base_fare)+(float(base_fare)*int(tax_percent)/100)
print(final_fare)

seat_list = seat_numbers.split(",")
print(seat_list)

seat_set = set(seat_list)
print(seat_set)

con_is_international = bool(is_international)
print(con_is_international)


flight_summary = {
    "flight_no": flight_no,
    "final_fare": int(final_fare),
    "seat_numbers": tuple(seat_list)
}
print(flight_summary)
