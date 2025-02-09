def main():

    num_customers = int(input("Number of customers: "))
    overall_total = 0

    for customer in range(1, num_customers + 1):
        print(f"\nCustomer {customer}")

        num_items = int(input("Number of items purchased: "))
        customer_total = 0

        for item in range(1, num_items + 1):
            price = float(input(f"price of item {item}: "))
            customer_total += price

        print(f"Total bill for Customer {customer}: TK{customer_total:.2f}")
        overall_total += customer_total
    print(f"\nOverall total for the day: TK{overall_total:.2f}")

if __name__ == "__main__":
    main()
