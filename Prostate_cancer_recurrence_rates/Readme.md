Although its use in screening healthy patients is debatable, Prostate Specific Antigen (PSA) is a very useful blood test for following the response of prostate cancer to treatment.

For patients treated with radiation therapy alone for prostate cancer, the PSA tends to take 2-3 years to reach a minimum value (nadir). If the PSA begins to rise again after the nadir value, this may represent a recurrence of prostate cancer.

The 2006 "Phoenix" definition (1) of a biochemical recurrence is: PSA level of at least 2.0 above the nadir (lowest value) occuring after reaching the nadir.

You are given a list of PSA values for one patient. The list consists of 12 PSA values in ng/mL (as a float with 2 decimal places) each taken 6 months apart. The first value is taken immediately before treatment. The nadir (minimum value) will only occur once in the list.

Return True if the values meet the Phoenix criteria (PSA at least 2 higher than the lowest value, occuring any time after the lowest value is reached) or False if they do not.

Note: Be careful with comparing float values for equality due to representation errors. It may make sense to check that the PSA is >1.999 of the nadir in your code.

Examples:

Input:
[7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35]
Ouput:
False
# Nadir 0.48, highest subsequent value 1.36 is less than 2 + 0.48

Input:
[9.98, 8.56, 4.62, 1.16, 0.26, 0.37, 0.32, 1.02, 0.99, 1.56, 1.41, 2.35],
Ouput:
True
# Nadir 0.26, highest subsequent value 2.35 is greater or equal to 2 + 0.26

Input:
[12.57, 6.86, 1.86, 1.93, 0.60, 1.46, 1.58,1.58, 0.86, 0.72, 0.88, 2.1]
Output:
False
# Nadir 0.60, highest subsequent value 2.1 is less than 2 + 0.60
(1) Roach M 3rd, Hanks G, Thames H Jr, et al. Defining biochemical failure following radiotherapy with or without hormonal therapy in men with clinically localized prostate cancer: recommendations of the RTOG-ASTRO Phoenix Consensus Conference. Int J Radiat Oncol Biol Phys. 2006;65:965–974.