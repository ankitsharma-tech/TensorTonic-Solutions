from scipy import stats

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, alpha):
    """
    Returns: [p_control, p_treatment, z_stat, p_value, reject] as a list.
    """
    pooled_proportion = (control_conversions+treatment_conversions)/(control_visitors+treatment_visitors)
    p_treatment = treatment_conversions/treatment_visitors
    p_control = control_conversions/control_visitors

    standard_error = math.sqrt(pooled_proportion *(1-pooled_proportion) * (1/control_visitors+1/treatment_visitors))
    z = round((p_treatment-p_control)/standard_error,4)
    p = round(2*(1-stats.norm.cdf(abs(z))),4)
    return [p_control,p_treatment,z,p,p<alpha]