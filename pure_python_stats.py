import csv
import math
from collections import Counter
from itertools import groupby
from operator import itemgetter

def load_csv_from_local(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def get_numeric_stats(data, column):
    values = []
    for row in data:
        value_str = row.get(column)
        if value_str and value_str not in ('NA', ''):
            try:
                values.append(float(value_str))
            except (ValueError, TypeError):
                continue

    if not values:
        return {'count': 0, 'mean': 'N/A', 'min': 'N/A', 'max': 'N/A', 'std_dev': 'N/A'}

    count = len(values)
    mean = sum(values) / count
    min_val = min(values)
    max_val = max(values)
    variance = sum([(x - mean) ** 2 for x in values]) / count
    std_dev = math.sqrt(variance)
    
    return {'count': count, 'mean': f"{mean:.2f}", 'min': min_val, 'max': max_val, 'std_dev': f"{std_dev:.2f}"}

def get_categorical_stats(data, column):
    
    values = [row[column] for row in data if row.get(column) and row[column] not in ('NA', '')]
    if not values:
        return {'unique_values': 0, 'most_frequent': ('N/A', 0)}
        
    value_counts = Counter(values)
    unique_values = len(value_counts)
    most_frequent = value_counts.most_common(1)[0] if value_counts else ('N/A', 0)
    
    return {'unique_values': unique_values, 'most_frequent': most_frequent}

def analyze_dataframe(data):

    if not data or not data[0]:
        print("No data or headers found to analyze.")
        return

    headers = data[0].keys()
    for column in headers:
        is_numeric = False
        for row in data:
            val = row.get(column)
            if val and val not in ('NA', ''):
                try:
                    float(val)
                    is_numeric = True
                    break
                except (ValueError, TypeError):
                    is_numeric = False
                    break
        
        print(f"\n- Column: {column}")
        if is_numeric:
            stats = get_numeric_stats(data, column)
            print(f"  Type: Numeric\n  Count: {stats['count']}\n  Mean: {stats['mean']}\n  Min: {stats['min']}\n  Max: {stats['max']}\n  Std Dev: {stats['std_dev']}")
        else:
            stats = get_categorical_stats(data, column)
            print(f"  Type: Categorical\n  Unique Values: {stats['unique_values']}\n  Most Frequent: '{stats['most_frequent'][0]}' (occurs {stats['most_frequent'][1]} times)")

def analyze_grouped(data, group_by_keys):

    if not data: return
    
    headers = data[0].keys()
    if not all(key in headers for key in group_by_keys):
        print(f"\n--- Skipping Grouped Analysis by {', '.join(group_by_keys)} (required columns not found) ---")
        return

    print(f"\n--- Grouped Analysis by {', '.join(group_by_keys)} ---")
    
    sorted_data = sorted([row for row in data if all(row.get(k) for k in group_by_keys)], key=itemgetter(*group_by_keys))
    
    for key, group in groupby(sorted_data, key=itemgetter(*group_by_keys)):
        group_data = list(group)
        print(f"\nGroup: {key}")
        analyze_dataframe(group_data)

if __name__ == "__main__":
    files_to_analyze = [
        "./period_03/2024_fb_ads_president_scored_anon.csv",
        "./period_03/2024_fb_posts_president_scored_anon.csv",
        "./period_03/2024_tw_posts_president_scored_anon.csv"
    ]
    
    for file_name in files_to_analyze:
        print(f"\n{'='*60}\nAnalyzing file: {file_name}\n{'='*60}")
        
        main_data = load_csv_from_local(file_name)
        
        if main_data:
            print("\n--- Overall Dataset Analysis ---")
            analyze_dataframe(main_data)
            
            analyze_grouped(main_data, ['page_id'])
            analyze_grouped(main_data, ['page_id', 'ad_id'])