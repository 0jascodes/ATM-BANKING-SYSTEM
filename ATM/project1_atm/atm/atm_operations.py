import datetime

# --- System State Variables ---
# In a real system, these would be stored in a database or file.
_PIN = "1234"
_balance = 0.0
_transactions = []
_attempts = 0
_MAX_ATTEMPTS = 3
_is_locked = False

# --- Helper Functions ---
def _format_currency(amount):
    """Format the amount to Indian Rupees (₹) with 2 decimal places and comma separator."""
    return f"₹ {amount:,.2f}"

def _record_transaction(trans_type, amount):
    """Record a transaction in the history."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _transactions.append({
        "date": now,
        "type": trans_type,
        "amount": amount,
        "balance": _balance
    })

# --- Main Operations ---

def authenticate():
    """Handle PIN authentication at startup (max 3 attempts)."""
    global _attempts, _is_locked
    
    if _is_locked:
        print("❌ Your account is locked due to too many failed attempts.")
        return False
        
    while _attempts < _MAX_ATTEMPTS:
        entered_pin = input("🔑 Enter your 4-digit PIN: ")
        if entered_pin == _PIN:
            print("✅ Authentication successful!\n")
            return True
        else:
            _attempts += 1
            remaining = _MAX_ATTEMPTS - _attempts
            if remaining > 0:
                print(f"❌ Incorrect PIN. You have {remaining} attempts remaining.")
            
    _is_locked = True
    print("❌ Account locked. Too many failed attempts.")
    return False

def display_balance():
    """Display the current balance with formatting."""
    print("════════════ BALANCE ════════════")
    print(f"🏦 Current Balance: {_format_currency(_balance)}")
    print("═════════════════════════════════\n")

def withdraw_money():
    """Withdraw money from the account."""
    global _balance
    print("────────── WITHDRAW MONEY ──────────")
    try:
        amount_str = input("💸 Enter amount to withdraw (Multiples of 100): ")
        amount = float(amount_str)
        
        # Validation checks
        if amount <= 0:
            print("❌ Invalid amount. Please enter a positive value.\n")
            return
            
        if amount % 100 != 0:
            print("❌ Invalid amount. Must be in multiples of 100.\n")
            return
            
        if amount > _balance:
            print(f"❌ Insufficient funds. Your current balance is {_format_currency(_balance)}.\n")
            return
            
        # Perform withdrawal
        _balance -= amount
        _record_transaction("DEBIT", amount)
        print(f"✅ Successfully withdrew {_format_currency(amount)}.")
        print(f"💰 New Balance: {_format_currency(_balance)}\n")
        
    except ValueError:
        print("❌ Invalid input. Please enter a valid numerical amount.\n")

def deposit_money():
    """Deposit money into the account."""
    global _balance
    print("────────── DEPOSIT MONEY ──────────")
    try:
        amount_str = input("💰 Enter amount to deposit: ")
        amount = float(amount_str)
        
        if amount <= 0:
            print("❌ Invalid amount. Please enter a positive value.\n")
            return
            
        # Perform deposit
        _balance += amount
        _record_transaction("CREDIT", amount)
        print(f"✅ Successfully deposited {_format_currency(amount)}.")
        print(f"💰 New Balance: {_format_currency(_balance)}\n")
        
    except ValueError:
        print("❌ Invalid input. Please enter a valid numerical amount.\n")

def mini_statement():
    """Display the transaction history."""
    print("════════════════════════════════ MINI STATEMENT ════════════════════════════════")
    if not _transactions:
        print("📝 No transactions available yet.")
    else:
        # Header
        print(f"{'Date & Time':<20} | {'Type':<8} | {'Amount':<15} | {'Running Balance'}")
        print("────────────────────────────────────────────────────────────────────────────────")
        # Rows
        for t in _transactions:
            date_time = t['date']
            t_type = t['type']
            amount = _format_currency(t['amount'])
            balance = _format_currency(t['balance'])
            print(f"{date_time:<20} | {t_type:<8} | {amount:<15} | {balance}")
    print("════════════════════════════════════════════════════════════════════════════════\n")
