# SUGGESTED FILE RENAME: automatic_discount.py

"""
Automatic Discount Calculator
Calculates dynamic pricing discounts based on stock levels and sales ratios.
"""

import os
import pandas as pd


def calculate_new_price_and_discount(row):
    """
    Calculates new price and discount rate based on stock and sales data.
    
    Args:
        row: DataFrame row containing product data
        
    Returns:
        tuple: (new_price, discount_rate)
    """
    stock_quantity = row['Stok_Adedi']
    sales_quantity = row['Satis_Adedi']
    sales_ratio = row['Satis_Orani']
    sale_price = row['Satis_Fiyat']

    # Sales_Ratio = Sales_Quantity / (Sales_Quantity + Stock_Quantity)
    # Can be calculated here if not present in Excel
    
    # If sales and stock data is missing or negative, don't change price
    if pd.isna(stock_quantity) or pd.isna(sales_quantity) or pd.isna(sales_ratio) or stock_quantity < 0 or sales_quantity < 0:
        discount = 0  # Keep price fixed, 0% discount

    # Zero stock products (stock = 0)
    if stock_quantity == 0:
        discount = 0  # Keep price fixed, 0% discount

    # Low stock and low sales ratio (Stock <= 3 and Sales Ratio < 0.34)
    if stock_quantity <= 3 and sales_ratio < 0.34:
        discount = 0.10  # 10% discount
        
    # Low stock and high sales ratio (Stock <= 3 and Sales Ratio >= 0.3)
    elif stock_quantity <= 3 and sales_ratio >= 0.3:
        discount = 0.05  # 5% discount
        
    # Normal stock and low sales ratio (Stock 4-9 and Sales Ratio < 0.3)
    elif 4 <= stock_quantity <= 9 and sales_ratio < 0.3:
        discount = 0.15  # 15% discount
        
    # Normal stock and good sales ratio (Stock 4-9 and 0.3 <= Sales Ratio <= 0.6)
    elif 4 <= stock_quantity <= 9 and sales_ratio >= 0.3 and sales_ratio <= 0.6:
        discount = 0.10  # 10% discount
        
    # Normal stock and high sales ratio (Stock 4-9 and Sales Ratio >= 0.6)
    elif 4 <= stock_quantity <= 9 and sales_ratio >= 0.6:
        discount = 0.05  # 5% discount
        
    # High stock and low sales ratio (Stock >= 10 and Sales Ratio < 0.2)
    elif stock_quantity >= 10 and sales_ratio < 0.2:
        discount = 0.30  # 30% discount
        
    # High stock and good sales ratio (Stock >= 10 and 0.2 <= Sales Ratio <= 0.5)
    elif stock_quantity >= 10 and sales_ratio >= 0.2 and sales_ratio <= 0.5:
        discount = 0.20  # 20% discount

    # High stock and high sales ratio (Stock >= 10 and Sales Ratio >= 0.5)
    elif stock_quantity >= 10 and sales_ratio >= 0.5:
        discount = 0.10  # 10% discount

    else:
        discount = 0  # No discount for other cases
    
    new_price = sale_price * (1 - discount)
    return new_price, discount


# File paths using os.path for cross-platform compatibility
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, 'urun_satis_adetleri_oranlari_stoklari.xlsx')
OUTPUT_FILE = os.path.join(BASE_DIR, 'yeni_satis_fiyatlari.xlsx')

# Read Excel file
df = pd.read_excel(INPUT_FILE)

# Calculate new prices and discount rates
df['Yeni_Fiyat'], df['Yapilan_Indirim'] = zip(*df.apply(calculate_new_price_and_discount, axis=1))

# Save results to new Excel file
df.to_excel(OUTPUT_FILE, index=False)

print(f"Process completed. Results saved to: {OUTPUT_FILE}")
