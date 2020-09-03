import numpy as np
import pandas as pd

# ------------------------PRE-PROCESSING CONCEPTIONS DATA-------------------------------

df1 = pd.read_stata("data/data_births_20110196.dta")
# df1 = pd.read_stata(r"../data/data_births_20110196.dta")

# Create month of birth variable, -1 = June '07, 0 = July '07, 1 = August '07
df1["birth_month"] = np.nan
# General pattern: month of birth = mesp + (12i) - 7
for year, i in zip(range(2000, 2011), range(-7, 4)):
    df1.loc[(df1["year"] == year), "birth_month"] = df1["mesp"] + (12 * i) - 7

# Create estimated month of conception variable
df1["conception_month"] = df1["birth_month"] - 9

df1.loc[((df1["semanas"] > 43) & (df1["semanas"] != np.nan)), ["conception_month"]] = (
    df1["birth_month"] - 10
)
df1.loc[
    (((df1["semanas"] < 39) & (df1["semanas"] != 0)) | (df1["prem"] == 2)),
    ["conception_month"],
] = (df1["birth_month"] - 8)


df1.rename(columns={"mesp": "calendar_birth_month", "year": "birth_year"}, inplace=True)

# Generate no. of conceptions for each month from month of conception
df1 = df1.groupby(["conception_month"]).size().reset_index(name="number_conceptions")

# Create calendar month of conception variable
df1["conception_year"] = np.nan

# ------------------------------------------DRY--------------------------------------
df1.loc[df1["conception_month"].isin(range(-102, -90)), ["conception_year"]] = 1999
df1.loc[df1["conception_month"].isin(range(-90, -78)), ["conception_year"]] = 2000
df1.loc[df1["conception_month"].isin(range(-78, -66)), ["conception_year"]] = 2001
df1.loc[df1["conception_month"].isin(range(-66, -54)), ["conception_year"]] = 2002
df1.loc[df1["conception_month"].isin(range(-54, -42)), ["conception_year"]] = 2003
df1.loc[df1["conception_month"].isin(range(-42, -30)), ["conception_year"]] = 2004
df1.loc[df1["conception_month"].isin(range(-30, -18)), ["conception_year"]] = 2005
df1.loc[df1["conception_month"].isin(range(-18, -6)), ["conception_year"]] = 2006
df1.loc[df1["conception_month"].isin(range(-6, 6)), ["conception_year"]] = 2007
df1.loc[df1["conception_month"].isin(range(6, 18)), ["conception_year"]] = 2008
df1.loc[df1["conception_month"].isin(range(18, 30)), ["conception_year"]] = 2009
df1.loc[df1["conception_month"].isin(range(30, 42)), ["conception_year"]] = 2010

# Conception yrs go from '99 to '10
df1["calendar_conception_month"] = np.nan
for year, i in zip(range(1999, 2011), range(-8, 4)):
    df1.loc[(df1["conception_year"] == year), "calendar_conception_month"] = (
        df1["conception_month"] - (12 * i) + 7
    )

# Generate 'July' indicator, for some mysterious reason
df1["july"] = 0
df1.loc[df1["calendar_conception_month"] == 7, ["july"]] = 1

# Number of days in each month (of conception)
df1["days_in_conception_month"] = 31
df1.loc[df1["calendar_conception_month"] == 2, ["days_in_conception_month"]] = 28
df1.loc[
    df1["calendar_conception_month"].isin([4, 6, 9, 11]), ["days_in_conception_month"]
] = 30
# Accounting for leap years - 2000, 2004, 2008 -- not done by author
df1.loc[
    (
        (df1["conception_year"].isin([2000, 2004, 2008]))
        & (df1["calendar_conception_month"] == 2)
    ),
    ["days_in_conception_month"],
] = 29


# (Treatment) Indicator variable: 1 for post-policy conception, 0 for pre-policy
df1["post_policy_conception"] = 0
df1.loc[df1["conception_month"] >= 0, ["post_policy_conception"]] = 1

df1["conception_month_sq"] = df1["conception_month"] ** 2
df1["conception_month_cubed"] = df1["conception_month"] ** 3

# Natural log of number_conceptions for each month
df1["ln_number_conceptions"] = np.log(df1["number_conceptions"])


# --------------------------PRE-PROCESSING ABORTIONS DATA----------------------------

df2 = pd.read_stata("data/data_abortions_20110196.dta")
# df2 = pd.read_stata(r"../data/data_abortions_20110196.dta")

