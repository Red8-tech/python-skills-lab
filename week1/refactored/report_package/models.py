from dataclasses import dataclass


@dataclass
class EmployeeRecord:
    id: str
    name: str
    department: str
    sales: float
    orders: int
