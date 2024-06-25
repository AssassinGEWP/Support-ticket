import json
import datetime


def load_issue_categories(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def create_ticket(ticket_id, issue_categories):
    print("\nCreate a New Ticket")
    print("===================")
    
    print("Select an issue category:")
    for idx, category in enumerate(issue_categories, start=1):
        print(f"{idx}. {category}")
    
    category_choice = int(input("Enter the number of the category: "))
    selected_category = list(issue_categories.keys())[category_choice - 1]

    print("\nSelect an issue type:")
    for idx, issue in enumerate(issue_categories[selected_category], start=1):
        print(f"{idx}. {issue}")
    
    issue_choice = int(input("Enter the number of the issue: "))
    selected_issue = issue_categories[selected_category][issue_choice - 1]

    description = input("\nDescribe the issue in detail: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ticket = {
        "Ticket ID": ticket_id,
        "Category": selected_category,
        "Issue": selected_issue,
        "Description": description,
        "Timestamp": timestamp
    }
    
    return ticket

def display_tickets(tickets):
    if not tickets:
        print("\nNo tickets found.")
        return
    
    print("\nSupport Tickets")
    print("================")
    for ticket in tickets:
        print(f"\nTicket ID: {ticket['Ticket ID']}")
        print(f"Category: {ticket['Category']}")
        print(f"Issue: {ticket['Issue']}")
        print(f"Description: {ticket['Description']}")
        print(f"Timestamp: {ticket['Timestamp']}")
        print("-------------------")

def main():
    issue_categories = load_issue_categories('issue_categories.json')
    tickets = []
    ticket_id = 1

    while True:
        print("\nWelcome To Technical Support Ticketing System")
        print("===================================")
        print("1. Create a new ticket")
        print("2. View all tickets")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            ticket = create_ticket(ticket_id, issue_categories)
            tickets.append(ticket)
            ticket_id += 1
            print("\nTicket created successfully!")
        elif choice == '2':
            display_tickets(tickets)
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
