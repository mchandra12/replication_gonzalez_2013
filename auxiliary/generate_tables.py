# import numpy as np
import pandas as pd

from auxiliary.pre_process_datasets import *
from auxiliary.run_regressions import *

# from pre_process_datasets import *
# from run_regressions import *
# import statsmodels.formula.api as smf
# import matplotlib.pyplot as plt


def generate_fertility_results_table():
    index = pd.MultiIndex.from_product(
        [["Conceptions", "Abortions",], ["Coefficient", "SE", "p-value",]]
    )

    columns = [
        "RDD 10 Years (1)",
        "RDD 5 Years (2)",
        "RDD 12 Months (3)",
        "RDD 9 Months (4)",
        "RDD 3 Months (5)",
        "DID 10 Years (6)",
        "DID 7 Years (7)",
        "DID 5 Years (8)",
    ]
    table = pd.DataFrame(index=index, columns=columns)

    rows = pd.MultiIndex.from_product(
        [
            ["Specification Details"],
            [
                "Years Included",
                "N",
                "Linear Trend in m",
                "Quadratic Trend in m",
                "Cubic Trend in m",
                "No. of days of month",
                "Calendar Month Dummies",
            ],
        ]
    )
    table1 = pd.DataFrame(index=rows, columns=columns)
    tab = pd.concat([table, table1])

    a = global_rdd_regression(
        data_list_concep, dep_var_list_concep, regressors_list_concep
    )
    tab.loc["Conceptions", "Coefficient"] = a[0]
    tab.loc["Conceptions", "SE"] = a[1]
    tab.loc["Conceptions", "p-value"] = a[2]

    b = global_rdd_regression(
        data_list_abort, dep_var_list_abort, regressors_list_abort
    )
    tab.loc["Abortions", "Coefficient"] = b[0]
    tab.loc["Abortions", "SE"] = b[1]
    tab.loc["Abortions", "p-value"] = b[2]

    tab.loc["Specification Details", "Years Included"] = [
        "2000-09",
        "2005-09",
        "2006-08",
        "2006-08",
        "2007",
        "2000-09",
        "2003-09",
        "2005-09",
    ]
    tab.loc["Specification Details", "N"] = [
        120,
        60,
        24,
        18,
        6,
        120,
        96,
        60,
    ]
    tab.loc["Specification Details", "Linear Trend in m"] = [
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Quadratic Trend in m"] = [
        "Y",
        "Y",
        "Y",
        "N",
        "N",
        "Y",
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Cubic Trend in m"] = [
        "Y",
        "N",
        "N",
        "N",
        "N",
        "Y",
        "N",
        "N",
    ]
    tab.loc["Specification Details", "No. of days of month"] = [
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Calendar Month Dummies"] = [
        "N",
        "N",
        "N",
        "N",
        "N",
        "Y",
        "Y",
        "Y",
    ]

    return tab
    # return fertility_results_table.round(2)


generate_fertility_results_table()

# ------------------------------Expenditure_results_table-----------------------------


