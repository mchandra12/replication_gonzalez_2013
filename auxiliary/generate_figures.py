import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf

from auxiliary.generate_tables import *
from auxiliary.pre_process_datasets import *
from auxiliary.run_regressions import *

# import pandas as pd


def create_fig_hh_expenditure():
    df3_avg = df3.groupby(["month"]).mean()
    # Turn month back  to a column from index
    df3_avg.reset_index(inplace=True)
    plt.figure(figsize=(13, 4))

    plt.subplot(1, 2, 1)

    df_rdd_left = df3_avg.loc[(df3_avg["month"] < 0) & (df3_avg["month"] > -31)]

    df_rdd_right = df3_avg.loc[(df3_avg["month"] > 0) & (df3_avg["month"] < 20)]

    coeffs = np.polyfit(df_rdd_left["month"], df_rdd_left["gastmon"], 2)
    poly = np.poly1d(coeffs)
    predict_x = np.linspace(df_rdd_left["month"].iloc[0], df_rdd_left["month"].iloc[-1])
    predict_y = poly(predict_x)
    plt.plot(
        df_rdd_left["month"], df_rdd_left["gastmon"], "o", predict_x, predict_y, c="g"
    )

    coeffsr = np.polyfit(df_rdd_right["month"], df_rdd_right["gastmon"], 2)
    polyr = np.poly1d(coeffsr)
    predict_xr = np.linspace(
        df_rdd_right["month"].iloc[0], df_rdd_right["month"].iloc[-1]
    )
    predict_yr = poly(predict_xr)
    plt.plot(
        df_rdd_right["month"],
        df_rdd_right["gastmon"],
        "o",
        predict_xr,
        predict_yr,
        c="y",
    )

    plt.ylim(0, 60000)
    plt.xlim(-30, 20)
    plt.xlabel("Month of birth (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.grid(True)
    plt.title("Total expenditure by month of birth")

    plt.subplot(1, 2, 2)
    # df_rdd_left = df3_avg.loc[(df3_avg["month"] < 0) & (df3_avg["month"] > -31)]

    # df_rdd_right = df3_avg.loc[(df3_avg["month"] > 0) & (df3_avg["month"] < 20)]

    coeffs = np.polyfit(df_rdd_left["month"], df_rdd_left["c_m_exp"], 2)
    poly = np.poly1d(coeffs)
    predict_x = np.linspace(df_rdd_left["month"].iloc[0], df_rdd_left["month"].iloc[-1])
    predict_y = poly(predict_x)
    plt.plot(
        df_rdd_left["month"], df_rdd_left["c_m_exp"], "o", predict_x, predict_y, c="g"
    )

    coeffsr = np.polyfit(df_rdd_right["month"], df_rdd_right["c_m_exp"], 3)
    polyr = np.poly1d(coeffsr)
    predict_xr = np.linspace(
        df_rdd_right["month"].iloc[0], df_rdd_right["month"].iloc[-1]
    )
    predict_yr = polyr(predict_xr)
    plt.plot(
        df_rdd_right["month"],
        df_rdd_right["c_m_exp"],
        "o",
        predict_xr,
        predict_yr,
        c="y",
    )

    plt.ylim(0, 10000)
    plt.xlim(-30, 20)
    plt.xlabel("Month of birth (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.grid(True)
    plt.title("Child-related expenditure by month of birth")
    plt.suptitle(
        "Household Expenditure (Annual) by Month of Birth (HBS 2008)",
        verticalalignment="baseline",
        fontsize=14,
    )

    return


def create_daycare_figure():
    df3_avg = df3.groupby(["month"]).mean()
    # Turn month back  to a column from index
    df3_avg.reset_index(inplace=True)
    plt.figure(figsize=(13, 4))

    plt.subplot(1, 2, 1)

    df_rdd_left = df3_avg.loc[(df3_avg["month"] < 0) & (df3_avg["month"] > -31)]

    df_rdd_right = df3_avg.loc[(df3_avg["month"] > 0) & (df3_avg["month"] < 20)]

    res = smf.ols(formula="m_exp12312 ~ month", data=df_rdd_left).fit()
    a1 = res.predict(df_rdd_left)

    res2 = smf.ols(formula="m_exp12312 ~ month", data=df_rdd_right).fit()
    a2 = res2.predict(df_rdd_right)

    plt.scatter(df3_avg["month"], df3_avg["m_exp12312"], edgecolors="r")
    plt.plot(df_rdd_left["month"], a1)
    plt.plot(df_rdd_right["month"], a2)

    plt.ylim(0, 1000)
    plt.xlim(-30, 20)
    plt.xlabel("Month of birth (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.grid(True)
    plt.title("Daycare expenditure by month of birth")

    plt.subplot(1, 2, 2)
    res = smf.ols(formula="daycare_bin ~ month", data=df_rdd_left).fit()
    a1 = res.predict(df_rdd_left)

    res2 = smf.ols(formula="daycare_bin ~ month", data=df_rdd_right).fit()
    a2 = res2.predict(df_rdd_right)

    plt.scatter(df3_avg["month"], df3_avg["daycare_bin"], edgecolors="r")
    plt.plot(df_rdd_left["month"], a1)
    plt.plot(df_rdd_right["month"], a2)

    plt.ylim(0, 0.7)
    plt.xlim(-30, 20)
    plt.xlabel("Month of birth (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.title("Fraction with positive daycare expenditure by month of birth")
    plt.grid(True)

    plt.suptitle(
        "Daycare Expenditure by Month of Birth (HBS 2008)",
        verticalalignment="baseline",
        fontsize=14,
    )

    return


def create_fertility_figure():
    df1_avg = df1.groupby(["conception_month"]).mean()
    # Turn month back  to a column from index
    df1_avg.reset_index(inplace=True)
    df2_avg = df2.groupby(["abortion_month"]).mean()
    # Turn month back  to a column from index
    df2_avg.reset_index(inplace=True)
    plt.figure(figsize=(13, 4))

    plt.subplot(1, 2, 1)

    df_rdd_left = df1_avg.loc[
        (df1_avg["conception_month"] < 0) & (df1_avg["conception_month"] > -31)
    ]

    df_rdd_right = df1_avg.loc[
        (df1_avg["conception_month"] > 0) & (df1_avg["conception_month"] < 20)
    ]

    res = smf.ols(
        formula="number_conceptions ~ conception_month", data=df_rdd_left
    ).fit()
    a1 = res.predict(df_rdd_left)

    res2 = smf.ols(
        formula="number_conceptions ~ conception_month", data=df_rdd_right
    ).fit()
    a2 = res2.predict(df_rdd_right)

    plt.scatter(
        df1_avg["conception_month"], df1_avg["number_conceptions"], edgecolors="r"
    )
    plt.plot(df_rdd_left["conception_month"], a1)
    plt.plot(df_rdd_right["conception_month"], a2)

    plt.ylim(30000, 50000)
    plt.xlim(-15, 15)
    plt.xlabel("Month of conception (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.grid(True)
    plt.title("Number of conceptions by month")

    plt.subplot(1, 2, 2)
    df_rdd_left = df2_avg.loc[
        (df2_avg["abortion_month"] < 0) & (df2_avg["abortion_month"] > -31)
    ]

    df_rdd_right = df2_avg.loc[
        (df2_avg["abortion_month"] > 0) & (df2_avg["abortion_month"] < 20)
    ]

    res = smf.ols(
        formula="ln_number_abortions ~ abortion_month", data=df_rdd_left
    ).fit()
    a1 = res.predict(df_rdd_left)

    res2 = smf.ols(
        formula="ln_number_abortions ~ abortion_month", data=df_rdd_right
    ).fit()
    a2 = res2.predict(df_rdd_right)

    plt.scatter(
        df2_avg["abortion_month"], df2_avg["ln_number_abortions"], edgecolors="r"
    )
    plt.plot(df_rdd_left["abortion_month"], a1)
    plt.plot(df_rdd_right["abortion_month"], a2)

    # plt.ylim(10000, 22000)
    plt.xlim(-30, 20)
    plt.xlabel("Month of abortion (0=July 2007)")
    plt.axvline(x=0, color="k")
    plt.title("Number of abortions by month")
    plt.grid(True)

    plt.suptitle(
        "Fertility Effect: Conceptions and Abortions by month",
        verticalalignment="baseline",
        fontsize=14,
    )

    return
