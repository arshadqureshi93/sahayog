# custom_app/overrides/employee.py

import frappe
from frappe import _

def override_validate_for_enabled_user_id(self, enabled):
    if not self.status == "Active":
        return

    if enabled is None:
        return  # Simply return without throwing an error

    if enabled == 0:
        return  # Simply return without throwing an error if the user is disabled