def generate_expenditure_results_table():
    index = pd.MultiIndex.from_product(
        [
            [
                "Total Expenditure",
                "Total Expenditure (log)",
                "Child-related Expenditure",
                "Child-related Expenditure (log)",
                "Durable goods Expenditure",
                "Durable goods Expenditure (log)",
            ],
            ["Coefficient", "SE", "p-value",],
        ]
    )

    columns = [
        "RDD 9m (1)",
        "RDD 6m (2)",
        "RDD 4m (3)",
        "RDD 3m (4)",
        "RDD 2m (5)",
        "RDD 2m (6)",
        "DID (7)",
    ]
    table = pd.DataFrame(index=index, columns=columns)

    rows = pd.MultiIndex.from_product(
        [
            ["Specification Details"],
            [
                "Linear Trend in m",
                "Quadratic Trend in m",
                "Calendar Month of birth dummies",
                "Controls",
                "Number of months",
            ],
        ]
    )
    table1 = pd.DataFrame(index=rows, columns=columns)
    tab = pd.concat([table, table1])

    row1 = global_rdd_regression(
        data_list_expen, dep_var_list_te, regressors_list_expen
    )
    tab.loc["Total Expenditure", "Coefficient"] = row1[0]
    tab.loc["Total Expenditure", "SE"] = row1[1]
    tab.loc["Total Expenditure", "p-value"] = row1[2]

    row2 = global_rdd_regression(
        data_list_expen, dep_var_list_tel, regressors_list_expen
    )
    tab.loc["Total Expenditure (log)", "Coefficient"] = row2[0]
    tab.loc["Total Expenditure (log)", "SE"] = row2[1]
    tab.loc["Total Expenditure (log)", "p-value"] = row2[2]

    row3 = global_rdd_regression(
        data_list_expen, dep_var_list_ce, regressors_list_expen
    )
    tab.loc["Child-related Expenditure", "Coefficient"] = row3[0]
    tab.loc["Child-related Expenditure", "SE"] = row3[1]
    tab.loc["Child-related Expenditure", "p-value"] = row3[2]

    row4 = global_rdd_regression(
        data_list_expen, dep_var_list_cel, regressors_list_expen
    )
    tab.loc["Child-related Expenditure (log)", "Coefficient"] = row4[0]
    tab.loc["Child-related Expenditure (log)", "SE"] = row4[1]
    tab.loc["Child-related Expenditure (log)", "p-value"] = row4[2]

    row5 = global_rdd_regression(
        data_list_expen, dep_var_list_dg, regressors_list_expen
    )
    tab.loc["Durable goods Expenditure", "Coefficient"] = row5[0]
    tab.loc["Durable goods Expenditure", "SE"] = row5[1]
    tab.loc["Durable goods Expenditure", "p-value"] = row5[2]

    row6 = global_rdd_regression(
        data_list_expen, dep_var_list_dgl, regressors_list_expen
    )
    tab.loc["Durable goods Expenditure (log)", "Coefficient"] = row6[0]
    tab.loc["Durable goods Expenditure (log)", "SE"] = row6[1]
    tab.loc["Durable goods Expenditure (log)", "p-value"] = row6[2]

    tab.loc["Specification Details", "Linear Trend in m"] = [
        "Y",
        "Y",
        "Y",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Quadratic Trend in m"] = [
        "Y",
        "N",
        "N",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Calendar Month of birth dummies"] = [
        "N",
        "N",
        "N",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Controls"] = [
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Number of months"] = [
        "18",
        "12",
        "8",
        "6",
        "4",
        "4",
        "48",
    ]

    return tab


generate_expenditure_results_table()


def generate_childcare_results_table():
    index = pd.MultiIndex.from_product(
        [
            ["Private day care", "Private day care (binary)",],
            ["Coefficient", "SE", "p-value",],
        ]
    )

    columns = [
        "RDD 9m (1)",
        "RDD 6m (2)",
        "RDD 4m (3)",
        "RDD 3m (4)",
        "RDD 2m (5)",
        "RDD 2m (6)",
        "DID (7)",
    ]
    table = pd.DataFrame(index=index, columns=columns)

    rows = pd.MultiIndex.from_product(
        [
            ["Specification Details"],
            [
                "Linear Trend in m",
                "Quadratic Trend in m",
                "Calendar Month of birth dummies",
                "Controls",
                "Number of months",
            ],
        ]
    )
    table1 = pd.DataFrame(index=rows, columns=columns)
    tab = pd.concat([table, table1])

    tab.loc["Specification Details", "Linear Trend in m"] = [
        "Y",
        "Y",
        "Y",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Quadratic Trend in m"] = [
        "Y",
        "N",
        "N",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Calendar Month of birth dummies"] = [
        "N",
        "N",
        "N",
        "N",
        "N",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Controls"] = [
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Number of months"] = [
        "18",
        "12",
        "8",
        "6",
        "4",
        "4",
        "48",
    ]

    row1 = global_rdd_regression(
        data_list_expen, dep_var_list_pvt, regressors_list_expen
    )
    tab.loc["Private day care", "Coefficient"] = row1[0]
    tab.loc["Private day care", "SE"] = row1[1]
    tab.loc["Private day care", "p-value"] = row1[2]

    row2 = global_rdd_regression(
        data_list_expen, dep_var_list_pvtbin, regressors_list_expen
    )
    tab.loc["Private day care (binary)", "Coefficient"] = row2[0]
    tab.loc["Private day care (binary)", "SE"] = row2[1]
    tab.loc["Private day care (binary)", "p-value"] = row2[2]

    return tab