# Total no. of abortions in Spain per month (all regions)
df2["number_abortions"] = df2.iloc[:, 2:14].sum(axis=1)

# Create abortion_month variable that takes value 0 in July 2007
df2["abortion_month_counter"] = range(1, 145)
df2["abortion_month"] = df2["abortion_month_counter"] - 103

# Number of days in each month (of abortion)
df2["days_in_abortion_month"] = 31
df2.loc[df2["month"] == 2, ["days_in_abortion_month"]] = 28
df2.loc[df2["month"].isin([4, 6, 9, 11]), ["days_in_abortion_month"]] = 30
# Accounting for leap years - 2000, 2004, 2008
df2.loc[
    ((df2["year"].isin([2000, 2004, 2008])) & (df2["month"] == 2)),
    ["days_in_abortion_month"],
] = 29

# Natural log of number_abortions for each month
df2["ln_number_abortions"] = np.log(df2["number_abortions"])

df2["abortion_month_sq"] = df2["abortion_month"] ** 2
df2["abortion_month_cubed"] = df2["abortion_month"] ** 3

# (Treatment) Indicator variable: 1 for post-policy abortion, 0 for pre-policy
df2["post_policy_abortion"] = 0
df2.loc[df2["abortion_month"] >= 0, ["post_policy_abortion"]] = 1

# Restrict period
df2 = df2.loc[(df2["abortion_month"] > -91) & (df2["abortion_month"] < 30)]

# --------------------------PRE-PROCESSING HBS DATA--------------------------------

# df3 = pd.read_stata(r"../data/data_hbs_20110196.dta")
df3 = pd.read_stata("data/data_hbs_20110196.dta")

# Age of mom and dad
df3.loc[df3["agemom"].isna(), "agemom"] = 0
df3.loc[df3["agedad"].isna(), "agedad"] = 0

# Mom or dad not present
df3 = df3.drop(["nomom", "nodad"], axis=1)
df3["nomom"] = 0
df3["nodad"] = 0
df3.loc[df3["agemom"] == 0, "nomom"] = 1
df3.loc[df3["agedad"] == 0, "nodad"] = 1


# Education of mom and dad
df3["sec1mom"] = 0
df3["sec1dad"] = 0
df3["sec2mom"] = 0
df3["sec2dad"] = 0
df3["unimom"] = 0
df3["unidad"] = 0

df3.loc[df3["educmom"] == 3, "sec1mom"] = 1
df3.loc[df3["educdad"] == 3, "sec1dad"] = 1
df3.loc[(df3["educmom"] > 3) & (df3["educmom"] < 7), "sec2mom"] = 1
df3.loc[(df3["educdad"] > 3) & (df3["educdad"] < 7), "sec2dad"] = 1
df3.loc[(df3["educmom"] == 7) | (df3["educmom"] == 8), "unimom"] = 1
df3.loc[(df3["educdad"] == 7) | (df3["educdad"] == 8), "unidad"] = 1

# Immigrant - indicator var for mom with foreign nationality
df3["immig"] = 0
df3.loc[(df3["nacmom"] == 2) | (df3["nacmom"] == 3), "immig"] = 1

# Mom not married
df3["smom"] = 0
df3.loc[df3["ecivmom"] != 2, "smom"] = 1

# Siblings
df3["sib"] = 0
df3.loc[df3["nmiem2"] > 1, "sib"] = 1

df3["agemom_sq"] = df3["agemom"] ** 2
df3["agemom_cubed"] = df3["agemom"] ** 3

# Daycare
df3["daycare_bin"] = 0
df3.loc[(df3["m_exp12312"] > 0) & (df3["m_exp12312"] != np.nan), "daycare_bin"] = 1

# Logs of dependent variables
df3["ln_gastmon"] = np.nan
df3.loc[df3["gastmon"] != 0, "ln_gastmon"] = np.log(df3["gastmon"])
df3["ln_c_m_exp"] = np.nan
df3.loc[df3["c_m_exp"] != 0, "ln_c_m_exp"] = np.log(df3["c_m_exp"])
df3["ln_dur_exp"] = np.nan
df3.loc[df3["dur_exp"] != 0, "ln_dur_exp"] = np.log(df3["dur_exp"])


# --------------------------PRE-PROCESSING LFS DATA--------------------------------

# df4 = pd.read_stata(r"../data/data_lfs_20110196.dta")
df4 = pd.read_stata("data/data_lfs_20110196.dta")

# Control variables
df4["m2"] = df4["m"] ** 2

# No father present
df4["nodad"] = 0
df4.loc[df4["dadid"] == 0, "nodad"] = 1

