import pandas as pd

#  Verify the user's credentials.
    
#   Parameters:
#   ic_number (str): The IC number of the user.
#   password (str): The password (last 4 digits of the IC number).

#   Returns:
#   bool: True if the credentials are valid, False otherwise.
def verify_user(ic_number, password):
    if len(ic_number) != 12:
        return False
    if password != ic_number[-4:]:
        return False
    return True

# Calculate the tax payable based on the income and tax relief.
def calculate_tax(income, tax_relief):
    taxable_income = income - tax_relief
    if taxable_income <= 5000:
        tax = 0
    elif taxable_income <= 20000:
        tax = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax = (taxable_income - 20000) * 0.03 + 150
    elif taxable_income <= 50000:
        tax = (taxable_income - 35000) * 0.06 + 600
    elif taxable_income <= 70000:
        tax = (taxable_income - 50000) * 0.11 + 1500
    elif taxable_income <= 100000:
        tax = (taxable_income - 70000) * 0.19 + 3700
    elif taxable_income <= 400000:
        tax = (taxable_income - 100000) * 0.25 + 9400
    elif taxable_income <= 600000:
        tax = (taxable_income - 400000) * 0.26 + 84400
    elif taxable_income <= 2000000:
        tax = (taxable_income - 600000) * 0.28 + 136400
    else:
        tax = (taxable_income - 2000000) * 0.30 + 528400    
    return tax

# Save the user's data to a CSV file.

#    Parameters:
#    data (dict): The user's data including IC number, income, tax relief, and tax payable.
#    filename (str): The name of the CSV file.
def save_to_csv(data, filename):
    df = pd.DataFrame([data], columns=['IC Number', 'Income', 'Tax Relief', 'Tax Payable'])
    try:
        existing_df = pd.read_csv(filename)
        df.to_csv(filename, mode='a', header=False, index=False)
    except FileNotFoundError:
        df.to_csv(filename, index=False)

#Read data from a CSV file.

#    Parameters:
#   filename (str): The name of the CSV file.

#    Returns:
#    pd.DataFrame or None: A DataFrame containing the data if the file exists, None otherwise.
def read_from_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None