generate_childcare_results_table()


def generate_labor_supply_results_table():
    index = pd.MultiIndex.from_product(
        [["Working Last Week", "Employed",], ["Coefficient", "SE", "p-value",],]
    )

    columns = [
        "RDD 9m (1)",
        "RDD 6m (2)",
        "RDD 4m (3)",
        "RDD 3m (4)",
        "RDD 2m (5)",
        "RDD 2m (6)",
    ]
    table = pd.DataFrame(index=index, columns=columns)

    rows = pd.MultiIndex.from_product(
        [
            ["Specification Details"],
            [
                "Linear Trend in m",
                "Quadratic Trend in m",
                "Calendar Month of birth dummies",
                "Controls",
                "Number of months",
            ],
        ]
    )
    table1 = pd.DataFrame(index=rows, columns=columns)
    tab = pd.concat([table, table1])

    tab.loc["Specification Details", "Linear Trend in m"] = [
        "Y",
        "Y",
        "Y",
        "N",
        "N",
        "N",
    ]
    tab.loc["Specification Details", "Quadratic Trend in m"] = [
        "Y",
        "N",
        "N",
        "N",
        "N",
        "N",
    ]
    tab.loc["Specification Details", "Calendar Month of birth dummies"] = [
        "N",
        "N",
        "N",
        "N",
        "N",
        "N",
    ]
    tab.loc["Specification Details", "Controls"] = [
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
    ]
    tab.loc["Specification Details", "Number of months"] = [
        "18",
        "12",
        "8",
        "6",
        "4",
        "4",
    ]

    row1 = global_rdd_regression(data_list_ls, dep_var_list_work, regressors_list_ls)
    tab.loc["Working Last Week", "Coefficient"] = row1[0]
    tab.loc["Working Last Week", "SE"] = row1[1]
    tab.loc["Working Last Week", "p-value"] = row1[2]

    row2 = global_rdd_regression(data_list_ls, dep_var_list_empl, regressors_list_ls)
    tab.loc["Employed", "Coefficient"] = row2[0]
    tab.loc["Employed", "SE"] = row2[1]
    tab.loc["Employed", "p-value"] = row2[2]

    return tab


generate_labor_supply_results_table()

# ---------------------------------------------------------------------
regressors_child_exten = [
    " ~ C(post) + month + month2 + nomom + agemom + agemom_sq + agemom_cubed + \
    sec1mom + sec2mom + unimom + immig + sib + \
    C(mes_enc) + C(n_month)",
    " ~ C(post) + month + month2 + nomom + agemom + agemom_sq + agemom_cubed + \
    sec1mom + sec2mom + unimom + immig + sib + month * C(post) + month2 * C(post) + \
    C(mes_enc) + C(n_month)",
]
dep_var_child_exten1 = ["m_exp12312"] * 2
dep_var_child_exten2 = ["daycare_bin"] * 2
data_child_exten = [data7e, data7e]