# Mother not married
df4["smom"] = 0
df4.loc[df4["eciv"] != 2, "smom"] = 1

# Mother single
df4["single"] = 0
df4.loc[df4["eciv"] == 1, "single"] = 1

# Mother separated or divorced
df4["sepdiv"] = 0
df4.loc[df4["eciv"] == 4, "sepdiv"] = 1

# No partner in the household
df4["nopart"] = 0
df4.loc[df4["partner"] == 0, "nopart"] = 1

# Probability of the mother being in the maternity leave period at the
# time of the interview
df4["pleave"] = 0

df4.loc[
    (
        ((df4["q"] == 1) & (df4["m"] == 2))
        | ((df4["q"] == 2) & (df4["m"] == 5))
        | ((df4["q"] == 3) & (df4["m"] == 8))
        | ((df4["q"] == 4) & (df4["m"] == 11))
    ),
    "pleave",
] = 0.17

df4.loc[
    (
        ((df4["q"] == 1) & (df4["m"] == 3))
        | ((df4["q"] == 2) & (df4["m"] == 6))
        | ((df4["q"] == 3) & (df4["m"] == 9))
        | ((df4["q"] == 4) & (df4["m"] == 12))
    ),
    "pleave",
] = 0.5

df4.loc[
    (
        ((df4["q"] == 1) & (df4["m"] == 4))
        | ((df4["q"] == 2) & (df4["m"] == 7))
        | ((df4["q"] == 3) & (df4["m"] == 10))
        | ((df4["q"] == 4) & (df4["m"] == 13))
    ),
    "pleave",
] = 0.83

df4.loc[
    (
        ((df4["q"] == 1) & (df4["m"] > 4) & (df4["m"] < 9))
        | ((df4["q"] == 2) & (df4["m"] > 7) & (df4["m"] < 12))
        | ((df4["q"] == 3) & (df4["m"] > 10) & (df4["m"] < 15))
        | ((df4["q"] == 4) & (df4["m"] > 13))
    ),
    "pleave",
] = 1

# ----------------------Specifications - Fertility Results----------------------------

data1 = df1.loc[((df1["conception_month"] > -91) & (df1["conception_month"] < 30))]
data2 = df1.loc[((df1["conception_month"] > -31) & (df1["conception_month"] < 30))]
data3 = df1.loc[((df1["conception_month"] > -13) & (df1["conception_month"] < 12))]
data4 = df1.loc[((df1["conception_month"] > -10) & (df1["conception_month"] < 9))]
data5 = df1.loc[((df1["conception_month"] > -4) & (df1["conception_month"] < 3))]
data7 = df1.loc[((df1["conception_month"] > -67) & (df1["conception_month"] < 30))]

data_list_concep = [data1, data2, data3, data4, data5, data1, data7, data2]

regressors_list_concep = [
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + \
    conception_month_cubed * C(post_policy_conception) + days_in_conception_month",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + days_in_conception_month",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + days_in_conception_month",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    days_in_conception_month",
    " ~ C(post_policy_conception) + days_in_conception_month",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + \
    conception_month_cubed * C(post_policy_conception) + days_in_conception_month + \
    C(calendar_conception_month)",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + days_in_conception_month + \
    C(calendar_conception_month)",
    " ~ C(post_policy_conception) + conception_month * C(post_policy_conception) + \
    conception_month_sq * C(post_policy_conception) + days_in_conception_month + \
    C(calendar_conception_month)",
]

dep_var_list_concep = ["ln_number_conceptions"] * 8

regressors_list_abort = [
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + \
    abortion_month_cubed * C(post_policy_abortion) + days_in_abortion_month",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + days_in_abortion_month",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + days_in_abortion_month",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    days_in_abortion_month",
    " ~ C(post_policy_abortion) + days_in_abortion_month",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + \
    abortion_month_cubed * C(post_policy_abortion) + days_in_abortion_month + C(month)",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + days_in_abortion_month + C(month)",
    " ~ C(post_policy_abortion) + abortion_month * C(post_policy_abortion) + \
    abortion_month_sq * C(post_policy_abortion) + days_in_abortion_month + C(month)",
]

data1_abort = df2
data2_abort = df2.loc[df2["abortion_month"] > -31]
data3_abort = df2.loc[((df2["abortion_month"] > -13) & (df2["abortion_month"] < 12))]
data4_abort = df2.loc[((df2["abortion_month"] > -10) & (df2["abortion_month"] < 9))]
data5_abort = df2.loc[((df2["abortion_month"] > -4) & (df2["abortion_month"] < 3))]
data7_abort = df2.loc[df2["abortion_month"] > -67]

