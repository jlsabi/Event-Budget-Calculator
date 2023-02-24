print("Event Budget Calculator")

budget = int(input("Enter the budget: "))

# Cost calculations
venue_cost = float(input("Enter the cost of the venue: "))
promo_cost = float(input("Enter the cost of the promotion: "))
dj_cost = float(input("Enter the cost of the DJ: "))
video_photo = float(input("Enter the cost of the videographer and photographer: "))
led_cost = float(input("Enter the cost of the LED: "))
travel_accommodation = float(input("Enter the cost of travel and accommodation: "))
clothes_and_accessories = float(input("Enter the cost of clothes and accessories: "))
artist_cost = float(input("Enter the cost of the artist: "))
other = float(input("Enter the extra cost: "))

total_cost = venue_cost + promo_cost + dj_cost + video_photo + led_cost + travel_accommodation + clothes_and_accessories + artist_cost + other
total = budget - total_cost

# Revenue calculations
early_bird_price = int(input("Enter the price for early bird tickets: "))
early_bird_sold = int(input("Enter the number of early bird tickets sold: "))
first_release_price = int(input("Enter the price for first release tickets: "))
first_release_sold = int(input("Enter the number of first release tickets sold: "))
second_release_price = int(input("Enter the price for second release tickets: "))
second_release_sold = int(input("Enter the number of second release tickets sold: "))
final_release_price = int(input("Enter the price for final release tickets: "))
final_release_sold = int(input("Enter the number of final release tickets sold: "))

early_bird_revenue = early_bird_price * early_bird_sold
first_release_revenue = first_release_price * first_release_sold
second_release_revenue = second_release_price * second_release_sold
final_release_revenue = final_release_price * final_release_sold

total_revenue = early_bird_revenue + first_release_revenue + second_release_revenue + final_release_revenue

# Profit and commission calculations
profit = total_revenue - total_cost

if profit > 0:
    commission = float(input("Enter the commission percentage: "))
    commission_amount = profit * commission / 100
    print(f"The profit from the event is: {profit}")
    print(f"The commission amount is: {commission_amount}")
else:
    print(f"The event has not made a profit. There is no commission to be paid.")

# Total tickets sold calculation
total_tickets_sold = early_bird_sold + first_release_sold + second_release_sold + final_release_sold
print(f"The total number of tickets sold is: {total_tickets_sold}")

# Club capacity calculation
club_capacity = int(input("Enter the capacity of the club: "))
if total_tickets_sold > club_capacity:
    print("The number of tickets sold exceeds the club capacity.")
else:
    remaining_tickets = club_capacity - total_tickets_sold
    print(f"The number of tickets sold is within the club capacity. {remaining_tickets} tickets remaining.")

# Average ticket price calculation
average_ticket_price = total_revenue / total_tickets_sold
print(f"The average ticket price is: {average_ticket_price}")

# Total cost per ticket calculation
total_cost_per_ticket = total_cost / total_tickets_sold
print(f"The total cost per ticket is: {total_cost_per_ticket}")

## Profit per ticket calculation
profit_per_ticket = (total_revenue - total_cost) / total_tickets_sold
print(f"The profit per ticket is: {profit_per_ticket}")