def generate_childcare_extension_table():
    index = pd.MultiIndex.from_product(
        [
            ["Private day care", "Private day care (binary)",],
            ["Coefficient", "SE", "p-value",],
        ]
    )

    columns = ["DID (1)", "DID (2)"]
    table = pd.DataFrame(index=index, columns=columns)

    rows = pd.MultiIndex.from_product(
        [
            ["Specification Details"],
            [
                "Interacting Running Variable (months) with Treatment indicator",
                "Linear Trend in m",
                "Quadratic Trend in m",
                "Calendar Month of birth dummies",
                "Controls",
                "Number of months",
            ],
        ]
    )
    table1 = pd.DataFrame(index=rows, columns=columns)
    tab = pd.concat([table, table1])

    tab.loc[
        "Specification Details",
        "Interacting Running Variable (months) with Treatment indicator",
    ] = [
        "N",
        "Y",
    ]

    tab.loc["Specification Details", "Linear Trend in m"] = [
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Quadratic Trend in m"] = [
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Calendar Month of birth dummies"] = [
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Controls"] = [
        "Y",
        "Y",
    ]
    tab.loc["Specification Details", "Number of months"] = [
        "48",
        "48",
    ]

    row1 = global_rdd_regression(
        data_child_exten, dep_var_child_exten1, regressors_child_exten
    )
    tab.loc["Private day care", "Coefficient"] = row1[0]
    tab.loc["Private day care", "SE"] = row1[1]
    tab.loc["Private day care", "p-value"] = row1[2]

    row2 = global_rdd_regression(
        data_child_exten, dep_var_child_exten2, regressors_child_exten
    )
    tab.loc["Private day care (binary)", "Coefficient"] = row2[0]
    tab.loc["Private day care (binary)", "SE"] = row2[1]
    tab.loc["Private day care (binary)", "p-value"] = row2[2]

    return tab


# --------------------------------------------------------------------------
def create_df1_ds():
    df1_ds = (
        df1.loc[
            (df1["conception_month"] > -91) & (df1["conception_month"] < 30),
            ["number_conceptions", "post_policy_conception", "conception_month"],
        ]
        .describe()
        .loc[["mean", "std", "50%"]]
        .round(3)
    )
    return df1_ds


def create_df2_ds():
    df2_ds = (
        df2[["number_abortions", "post_policy_abortion", "abortion_month"]]
        .describe()
        .loc[["mean", "std", "50%"]]
        .round(3)
    )
    return df2_ds


def create_df3_ds():
    df3_ds = (
        df3.loc[
            (df3["month"] > -10) & (df3["month"] < 9),
            [
                "gastmon",
                "c_m_exp",
                "dur_exp",
                "m_exp12312",
                "post",
                "month",
                "agemom",
                "sec1mom",
                "sec2mom",
                "unimom",
                "immig",
                "sib",
            ],
        ]
        .describe()
        .loc[["mean", "std", "50%"]]
        .round(3)
    )
    df3_ds = df3_ds.rename(
        columns={
            "gastmon": "Total Expenditure",
            "c_m_exp": "Child Related Expenditure",
            "dur_exp": "Durable expenditure",
            "m_exp12312": "Day care expenditure",
            "post": "Post-June 2007 dummy",
            "month": "Month of birth",
            "agemom": "Age of mother",
            "sec1mom": "Mother some secondary",
            "sec2mom": "Mother High School Graduate",
            "unimom": "Mother College Graduate",
            "immig": "Mother Immigrant",
            "sib": "Not first born",
        }
    )
    return df3_ds


def create_df4_ds():
    df4_ds = (
        df4.loc[
            (df4["m"] > -10) & (df4["m"] < 9),
            [
                "work",
                "work2",
                "post",
                "m",
                "age",
                "primary",
                "hsgrad",
                "univ",
                "immig",
                "sib",
            ],
        ]
        .describe()
        .loc[["mean", "std", "50%"]]
        .round(3)
    )
    df4_ds = df4_ds.rename(
        columns={
            "work": "Worked Last week",
            "work2": "Currently Employed",
            "post": "Post-June 2007 dummy",
            "m": "Month of birth",
            "age": "Age of mother",
            "primary": "Mother some secondary",
            "hsgrad": "Mother High School Graduate",
            "univ": "Mother College Graduate",
            "immig": "Mother Immigrant",
            "sib": "Not first born",
        }
    )
    return df4_ds
