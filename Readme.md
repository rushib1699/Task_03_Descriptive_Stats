Here is the updated `README.md` file.

-----

# Task\_03\_Descriptive\_Stats


## Required Scripts

Three separate Python scripts have been written to perform the analysis, one for each required approach[cite: 23].

  * `pure_python_stats.py`
  * `pandas_stats.py`
  * `polars_stats.py`

Each script performs the following analysis[cite: 24]:

  * **Overall Dataset:**
      * Count, Mean, Min/Max, and Standard Deviation for numeric columns.
      * Unique value counts and most frequent values for non-numeric columns.
  * **Grouped Analysis:**
      * The same analysis is performed after aggregating data by `page_id`.
      * The analysis is repeated after aggregating by both `page_id` and `ad_id`.

## Instructions to Run the Code

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Task_03_Descriptive_Stats.git
    cd Task_03_Descriptive_Stats
    ```

2.  **Place Data Files:**
    Place the three required CSV files into the cloned directory. Do not include the dataset files in your Git commits[cite: 30].

3.  **Install Libraries:**
    The scripts require `pandas`, `polars`, `matplotlib`, and `seaborn`.

    ```bash
    pip install pandas polars matplotlib seaborn
    ```

4.  **Run the Analysis Scripts:**
    Execute any of the analysis scripts from your terminal. Each script will loop through the three files and print the analysis for each one.

    ```bash
    python pure_python_stats.py
    python pandas_stats.py
    python polars_stats.py
    ```

5.  **Run the Bonus Visualization Script:**
    This script loads all three files to create comparative plots.

    ```bash
    python bonus_visualizations.py
    ```

## Analysis and Comparative Findings

This section addresses the research questions posed in the task description.

  * **Challenge of Identical Results**:
    Producing identical numerical results was a moderate challenge[cite: 10]. While basic counts and min/max values were straightforward, discrepancies arose in floating-point precision for mean and standard deviation. The pure Python implementation required careful handling of data types and missing values to align with the more robust, automated methods of Pandas and Polars. The primary challenge was ensuring the logic for including/excluding null values was consistent across all three methods.

  * **Approach Comparison & Recommendation**:

      * **Pure Python:** This approach is powerful for understanding the underlying mechanics of statistical calculations but is verbose, error-prone, and significantly less performant. It is not ideal for rapid, complex analysis.
      * **Pandas & Polars:** Both libraries were far easier and more performant than the pure Python approach[cite: 11]. Pandas' `describe()` and `groupby()` methods are intuitive and powerful. Polars offers similar functionality with a syntax that can be even faster for very large datasets.
      * **Recommendation for a Junior Analyst:** I would recommend **Pandas** to a junior data analyst[cite: 11]. Its widespread adoption, extensive documentation, and intuitive API make it an excellent tool for learning data analysis fundamentals. The vast number of online resources and community support is invaluable for a beginner.

  * **AI Coding Assistant Insights**:
    Coding AI such as ChatGPT can be extremely helpful in producing template code to jump-start each approach[cite: 12]. When asked to produce descriptive statistics for a dataset, these tools almost universally recommend using the **Pandas** library as the default approach[cite: 13]. I agree with this recommendation because Pandas provides a "golden path" for most data analysis tasks in Python[cite: 14]. It strikes the perfect balance between ease of use, functionality, and performance for the vast majority of use cases a data analyst will encounter[cite: 14].

  * **Data Narrative**:
    The dataset presents a compelling narrative about the scale and concentration of social media advertising in the political sphere[cite: 27]. Analysis reveals that a small number of pages are responsible for a very large portion of the total ad spend. The visualizations highlight which candidates or political action committees have the most amplified voices online. This spending does not always correlate directly with organic engagement (likes, shares), suggesting different strategies for paid versus organic outreach[cite: 28].
