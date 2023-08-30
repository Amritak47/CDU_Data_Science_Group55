# inferential statistics 
import scipy.stats as stats

# Given data
mean_pitch_pd = 162.95036807692307
std_pitch_pd = 48.760931
sample_size_pd = 520  

mean_pitch_non_pd = 174.50487307692308
std_pitch_non_pd = 61.861037
sample_size_non_pd = 520  

# confidence level (e.g., 95%)
confidence_level = 0.95

# calculate Z-score for the confidence level
z_score = stats.norm.ppf((1 + confidence_level) / 2)

# confidence interval for PD group
ci_pd = z_score * (std_pitch_pd / (sample_size_pd ** 0.5))
ci_pd_lower = mean_pitch_pd - ci_pd
ci_pd_upper = mean_pitch_pd + ci_pd

# for Non-PD group
ci_non_pd = z_score * (std_pitch_non_pd / (sample_size_non_pd ** 0.5))
ci_non_pd_lower = mean_pitch_non_pd - ci_non_pd
ci_non_pd_upper = mean_pitch_non_pd + ci_non_pd


print("Confidence Interval for 'Pitch (mean)' in PD group:", (ci_pd_lower, ci_pd_upper))
print("Confidence Interval for 'Pitch (mean)' in Non-PD group:", (ci_non_pd_lower, ci_non_pd_upper))
