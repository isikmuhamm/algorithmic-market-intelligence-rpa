"""
Price Detective - Main Application
Automated competitor price monitoring and analysis system.
Reads products from Excel, scrapes prices from Turkish e-commerce platforms,
and exports statistical analysis results.
"""

import pandas as pd
import os
from scrapper import get_results
from connection import setup_driver


# Read Excel input file
INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'urunler.xlsx')
df = pd.read_excel(INPUT_FILE)

# Create output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def calculate_prices(products):
    """
    Calculates min, average, and max prices from a list of products.
    
    Args:
        products: List of tuples (product_name, price_string)
    
    Returns:
        tuple: (min_price, avg_price, max_price) or (None, None, None) if no valid prices
    """
    prices = []
    for price in products:
        try:
            # Clean price string: remove TL currency, thousand separators (dots), 
            # convert decimal separator (comma) to dot
            clean_price = price[1].replace(' TL', '').replace('.', '').replace(',', '.').replace('\xa0', '').strip()
            
            # Handle multiple dots (thousand separators)
            if clean_price.count('.') > 1:
                parts = clean_price.split('.')
                clean_price = parts[0] + ''.join(parts[1:])

            prices.append(float(clean_price))
        except (ValueError, IndexError) as e:
            # Skip if conversion fails
            continue

    # Return min, average, max if valid prices exist
    if prices:
        return min(prices), sum(prices) / len(prices), max(prices)
    
    # Return None if no valid prices
    return None, None, None


# Process each product
for index, row in df.iterrows():
    product_name = row['Urun_Adi']
    product_code = row['Urun_Kodu']

    print(f"\n\n{product_code} - Running program for {product_name}...")

    # Restart driver each iteration due to Ciceksepeti bot protection
    # This reduces performance but no other solution found
    driver = setup_driver()
    
    # Search each platform
    results = get_results(product_name, driver)
    driver.quit()
    
    # Write output to file
    output_file = os.path.join(OUTPUT_DIR, f"{product_code}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Product Code: {product_code}\nProduct Name: {product_name}\n\n")
        for site, products in results.items():
            f.write(f"{site} Results:\n")
            for prod_name, price in products:
                f.write(f"{prod_name}: {price}\n")
            f.write("\n")

    # Calculate prices for each platform
    site_prices = {}
    for site, products in results.items():
        min_price, avg_price, max_price = calculate_prices(products)
        site_prices[site] = {
            'Min': min_price,
            'Avg': avg_price,
            'Max': max_price
        }

    # Add results to DataFrame
    for site, prices in site_prices.items():
        df.at[index, f"{site} Min"] = prices['Min']
        df.at[index, f"{site} Avg"] = prices['Avg']
        df.at[index, f"{site} Max"] = prices['Max']


# Save updated data to new Excel file
OUTPUT_EXCEL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'urunler_sonuc.xlsx')
df.to_excel(OUTPUT_EXCEL_FILE, index=False)

print("Process completed. Results saved to 'output' folder and 'urunler_sonuc.xlsx' file.")
