import random

def generate_voucher_code():
    """Generate a random voucher code."""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    code = "".join(random.choices(letters, k=3))
    code += "-".join([random.choices(digits, k=4) for _ in range(3)])
    return code

class VoucherSystem:
    """Manage a voucher system."""
    
    def __init__(self):
        self.vouchers = []
        
    def add_voucher(self, code):
        """Add a voucher to the system."""
        self.vouchers.append(code)
        
    def remove_voucher(self, code):
        """Remove a voucher from the system."""
        if code in self.vouchers:
            self.vouchers.remove(code)
        else:
            raise ValueError("Voucher code not found.")
            
    def check_voucher(self, code):
        """Check if a voucher is valid."""
        if code in self.vouchers:
            return True
        else:
            return False
