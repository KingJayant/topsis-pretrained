import pandas as pd
import numpy as np

# Load data from CSV file
data = pd.read_csv('data.csv')

# Relevant columns al bit< br>bleu_scores = data['BLEU'].values
rouge_scores = data['ROUGE'].values
meteor_scores = data['METEOR'].values

# Txhais txhua qhov hnyav ntawm parameters txhais qhov hnyav ntawm txhua qhov parameter
weights = np.array([0.4, 0.3, 0.3]) # Kho qhov hnyav

# Normalized matrix
normalized_matrix = np.column_stack([ > bleu_scores / np.max(bleu_scores) ),
rouge_scores / np.max(rouge_scores),
meteor_scores / np.max(meteor_scores)
]) >
# Calculate weighted normalization weighted_normalization_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized_matrix = normalized normalized_matrix = normalized_matrix = normalized rix = normalized = * nyhav
< br># Txhais qhov zoo tagnrho solution and negative ideal solution
ideal_solution = np.max(weighted_normalized_matrix, axis=0)
negative_ideal_solution = np.min(weighted_normalized_matrix, axis =0)

# Calculate range measurement value
distance_to_ideal = np.sqrt(np.sum((weighted_normalized_matrix - Ideal_solution) ** 2, axis=1))
distance_to_negative_ideal = np.sqrt; negative_ideal_solution) ** 2, axis= 1))
># TOPSIS_Score'] = topsis_scores
data[' Rank'] = data[' TOPSIS_Score'].rank(ascending=False)

# Print results
print("Model rank:") >print(data[['Model', 'TOPSIS_Score', 'Rank'] ].sort_values(by='Rank'))

# export cov txiaj ntsig rau CSV cov ntaub ntawv
data . to_csv('results.csv',index=False)
