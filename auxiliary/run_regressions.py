import statsmodels.formula.api as smf


# def global_rdd_regression(data_list, dep_var_list, regressors_list):
#     """
#     For each combination of data, dep_var and regressors, compute the corresponding c,
#     se and pval. Add each of the 3 to corres list. These lists can then easily be added as
#     rows into the table of results. All 3 lists must have equal lengths.
#
#     """
#     coeff = []
#     se = []
#     pvalue = []
#     for data, dep_var, regressors in zip(data_list, dep_var_list, regressors_list):
#         rdd = smf.ols(formula=dep_var + regressors, data=data).fit(cov_type="HC1")
#         c = rdd.params[1]
#         s = rdd.bse[1]
#         p = rdd.pvalues[1]
#         coeff.append(c)
#         se.append(s)
#         pvalue.append(p)
#
#     return coeff, se, pvalue


def global_rdd_regression(
    data_list, dep_var_list, regressors_list, cov_type="HC1", cov_kwds=None
):
    """
    For each combination of data, dep_var and regressors, compute the corresponding c,
    se and pval. Add each of the 3 to corres list. These lists can then easily be added as
    rows into the table of results. All 3 lists must have equal lengths.

    """
    coeff = []
    se = []
    pvalue = []
    for data, dep_var, regressors in zip(data_list, dep_var_list, regressors_list):
        rdd = smf.ols(formula=dep_var + regressors, data=data).fit(
            cov_type=cov_type, cov_kwds=cov_kwds
        )
        c = rdd.params[1]
        s = rdd.bse[1]
        p = rdd.pvalues[1]
        coeff.append(c)
        se.append(s)
        pvalue.append(p)

    return coeff, se, pvalue


# c, s, p = [rdd.params[1], rdd.bse[1], rdd.pvalues[1]]
