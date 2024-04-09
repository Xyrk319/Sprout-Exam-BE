from enum import Enum


class EmployeeTypes(Enum):
    REGULAR = 1
    CONTRACTUAL = 2

    def text(self):
        if self == EmployeeTypes.REGULAR:
            return "Regular"
        elif self == EmployeeTypes.CONTRACTUAL:
            return "Contractual"
        else:
            return "Unknown"