import pandas as pd

def q1_import_and_version():
    import pandas as pd
    return pd.__version__

def q1_2_create_df():
    df = pd.DataFrame({
        'Name': ['Alice','Bob','Charlie'],
        'Age': [25,30,35],
        'City': ['New York','Los Angeles','Chicago']
    })
    return df

def q2_series():
    s1 = pd.Series([100,200,300,400,500])
    return s1

def q2_2_access(s):
    return s.iloc[1], s.iloc[3]  

def q2_3_series_ops():
    s1 = pd.Series([100,200,300,400,500])
    s2 = pd.Series([10,20,30,40,50])
    return s1 + s2

def q3_column_access_and_add():
    df = q1_2_create_df()
    names_cities = df[['Name','City']]
    df['Salary'] = [50000,60000,70000]
    avg_age = df['Age'].mean()
    sum_salary = df['Salary'].sum()
    return names_cities, df, avg_age, sum_salary

def q4_filter_and_indexing():
    _, df, _, _ = q3_column_access_and_add()
    filtered = df[df['Age'] > 28]
    set_idx = df.set_index('Name')
    reset = set_idx.reset_index()
    return filtered, set_idx, reset

def q5_csv_read_filter():
    
    df = pd.DataFrame({
        'Name': ['John','Jane','Emily'],
        'Department': ['Sales','Marketing','HR'],
        'Salary': [50000,60000,55000]
    })
    filtered = df[df['Salary'] > 55000]
    return df, filtered[['Name','Department']]

def q6_grouping_and_aggregation():
    df, _ = q5_csv_read_filter()
    avg_by_dept = df.groupby('Department')['Salary'].mean()
    minmax = df.groupby('Department')['Salary'].agg(['min','max'])
    return avg_by_dept, minmax

def q7_merge_dfs():
    df1 = pd.DataFrame({'Name':['John','Jane','Emily'],
                        'Department':['Sales','Marketing','HR']})
    df2 = pd.DataFrame({'Name':['John','Jane','Emily'],
                        'Experience (Years)': [5,7,3]})
    merged = pd.merge(df1, df2, on='Name')
    return merged

def q8_sorting():
    merged = q7_merge_dfs()
    sorted_df = merged.sort_values(by='Experience (Years)', ascending=False)
    return sorted_df

if __name__ == "__main__":
    print("Pandas version:", q1_import_and_version())
    print("Q1.2 DF:\n", q1_2_create_df())
    s = q2_series()
    print("Series:", s)
    print("Access:", q2_2_access(s))
    print("Series add:", q2_3_series_ops())
    print("Q3 names_cities and updated DF:\n", q3_column_access_and_add())
    print("Q4:", q4_filter_and_indexing()[0])
    print("Q5 example CSV df:\n", q5_csv_read_filter()[0])
    print("Q6 group avg:\n", q6_grouping_and_aggregation()[0])
    print("Q7 merged:\n", q7_merge_dfs())
    print("Q8 sorted:\n", q8_sorting())
