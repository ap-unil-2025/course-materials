---
layout: project
title: "Design Patterns in Banking System"
type: "Programming Concepts"
featured: true
summary: "Educational demonstration of key design patterns including Strategy, Observer, and Factory patterns in a simplified banking context."
technologies:
  - "Python 3.11"
  - "ABC (Abstract Base Classes)"
  - "Type Hints"
  - "Design Patterns"
tags:
  - "Design Patterns"
  - "Object-Oriented Programming"
  - "Software Architecture"
  - "Code Organization"
learning_objectives:
  - "Strategy Pattern Implementation"
  - "Observer Pattern for Event Handling" 
  - "Factory Pattern for Object Creation"
  - "Clean Code Principles"
status: "Educational Example"
---

## ⚠️ Educational Content Notice
**This is a DEMO/EDUCATIONAL example showing programming concepts. It is NOT related to any course project and contains no project solutions.**

## Overview

This educational example demonstrates how classic design patterns can be applied to create maintainable, extensible software. Using a simplified banking system context, we showcase key patterns that every advanced programmer should understand.

## Learning Objectives

By studying this example, you will understand:
- **Strategy Pattern**: How to encapsulate algorithms and make them interchangeable
- **Observer Pattern**: Event-driven programming and loose coupling
- **Factory Pattern**: Object creation abstraction
- **SOLID Principles**: Writing maintainable object-oriented code

## Design Patterns Demonstrated

### 1. Strategy Pattern - Interest Calculation

Different account types use different interest calculation strategies:

```python
from abc import ABC, abstractmethod
from typing import Protocol

class InterestStrategy(Protocol):
    """Strategy interface for interest calculations."""
    
    def calculate_interest(self, balance: float, days: int) -> float:
        """Calculate interest for given balance and period."""
        ...

class SavingsInterestStrategy:
    """Strategy for savings account interest calculation."""
    
    def __init__(self, annual_rate: float = 0.02):
        self.annual_rate = annual_rate
    
    def calculate_interest(self, balance: float, days: int) -> float:
        """Calculate compound interest for savings."""
        daily_rate = self.annual_rate / 365
        return balance * (1 + daily_rate) ** days - balance

class PremiumInterestStrategy:
    """Strategy for premium account with tiered rates."""
    
    def __init__(self, base_rate: float = 0.03, bonus_rate: float = 0.01):
        self.base_rate = base_rate
        self.bonus_rate = bonus_rate
        self.threshold = 10000
    
    def calculate_interest(self, balance: float, days: int) -> float:
        """Calculate tiered interest for premium accounts."""
        if balance > self.threshold:
            rate = self.base_rate + self.bonus_rate
        else:
            rate = self.base_rate
        
        daily_rate = rate / 365
        return balance * (1 + daily_rate) ** days - balance

class Account:
    """Account class using Strategy pattern."""
    
    def __init__(self, account_id: str, initial_balance: float, 
                 interest_strategy: InterestStrategy):
        self.account_id = account_id
        self.balance = initial_balance
        self.interest_strategy = interest_strategy
    
    def calculate_interest(self, days: int) -> float:
        """Delegate interest calculation to strategy."""
        return self.interest_strategy.calculate_interest(self.balance, days)
    
    def set_interest_strategy(self, strategy: InterestStrategy):
        """Change interest calculation strategy at runtime."""
        self.interest_strategy = strategy
```

### 2. Observer Pattern - Account Notifications

Implement event-driven notifications when account events occur:

```python
from typing import List, Protocol

class AccountObserver(Protocol):
    """Observer interface for account events."""
    
    def notify(self, account_id: str, event_type: str, data: dict) -> None:
        """Handle account event notification."""
        ...

class EmailNotifier:
    """Observer that sends email notifications."""
    
    def __init__(self, email_address: str):
        self.email_address = email_address
    
    def notify(self, account_id: str, event_type: str, data: dict) -> None:
        """Send email notification for account events."""
        print(f"📧 Email to {self.email_address}:")
        print(f"   Account {account_id}: {event_type}")
        print(f"   Details: {data}")

class AuditLogger:
    """Observer that logs all account activities."""
    
    def __init__(self, log_file: str = "audit.log"):
        self.log_file = log_file
    
    def notify(self, account_id: str, event_type: str, data: dict) -> None:
        """Log account event for audit purposes."""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {account_id}: {event_type} - {data}"
        print(f"📝 Audit Log: {log_entry}")

class ObservableAccount(Account):
    """Account class that supports observers (Observable pattern)."""
    
    def __init__(self, account_id: str, initial_balance: float, 
                 interest_strategy: InterestStrategy):
        super().__init__(account_id, initial_balance, interest_strategy)
        self._observers: List[AccountObserver] = []
    
    def add_observer(self, observer: AccountObserver) -> None:
        """Add an observer to receive notifications."""
        self._observers.append(observer)
    
    def remove_observer(self, observer: AccountObserver) -> None:
        """Remove an observer."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self, event_type: str, data: dict) -> None:
        """Notify all observers of an account event."""
        for observer in self._observers:
            observer.notify(self.account_id, event_type, data)
    
    def deposit(self, amount: float) -> None:
        """Deposit money and notify observers."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        old_balance = self.balance
        self.balance += amount
        
        self._notify_observers("DEPOSIT", {
            "amount": amount,
            "old_balance": old_balance,
            "new_balance": self.balance
        })
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money and notify observers."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        old_balance = self.balance
        self.balance -= amount
        
        self._notify_observers("WITHDRAWAL", {
            "amount": amount,
            "old_balance": old_balance,
            "new_balance": self.balance
        })
```

