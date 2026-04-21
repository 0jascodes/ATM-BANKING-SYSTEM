# Main Entry Point
from atm import atm_operations as atm

def main():
    print("═════════════════════════════════════════")
    print("🏦 Welcome to the Python ATM Simulation 🏦")
    print("═════════════════════════════════════════\n")
    
    # PIN authentication at startup
    if not atm.authenticate():
        return
        
    # Infinite loop for the menu
    while True:
        print("────────── MAIN MENU ──────────")
        print("1️⃣ Display Balance")
        print("2️⃣ Withdraw Money")
        print("3️⃣ Deposit Money")
        print("4️⃣ Mini Statement")
        print("5️⃣ Exit")
        print("───────────────────────────────")
        
        choice = input("👉 Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            atm.display_balance()
        elif choice == '2':
            atm.withdraw_money()
        elif choice == '3':
            atm.deposit_money()
        elif choice == '4':
            atm.mini_statement()
        elif choice == '5':
            print("👋 Thank you for using the ATM. Goodbye!")
            print("═════════════════════════════════════════")
            break
        else:
            print("❌ Invalid choice. Please select an option from 1 to 5.\n")

if __name__ == "__main__":
    main()
