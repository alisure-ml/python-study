# http://pandas.pydata.org/pandas-docs/stable/10min.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Object Creation
def object_creation():

    # Series by list
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df)

    # DataFrame by dict -- Note: column names become attributes
    df2 = pd.DataFrame({
        "A": 1.,
        "B": pd.Timestamp("20170518"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    })
    print(df2)
    print(df2.dtypes)

    pass


# Viewing Data
def viewing_data():
    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    # See the top & bottom rows of the frame
    print(df.head(n=2))
    print(df.tail(n=2))
    # Display the index, columns, and the underlying numpy data
    print(df.index)
    print(df.columns)
    print(df.values)
    # Describe shows a quick statistic summary of your data
    print(df.describe())
    # Transposing your data
    print(df.T)
    # Sorting by an axis
    print(df.sort_index(axis=0, ascending=True))
    print(df.sort_index(axis=0, ascending=False))
    print(df.sort_index(axis=1, ascending=True))
    print(df.sort_index(axis=1, ascending=False))
    # Sorting by values
    print(df.sort_values(by="B"))
    print(df.sort_values(by=["A", "B"]))

    pass


# Selection Getting
def selection_getting():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Selecting a single column, which yields a Series, equivalent to df.A
    print(df["A"])
    print(df.A)

    # Selecting via [], which slices the rows.
    print(df[0: 3])
    print(df["2017-05-20":"2017-05-22"])

    pass


# Selection by Label
def selection_by_label():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # For getting a cross section using a label
    print(df.loc[dates[0]])

    # Selecting on a multi-axis by label
    print(df.loc[:, ["A", "B"]])

    # Showing label slicing, both endpoints are included
    print(df.loc[dates[1]:dates[3], ["A", "B"]])

    # Reduction in the dimensions of the returned object
    print(df.loc[dates[2], ["C", "B"]])

    # For getting a scalar value
    print(df.loc[dates[2], "C"])

    # For getting fast access to a scalar (equiv to the prior method)
    print(df.at[dates[2], "B"])

    pass


# Selection by Position
def selection_by_position():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Select via the position of the passed integers
    print(df.iloc[3])

    # By integer slices, acting similar to numpy/python
    print(df.iloc[2: 4, 1: 3])

    # By lists of integer position locations, similar to the numpy/python style
    print(df.iloc[[1, 3, 5], 0: 3])
    print(df.iloc[[1, 3, 5], [0, 2, 3]])
    print(df.iloc[[1, 3, 5], :])

    # For getting a value explicitly
    print(df.iloc[1, 1])
    print(df.iat[1, 1])

    pass


# Selection by Boolean Indexing
def selection_by_boolean_indexing():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Using a single column’s values to select data.
    print(df.A > 0)
    print(df[df.A > 0])
    # Selecting values from a DataFrame where a boolean condition is met.
    print(df[df > 0])

    # Using the isin() method for filtering
    df2 = df.copy()
    df2["E"] = ["1", "1", "2", "3", "3", "4"]
    print(df2)
    print(df2[df2["E"].isin(["1", "2"])])

    # Boolean list
    boolean = [True, False, False, True, True, True]
    print(df2[boolean])

    def sb(x):
        booleans = []
        for i in x.iloc[:, 1]:
            if i > 0:
                booleans.append(True)
            else:
                booleans.append(False)
        print(booleans)
        return booleans
    print(df2[lambda x: sb(x)])

    pass


# Selection by Setting
def selection_by_setting():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Setting a new column automatically aligns the data by the indexes
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
    print(s1)
    df["E"] = s1
    print(df)
    df["D"] = s1
    print(df)

    # Setting values by label
    df.at[dates[2], "B"] = 0
    print(df)

    # Setting values by position
    df.iat[3, 1] = 0
    print(df)

    # Setting by assigning with a numpy array
    df.loc[:, "C"] = np.array([5] * len(df))
    print(df)

    pass


# Missing Data
def missing_data():
    """
    pandas primarily uses the value np.nan to represent missing data.
    It is by default not included in computations.
    :return: 
    """

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Reindexing allows you to change/add/delete the index on a specified axis.
    df1 = df.reindex(index=dates[1: 5], columns=list(df.columns) + ["E"])
    print(df1)
    df1.loc[dates[2]: dates[3], "E"] = 1
    print(df1)

    # To drop any rows that have missing data.
    # Reindex-based selection methods
    print(df1.dropna(how="any"))

    # Filling missing data
    print(df1.fillna(value=1000000))

    # To get the boolean mask where values are nan
    print(df1.isnull())

    pass


# Operations Stats
def operations_stats():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    print(df)
    print(df.mean())
    print(df.mean(1))

    # Operating with objects that have different dimensionality and need alignment.
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
    print(s)
    print(df.sub(s, axis="index"))

    pass


# Operations Apply
def operations_apply():

    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    print(df)
    # Applying functions to the data
    # cumsum : the cumulative sum of the elements（累积和）
    print(df.apply(np.cumsum))
    print(df.apply(lambda x: x.max() - x.min()))

    pass


# Operations Histogramming(直方图化)
def operations_histogramming():

    s = pd.Series(np.random.randint(0, 7, size=100))
    print(s)
    print(s.value_counts())

    pass


# Operations String Methods
def operations_string():

    s = pd.Series(["A", "B", "C", "AbC", np.nan])
    print(s.str.lower())

    pass


# Merge
def merge():
    """
    concat
    merge
    append
    :return: 
    """
    """
    JOIN: 如果表中有至少一个匹配，则返回行
    LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
    RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
    FULL JOIN: 只要其中一个表中存在匹配，就返回行
    """
    """
    how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
    """
    # Concatenating pandas objects together with concat()
    df = pd.DataFrame(np.random.randn(10, 4))
    pieces = [df[: 1], df[3: 5], df[8: 9]]
    print(pd.concat(pieces))
    pieces = [df.iloc[:, 0], df.iloc[:, 2]]
    print(pd.concat(pieces, axis=1))

    # Join : SQL style merges.
    left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
    right = pd.DataFrame({"key": ["foo", "foo"], "rval": [5, 2]})
    print(pd.merge(left=left, right=right, on="key"))
    print(pd.merge(left=right, right=left, on="key"))
    print(pd.merge(left=left, right=right, left_on="lval", right_on="rval"))

    # Append : Append rows to a dataframe
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    print(df.append(df.iloc[3: 6], ignore_index=True))

    pass


# Grouping
def grouping():
    """
    By “group by” we are referring to a process involving 
    one or more of the following steps:
        1.Splitting the data into groups based on some criteria
        2.Applying a function to each group independently
        3.Combining the results into a data structure
    :return: 
    """
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)
                       })
    print(df)

    # Grouping and then applying a function sum to the resulting groups.
    print(df.groupby("A"))
    print(df.groupby("A").sum())

    # Grouping by multiple columns forms a hierarchical index(分级索引),
    # which we then apply the function.
    print(df.groupby(["A", "B"]).sum())

    pass


