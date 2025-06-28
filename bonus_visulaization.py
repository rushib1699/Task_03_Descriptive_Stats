import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_visualizations(file_list):
    """Loads data from a list of local files, combines them, and creates visualizations."""
    
    all_dfs = []
    for file_path in file_list:
        try:
            df = pd.read_csv(file_path)
            # Add a column to identify the source of the data
            if 'ads' in file_path:
                df['source_platform'] = 'Facebook Ads'
            elif 'fb_posts' in file_path:
                df['source_platform'] = 'Facebook Posts'
            elif 'tw_posts' in file_path:
                df['source_platform'] = 'Twitter Posts'
            all_dfs.append(df)
        except FileNotFoundError:
            print(f"Warning: The file was not found at {file_path}. Skipping.")
        except Exception as e:
            print(f"An error occurred with {file_path}: {e}. Skipping.")
    
    if not all_dfs:
        print("No data could be loaded. Exiting visualization script.")
        return

    # Combine all dataframes, aligning on common columns and keeping unique ones
    combined_df = pd.concat(all_dfs, ignore_index=True, sort=False)

    print("--- Generating Combined Visualizations ---")
    
    # Set plot style
    sns.set_style("whitegrid")

    # 1. Bar Chart: Count of entries by platform
    plt.figure(figsize=(10, 6))
    sns.countplot(y='source_platform', data=combined_df, palette='cividis')
    plt.title('Volume of Social Media Activity by Platform')
    plt.xlabel('Count of Entries')
    plt.ylabel('Platform')
    plt.tight_layout()
    plt.savefig('platform_activity_count.png')
    print("Saved 'platform_activity_count.png'")
    plt.show()

    # --- Narrative: Comparing Engagement Across Platforms ---
    # We can analyze shared engagement metrics. Let's assume a common metric like 'reactions_total'
    # exists or can be synthesized from columns like 'likes', 'comments', 'shares'.
    # For this example, we'll create a 'total_engagement' column.
    
    # Coalesce engagement columns. Fill NaN with 0 before adding.
    # Note: Column names might differ. Adjust as needed based on actual file headers.
    reaction_cols = ['reactions_total', 'favorite_count', 'retweet_count', 'like_count', 'comment_count']
    for col in reaction_cols:
        if col not in combined_df.columns:
            combined_df[col] = 0 # Add missing columns and fill with 0
        else:
            combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce').fillna(0)
            
    combined_df['total_engagement'] = combined_df[reaction_cols].sum(axis=1)

    # 2. Box Plot of Engagement by Platform
    plt.figure(figsize=(12, 7))
    sns.boxplot(x='source_platform', y='total_engagement', data=combined_df, palette='magma')
    plt.title('Distribution of Engagement by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Total Engagement (Reactions, Shares, etc.)')
    plt.yscale('log') # Use log scale as engagement is often highly skewed
    plt.tight_layout()
    plt.savefig('platform_engagement_boxplot.png')
    print("Saved 'platform_engagement_boxplot.png'")
    plt.show()

    # 3. Ad Spend Analysis (only for the ads data)
    ad_df = combined_df[combined_df['source_platform'] == 'Facebook Ads'].copy()
    if not ad_df.empty and 'spend' in ad_df.columns:
        ad_df['spend'] = pd.to_numeric(ad_df['spend'], errors='coerce')
        ad_df.dropna(subset=['spend'], inplace=True)
        
        # Check if there is spend data to plot
        if not ad_df.empty and ad_df['spend'].sum() > 0:
            plt.figure(figsize=(12, 8))
            top_10_spenders = ad_df.groupby('page_name')['spend'].sum().nlargest(10)
            sns.barplot(x=top_10_spenders.values, y=top_10_spenders.index, palette='viridis')
            plt.title('Top 10 Facebook Ad Spenders')
            plt.xlabel('Total Spend (USD)')
            plt.ylabel('Page Name')
            plt.tight_layout()
            plt.savefig('top_ad_spenders_barchart.png')
            print("Saved 'top_ad_spenders_barchart.png'")
            plt.show()
        else:
            print("No valid ad spend data to visualize.")
    else:
        print("No ad data or 'spend' column found for spend analysis.")

if __name__ == "__main__":
    files_to_analyze =  files_to_analyze = [
        "./period_03/2024_fb_ads_president_scored_anon.csv",
        "./period_03/2024_fb_posts_president_scored_anon.csv",
        "./period_03/2024_tw_posts_president_scored_anon.csv"
    ]
    create_visualizations(files_to_analyze)