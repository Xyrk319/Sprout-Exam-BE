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
    
    @staticmethod
    def fromValueToText(value):
        print("From Value To Text", value)
        if value == EmployeeTypes.REGULAR:
            return EmployeeTypes.REGULAR.text()
        elif value == EmployeeTypes.CONTRACTUAL:
            return EmployeeTypes.CONTRACTUAL.text()
        else:
            return "Unknown"
    
    @staticmethod
    def employeeTypeList():
        return [
            {
                "id": EmployeeTypes.REGULAR.value,
                "text": EmployeeTypes.REGULAR.text()
            }, 
            {
                "id": EmployeeTypes.CONTRACTUAL.value,
                "text": EmployeeTypes.CONTRACTUAL.text()
            }
        ]