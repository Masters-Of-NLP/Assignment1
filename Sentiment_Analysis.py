import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

def perform_sentiment_analysis(csv_path, model_path):
    
    # Using model_path as both model and tokenizer directly in this example
    model = model_path
    tokenizer = model_path
    
    # Try reading existing output file or initialize an empty DataFrame
    try:
        output_df = pd.read_csv("sentiment_output_4_ver2.csv")
    except FileNotFoundError:
        output_df = pd.DataFrame()
        
    # Initialize the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    
    # Read the input CSV file containing comments
    comments_df = pd.read_csv(csv_path)
    
    # Loop through each row in the DataFrame
    for i in range(len(comments_df)):
        
        # Slice the DataFrame to get the current row
        current_row = comments_df[i:i+1]
        
        # Convert all comments to strings and handle NaNs
        current_row['Preprocessed_Comment'] = current_row['Preprocessed_Comment'].astype(str)
        
        try:
            # Perform sentiment analysis on comments
            comments = current_row['Preprocessed_Comment'].tolist()
            sentiments = sentiment_pipeline(comments)
            
            # Normalize sentiment labels
            sentiment_labels = [item['label'] for item in sentiments]
            for i in range(len(sentiment_labels)):
                if sentiment_labels[i] in ['NEU', 'LABEL_1']:
                    sentiment_labels[i] = 'neutral'
                elif sentiment_labels[i] in ['POS', 'LABEL_2']:
                    sentiment_labels[i] = 'positive'
                elif sentiment_labels[i] in ['NEG', 'LABEL_0']:
                    sentiment_labels[i] = 'negative'
                    
            # Append sentiment labels to DataFrame
            current_row['Sentiment'] = sentiment_labels
            
            # Concatenate the result to the output DataFrame
            output_df = pd.concat([output_df, current_row], ignore_index=True)
            
            # Save the output DataFrame to a CSV file
            output_df.to_csv("sentiment_output_4_ver2.csv", index=False)
            
        except Exception as e:
            print(f"Error occurred at index {i}: {e}")
    
    print("Sentiment analysis complete! Results saved to 'sentiment_output_4_ver2.csv'.")

# Specify the path for your CSV file and model
csv_path = "Assignment1/final_preprocessed_comments.csv"
model_path = "Assignment1/sentiment_analysis_generic_dataset"

# Execute the function to perform sentiment analysis
perform_sentiment_analysis(csv_path, model_path)