### 3. Factory Pattern - Account Creation

Centralize account creation logic using the Factory pattern:

```python
from enum import Enum
from typing import Dict, Type

class AccountType(Enum):
    """Enumeration of available account types."""
    SAVINGS = "savings"
    PREMIUM = "premium"
    STUDENT = "student"

class AccountFactory:
    """Factory class for creating different types of accounts."""
    
    def __init__(self):
        self._strategies: Dict[AccountType, InterestStrategy] = {
            AccountType.SAVINGS: SavingsInterestStrategy(annual_rate=0.02),
            AccountType.PREMIUM: PremiumInterestStrategy(base_rate=0.03, bonus_rate=0.01),
            AccountType.STUDENT: SavingsInterestStrategy(annual_rate=0.01)  # Lower rate
        }
        self._minimum_balances: Dict[AccountType, float] = {
            AccountType.SAVINGS: 100.0,
            AccountType.PREMIUM: 5000.0,
            AccountType.STUDENT: 0.0
        }
    
    def create_account(self, account_type: AccountType, account_id: str, 
                      initial_balance: float) -> ObservableAccount:
        """Create an account of the specified type."""
        min_balance = self._minimum_balances[account_type]
        if initial_balance < min_balance:
            raise ValueError(f"{account_type.value} account requires minimum ${min_balance}")
        
        strategy = self._strategies[account_type]
        account = ObservableAccount(account_id, initial_balance, strategy)
        
        # Add default observers based on account type
        if account_type == AccountType.PREMIUM:
            # Premium accounts get email notifications
            email_notifier = EmailNotifier("premium@bank.com")
            account.add_observer(email_notifier)
        
        # All accounts get audit logging
        audit_logger = AuditLogger()
        account.add_observer(audit_logger)
        
        return account
    
    def get_account_types(self) -> List[AccountType]:
        """Return list of available account types."""
        return list(AccountType)
```

## Usage Example

Here's how these patterns work together:

```python
def main():
    """Demonstrate the design patterns in action."""
    
    # Create factory
    factory = AccountFactory()
    
    # Create different types of accounts
    savings_account = factory.create_account(
        AccountType.SAVINGS, "SAV001", 1000.0
    )
    
    premium_account = factory.create_account(
        AccountType.PREMIUM, "PREM001", 15000.0
    )
    
    # Add custom observers
    email_notifier = EmailNotifier("customer@example.com")
    savings_account.add_observer(email_notifier)
    
    # Perform operations (Observer pattern in action)
    print("=== Performing account operations ===")
    savings_account.deposit(500.0)
    premium_account.withdraw(1000.0)
    
    # Calculate interest (Strategy pattern in action)
    print("\n=== Interest calculations ===")
    savings_interest = savings_account.calculate_interest(30)  # 30 days
    premium_interest = premium_account.calculate_interest(30)
    
    print(f"Savings interest (30 days): ${savings_interest:.2f}")
    print(f"Premium interest (30 days): ${premium_interest:.2f}")
    
    # Change strategy at runtime (Strategy pattern flexibility)
    print("\n=== Changing interest strategy ===")
    new_strategy = PremiumInterestStrategy(base_rate=0.04, bonus_rate=0.015)
    savings_account.set_interest_strategy(new_strategy)
    
    new_interest = savings_account.calculate_interest(30)
    print(f"Savings with premium strategy: ${new_interest:.2f}")

if __name__ == "__main__":
    main()
```

## Key Takeaways

### Design Pattern Benefits
- **Strategy Pattern**: Makes algorithms interchangeable and testable
- **Observer Pattern**: Enables loose coupling and event-driven architecture  
- **Factory Pattern**: Centralizes object creation and reduces dependencies

### Software Engineering Principles
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Dependency Inversion**: Depend on abstractions, not concretions
- **Composition over Inheritance**: Flexible object relationships

### Testing Benefits
Each pattern makes the code more testable:
- **Strategy**: Mock different calculation strategies
- **Observer**: Test event handling in isolation
- **Factory**: Control object creation in tests

## Further Learning

To deepen your understanding:
1. **Read**: "Design Patterns" by Gang of Four
2. **Practice**: Implement other patterns (Decorator, Command, State)
3. **Apply**: Use patterns in your own projects where appropriate
4. **Analyze**: Study how popular frameworks use these patterns

Remember: Design patterns are tools, not rules. Use them when they solve real problems and improve code maintainability.

---

*This example demonstrates professional software design principles that apply across all programming domains.*