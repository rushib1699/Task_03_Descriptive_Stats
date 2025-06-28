import pandas as pd
import numpy as np

def analyze_with_pandas(file_path):
    print(f"\n{'='*60}\nAnalyzing file: {file_path}\n{'='*60}")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    print("\n--- Overall Dataset Analysis (Pandas) ---")
    
    print("\nNumeric Columns Summary:")
    print(df.describe(include=[np.number]))
    
    print("\nCategorical Columns Summary:")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"\n- Column: {col}")
        print(f"  Unique Values: {df[col].nunique()}")
        print(f"  Most Frequent Value:\n{df[col].value_counts().head(1)}")

    # [cite_start]Grouped analysis by page_id [cite: 24]
    if 'page_id' in df.columns:
        print("\n\n--- Grouped Analysis by page_id (Pandas) ---")
        grouped_by_page = df.groupby('page_id')
        print(grouped_by_page[df.select_dtypes(include=np.number).columns].mean())
    else:
        print("\n--- Skipping Grouped Analysis by page_id (column not found) ---")

    # [cite_start]Grouped analysis by page_id and ad_id [cite: 24]
    if 'page_id' in df.columns and 'ad_id' in df.columns:
        print("\n\n--- Grouped Analysis by page_id and ad_id (Pandas) ---")
        grouped_by_page_ad = df.groupby(['page_id', 'ad_id'])
        print(grouped_by_page_ad[df.select_dtypes(include=np.number).columns].mean())
    else:
        print("\n--- Skipping Grouped Analysis by page_id and ad_id (one or more columns not found) ---")


if __name__ == "__main__":
    files_to_analyze = [
        "./period_03/2024_fb_ads_president_scored_anon.csv",
        "./period_03/2024_fb_posts_president_scored_anon.csv",
        "./period_03/2024_tw_posts_president_scored_anon.csv"
    ]
    
    for file_name in files_to_analyze:
        analyze_with_pandas(file_name)