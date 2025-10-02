import pandas as pd

try:
    df = pd.read_csv(
        'C:/Users/darshdeepg/Documents/Recordings/10_02_2025_12_15_58-Exp_W1-Sbj_darsh-Ssn_0.dats',
        encoding= 'utf-8',
        engine='python',         # More flexibility for irregular files
        on_bad_lines='skip'      # Skips lines with incorrect number of fields
    )
    print(df.head())
except Exception as e:
    print("Error occurred:", e)