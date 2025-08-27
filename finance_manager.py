import json
from dataclasses import dataclass, asdict
from datetime import date
from typing import List


@dataclass
class Transaction:
    amount: float
    category: str
    description: str = ""
    date: str = date.today().isoformat()


class FinanceManager:
    """Simple personal finance manager with JSON persistence."""

    def __init__(self, filepath: str = "finanzas.json") -> None:
        self.filepath = filepath
        self.transactions: List[Transaction] = []
        self.load()

    def load(self) -> None:
        """Load transactions from JSON file."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.transactions = [Transaction(**t) for t in data]
        except FileNotFoundError:
            self.transactions = []

    def save(self) -> None:
        """Persist transactions to JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([asdict(t) for t in self.transactions], f, ensure_ascii=False, indent=2)

    def add_income(self, amount: float, category: str, description: str = "") -> None:
        self.transactions.append(Transaction(amount, category, description))
        self.save()

    def add_expense(self, amount: float, category: str, description: str = "") -> None:
        self.transactions.append(Transaction(-abs(amount), category, description))
        self.save()

    def balance(self) -> float:
        return sum(t.amount for t in self.transactions)

    def summary_by_category(self) -> dict:
        summary: dict[str, float] = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0.0) + t.amount
        return summary

    def list_transactions(self) -> List[Transaction]:
        return list(self.transactions)