# Reshaping
def reshaping():
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
    print(tuples)

    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    print(index)

    df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=['A', 'B', "C", "D"])
    print(df)
    # The stack() method “compresses” a level in the DataFrame’s columns.
    stacked = df.stack()
    print(stacked)
    # With a “stacked” DataFrame or Series (having a MultiIndex as the index),
    # the inverse operation of stack() is unstack(),
    # which by default unstacks the last level:
    print(stacked.unstack())
    print(stacked.unstack(0))
    print(stacked.unstack(1))

    # Pivot Tables
    print(pd.pivot_table(df, values="A", index="first", columns="second"))
    print(pd.pivot_table(df, values=["A", "B"], index="first", columns="second"))
    print(pd.pivot_table(df, values=["A", "B"], index=["first", "second"], columns="C"))

    pass


# Time Series
def time_series():

    # http://pandas.pydata.org/pandas-docs/stable/10min.html#time-series

    pass


# Categoricals(类别)
def categoricals():
    df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
    })
    print(df)

    # Convert the raw grades to a categorical data type.
    df["grade"] = df["raw_grade"].astype("category")
    print(df)
    print(df["grade"])

    # Rename the categories to more meaningful names
    df["grade"].cat.categories = ["good", "common", "bad"]
    print(df["grade"])
    print(df)

    # Sorting is per order in the categories
    print(df.sort_values(by="grade"))

    # Grouping by a categorical column shows also empty categories.
    print(df.groupby("grade").size())

    pass


# Plotting
def plotting():
    """
    # The plot method on Series and DataFrame is just a simple wrapper around plt.plot()
    :return: 
    """

    # Series
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()  # 累积和
    ts.plot()
    plt.show()

    # DataFrame
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])
    df = df.cumsum()  # 累积和
    df.plot()
    plt.legend(loc="best")
    plt.show()

    pass


# Getting Data In/Out
def data_in_out():

    path = "data/study_pandas/"
    file_csv = path + "test.csv"
    file_excel = path + "test.xlsx"

    df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
    print(df)

    # Writing to a csv file
    df.to_csv(file_csv, index=False)
    # Reading from a csv file
    df2 = pd.read_csv(file_csv)
    print(df2)

    # Writing to an excel f ile
    df.to_excel(file_excel, sheet_name="A")
    # Reading from an excel file
    df4 = pd.read_excel(file_excel, sheetname="A",index_col=None, na_values=["NA"])
    print(df4)

    pass


# very important
def reset_index():
    """
    http://blog.csdn.net/qq_28219759/article/details/49083693
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html?highlight=reset_index
    :return: 
    """
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)
                       })
    print(df)
    df = df.groupby("A").count()
    print(df)
    df = df.reset_index()
    print(df)
    print(df["A"])
    print(df["B"])

    pass

if __name__ == "__main__":

    # object_creation()
    # viewing_data()
    # selection_getting()
    # selection_by_label()
    # selection_by_position()
    # selection_by_boolean_indexing()
    # selection_by_setting()
    # missing_data()
    # operations_stats()
    # operations_apply()
    # operations_histogramming()
    # operations_string()
    # merge()
    # grouping()
    # reshaping()
    # time_series()
    # categoricals()
    # plotting()
    # data_in_out()
    reset_index()

    pass
