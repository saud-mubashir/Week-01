"""
Task 1 – Setting up the system and ordering the main items.
Write a program to:
use arrays to store the item code, description and price
allow a customer to choose one case, one RAM and one Main Hard Disk Drive
calculate the price of the computer using the cost of the chosen items and the
basic set of components
store and output the chosen items and the price of the computer
"""

# arrays to store the item code, description and price
case_code = ["A1", "A2"]
case_description = ["Compact", "Tower"]
case_prices = [75.00, 150.00]

ram_code = ["B1", "B2", "B3"]
ram_descriptions = ["8 GB", "16 GB", "32 GB"]
ram_prices = [79.99, 149.99, 299.99]

hard_drives_code = ["C1", "C2", "C3"]
hd_descriptions = ["1 TB HDD", "2 TB HDD", "4 TB HDD"]
hd_prices = [49.99, 89.99, 129.99]

basic_cost = 200

# Allow a customer to choose one case, one RAM and one Main Hard Disk Drive
selected_case = input('Please choose one case \n A1 or A2: ')
selected_ram = input('Please choose one RAM \n B1, B2 or B3: ')
selected_hd = input('Please choose one Main Hard Disk Drive \n C1, C2 or C3: ')

# Validate user inputs

if selected_case not in case_code or selected_ram not in ram_code or selected_hd not in hard_drives_code:
    print("\nPlease enter items from the provided list")
else:
    total_cost = basic_cost + case_prices[case_code.index(selected_case)] + ram_prices[
        ram_code.index(selected_ram)] + hd_prices[hard_drives_code.index(selected_hd)]

# Total Price of computer
print("\nItems Chosen")
print("Case: ", selected_case, "-", case_description[case_code.index(selected_case)])
print("RAM: ", selected_ram, "-", ram_descriptions[ram_code.index(selected_ram)])
print("Main Hard Disk Drive: ", selected_hd, "-", hd_descriptions[hard_drives_code.index(selected_hd)])

print(f"\nPrice of the computer: ${total_cost:.2f}")

"""Task 2 – Ordering additional items.
Extend TASK 1 to:
allow a customer to choose whether to purchase any items from the other
categories – if so, which item(s)
update the price of the computer
store and output the additional items and the new price of the computer
"""

# Additional Items

ssds_code = ["D1", "D2"]
ssd_descriptions = ["240 GB SSD", "480 GB SSD"]
ssd_prices = [59.99, 119.99]

second_hds_code = ["E1", "E2", "E3"]
second_hd_descriptions = ["1 TB HDD", "2 TB HDD", "4 TB HDD"]
second_hd_prices = [49.99, 89.99, 129.99]

optical_drives_code = ["F1", "F2"]
optical_drive_descriptions = ["DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer"]
optical_drive_prices = [50.00, 100.00]

os_versions = ["G1", "G2"]
os_descriptions = ["Standard Version", "Professional Version"]
os_prices = [100.00, 175.00]

# Ask the customer whether they want to purchase additional items
additional_items_choice = input('Do you want to purchase items from other categories? (yes/no): ')

if additional_items_choice.lower() == 'yes':
    # User Input
    print("\nPlease choose additional items")
    print("1. Solid State Drive (SSD)")
    print("2. Second Hard Disk Drive")
    print("3. Optical Drive")
    print("4. Operating System")

    chose = input('Select items number (like 1,2..): ')
    additional_items = chose.split(',')

    additional_items_list = []  # List for storing additional items
    additional_price = 0.0

    for item in additional_items:
        if item == '1':
            ssd_chosen = input('Please choose SSD (D1 or D2): ')

            if ssd_chosen in ssds_code:
                # Add SSD name, description in the list and calculate the price for SSD
                additional_items_list.append(
                    f'SSD: {ssd_chosen} - {ssd_descriptions[ssds_code.index(ssd_chosen)]}')
                additional_price += ssd_prices[ssds_code.index(ssd_chosen)]

            else:
                print('Please choose a valid SSD')

        elif item == '2':
            hds_chosen = input('Choose Second Hard Disk Drive (E1, E2, or E3):')

            if hds_chosen in second_hds_code:
                # Add SSD name, description in the list and calculate the price for the second hard disk
                additional_items_list.append(
                    f'Second Hard Disk Drive: {hds_chosen} - {second_hd_descriptions[second_hds_code.index(hds_chosen)]}')
                additional_price += second_hd_prices[second_hds_code.index(hds_chosen)]

            else:
                print('Please choose a valid Second Hard Disk Drive')

        elif item == '3':
            chosen_optical_drive = input("Choose Optical Drive (F1 or F2): ")
            if chosen_optical_drive in optical_drives_code:
                additional_items_list.append(
                    f"Optical Drive: {chosen_optical_drive} - {optical_drive_descriptions[optical_drives_code.index(chosen_optical_drive)]}")
                additional_price += optical_drive_prices[optical_drives_code.index(chosen_optical_drive)]
            else:
                print("Invalid Optical Drive choice.")

        elif item == '4':
            chosen_os = input("Choose Operating System (G1 or G2): ")
            if chosen_os in os_versions:
                additional_items_list.append(
                    f"Operating System: {chosen_os} - {os_descriptions[os_versions.index(chosen_os)]}")
                additional_price += os_prices[os_versions.index(chosen_os)]
            else:
                print("\nInvalid Operating System.")

    total_cost += additional_price

    # Print additional items and new price of the computer
    print('\nNew Items')
    for item in additional_items_list:
        print(item)
    print(f"\nTotal cost for computer ${total_cost:.2f}")

    """Task 3 – Offering discounts.
    Extend TASK 2 to:
    apply a 5% discount to the price of the computer if the customer has bought only one additional item.
    apply a 10% discount to the price of the computer if the customer has bought two or more additional items.
    output the amount of money saved and the new price of the computer after the
    discount
    """

    if len(additional_items_list) == 1:
        discount_amount = 0.05 * total_cost
        New_Price = total_cost - discount_amount
    elif len(additional_items_list) >= 2:
        discount_amount = 0.1 * total_cost
        New_Price = total_cost - discount_amount

    print("Amount of money saved: ", discount_amount)
    print(f"Final price of the computer after discount: ${New_Price:.2f}")

    value = 5 / 100 * total_cost
    value
else:
    print("\nNo additional items selected. Total cost for the computer remains the same.")
    print(f"Total cost for the computer ${total_cost:.2f}")
