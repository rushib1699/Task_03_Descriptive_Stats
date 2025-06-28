import polars as pl

def analyze_with_polars(file_path):
    print(f"\n{'='*60}\nAnalyzing file: {file_path}\n{'='*60}")
    try:
        df = pl.read_csv(file_path, ignore_errors=True) 
    except Exception as e:
        print(f"Error loading file with Polars: {e}")
        return

    print("\n--- Overall Dataset Analysis (Polars) ---")
    print(df.describe())
    
    print("\nCategorical Columns Summary:")
    for col in df.select(pl.col(pl.Utf8)).columns:
        print(f"\n- Column: {col}")
        print(f"  Unique Values: {df[col].n_unique()}")
        print(f"  Most Frequent Value:\n{df[col].value_counts().head(1)}")

    # [cite_start]Grouped analysis by page_id [cite: 24]
    if 'page_id' in df.columns:
        print("\n\n--- Grouped Analysis by page_id (Polars) ---")
        print(df.group_by('page_id').agg(pl.col(pl.NUMERIC_DTYPES).mean()))
    else:
         print("\n--- Skipping Grouped Analysis by page_id (column not found) ---")

    # [cite_start]Grouped analysis by page_id and ad_id [cite: 24]
    if 'page_id' in df.columns and 'ad_id' in df.columns:
        print("\n\n--- Grouped Analysis by page_id and ad_id (Polars) ---")
        print(df.group_by(['page_id', 'ad_id']).agg(pl.col(pl.NUMERIC_DTYPES).mean()))
    else:
        print("\n--- Skipping Grouped Analysis by page_id and ad_id (one or more columns not found) ---")


if __name__ == "__main__":
    files_to_analyze = [
        "./period_03/2024_fb_ads_president_scored_anon.csv",
        "./period_03/2024_fb_posts_president_scored_anon.csv",
        "./period_03/2024_tw_posts_president_scored_anon.csv"
    ]

    for file_name in files_to_analyze:
        analyze_with_polars(file_name)