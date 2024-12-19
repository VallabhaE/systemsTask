import pandas as pd

def calculate_sma(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    sma_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    #Updating SMA VALUES
    for col in sma_columns:
        sma_col_name = f'SMA({col}) 10D'
        if sma_col_name in df.columns:
            # Calculate SMA for each day, starting from the first row
            df[sma_col_name] = df[col].rolling(window=10, min_periods=1).mean()

    # Save the updated
    output_file_path = "output_with_sma.csv"
    df.to_csv(output_file_path, index=False)
    print(f"SMA columns updated successfully! Output saved to {output_file_path}")

# Replace 'input.csv' with the path to your actual CSV file
calculate_sma('RELIANCE.csv')
