# Pretrained-model-Comparison-using-Topsis
## Overview

Welcome to the Text Generation Model Comparison project! This initiative aims to help users select the most suitable text generation model by comparing various pre-trained models using the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. Through the assessment of key metrics such as BLEU, ROUGE, and METEOR, this project offers insights into the efficacy and efficiency of different models in generating natural language text.

## Key Features:

1. **Holistic Metrics Evaluation:**
   - This project evaluates models based on a comprehensive set of metrics, including BLEU, ROUGE, and METEOR. This provides a well-rounded perspective on model performance in text generation tasks.
2. **Methodology - TOPSIS:**
   - Leveraging the TOPSIS method ensures a robust comparison by considering both similarity to the ideal solution and dissimilarity to the negative ideal solution, facilitating a reliable ranking of text generation models.
     
3. **Models Assessed:**
   - Models such as BERT, GPT-3, XLNet, T5, CTRL, and UniLM are assessed, representing widely-used pre-trained models in text generation applications.

## Project Structure:

- **`data.csv`**: Contains evaluation metrics for each model.
- **`result.csv`**: Presents ranked results in a tabular format for easy interpretation

## Results and Analysis:
1. **Ranked Table:**

| **Model**   | **BLEU**    | **ROUGE**              | **METEOR**         |
|-------------|-------------------|-----------------------|-------------------|
| BERT    | 0.42                | 0.52                  | 0.36              |
| GPT-3  | 0.40                | 0.50                  | 0.34              |
| XLNet       | 0.38                | 0.48                  | 0.32              |
| T5       | 0.36                | 0.46                  | 0.30              |
| CTRL       | 0.34                | 0.44                  | 0.28              |
| UniLM        | 0.39              | 0.49                  | 0.35              |




## Analysis:
**Model Performance:**
BERT achieves the highest BLEU, ROUGE, and METEOR scores, indicating superior text generation quality. GPT-3 and XLNet closely follow in performance, while T5 and UniLM show competitive results across the metrics.

**Efficiency Consideration:**  CTRL, despite recording the highest perplexity score, exhibits competitive BLEU, ROUGE, and METEOR scores compared to other models. This highlights potential trade-offs between perplexity and text generation quality. Additionally, computational efficiency and response time remain crucial considerations for real-time text generation applications.