data_list_abort = [
    data1_abort,
    data2_abort,
    data3_abort,
    data4_abort,
    data5_abort,
    data1_abort,
    data7_abort,
    data2_abort,
]

dep_var_list_abort = ["ln_number_abortions"] * 8


# ---------------Specifications - Expenditure & Childcare Results---------------------

dep_var_list_te = ["gastmon"] * 7
dep_var_list_tel = ["ln_gastmon"] * 7
dep_var_list_ce = ["c_m_exp"] * 7
dep_var_list_cel = ["ln_c_m_exp"] * 7
dep_var_list_dg = ["dur_exp"] * 7
dep_var_list_dgl = ["ln_dur_exp"] * 7

regressors_list_expen = [
    " ~ C(post) + month + month2 + nomom + agemom + agemom_sq + agemom_cubed + \
    sec1mom + sec2mom + unimom + immig + sib + month * C(post) + month2 * C(post) + \
    C(mes_enc)",
    " ~ C(post) + month + nomom + agemom + agemom_sq + agemom_cubed + sec1mom + \
    sec2mom + unimom + immig + sib + month * C(post) + C(mes_enc)",
    " ~ C(post) + month + nomom + agemom + agemom_sq + agemom_cubed + sec1mom + \
    sec2mom + unimom + immig + sib + month * C(post) + C(mes_enc)",
    " ~ C(post) + nomom + agemom + agemom_sq + agemom_cubed + sec1mom + sec2mom + \
    unimom + immig + sib + C(mes_enc)",
    " ~ C(post)",
    " ~ C(post) + nomom + agemom + agemom_sq + agemom_cubed + sec1mom + sec2mom + \
    unimom + immig + sib + C(mes_enc)",
    " ~ C(post) + month + month2 + nomom + agemom + agemom_sq + agemom_cubed + \
    sec1mom + sec2mom + unimom + immig + sib + month * C(post) + month2 * C(post) + \
    C(mes_enc) + C(n_month)",
]

data1e = df3.loc[((df3["month"] > -10) & (df3["month"] < 9))]
data2e = df3.loc[((df3["month"] > -7) & (df3["month"] < 6))]
data3e = df3.loc[((df3["month"] > -5) & (df3["month"] < 4))]
data4e = df3.loc[((df3["month"] > -4) & (df3["month"] < 3))]
data5e = df3.loc[((df3["month"] > -3) & (df3["month"] < 2))]
data6e = df3.loc[((df3["month"] > -3) & (df3["month"] < 2))]
data7e = df3

data_list_expen = [
    data1e,
    data2e,
    data3e,
    data4e,
    data5e,
    data6e,
    data7e,
]

# Childcare
dep_var_list_pvt = ["m_exp12312"] * 7
dep_var_list_pvtbin = ["daycare_bin"] * 7

# ----------------------Specifications - Labor Supply Results--------------------------

dep_var_list_work = ["work"] * 6
dep_var_list_empl = ["work2"] * 6

regressors_list_ls = [
    " ~ C(post) + m * C(post) + m2 * C(post) + age + age2 + age3 + immig + primary + \
    hsgrad + univ + sib + pleave + C(q)",
    " ~ C(post) + m * C(post) + age + age2 + age3 + immig + primary + hsgrad + univ + \
    sib + pleave + C(q)",
    " ~ C(post) + m * C(post) + age + age2 + age3 + immig + primary + hsgrad + univ + \
    sib + pleave + C(q)",
    " ~ C(post) + age + age2 + age3 + immig + primary + hsgrad + univ + \
    sib + pleave + C(q)",
    " ~ C(post)",
    " ~ C(post) + age + age2 + age3 + immig + primary + hsgrad + univ + \
    sib + pleave + C(q)",
]

data1ls = df4.loc[((df4["m"] > -10) & (df4["m"] < 9))]
data2ls = df4.loc[((df4["m"] > -7) & (df4["m"] < 6))]
data3ls = df4.loc[((df4["m"] > -5) & (df4["m"] < 4))]
data4ls = df4.loc[((df4["m"] > -4) & (df4["m"] < 3))]
data5ls = df4.loc[((df4["m"] > -3) & (df4["m"] < 2))]
data6ls = df4.loc[((df4["m"] > -3) & (df4["m"] < 2))]


data_list_ls = [data1ls, data2ls, data3ls, data4ls, data5ls, data6ls]
