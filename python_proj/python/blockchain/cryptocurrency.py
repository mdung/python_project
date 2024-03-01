import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset (replace it with your actual data)
data = {
    'Name': ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano'],
    'Description': [
        'Bitcoin is a decentralized digital currency without a central bank or single administrator.',
        'Ethereum is a decentralized platform that runs smart contracts.',
        'Ripple is both a platform and a currency.',
        'Litecoin is a peer-to-peer cryptocurrency.',
        'Cardano is a blockchain platform for the development of decentralized applications.'
    ],
    'InvestmentRisk': [3, 4, 2, 3, 5],
    'Volatility': [4, 5, 3, 4, 2]
}

df = pd.DataFrame(data)

# Preprocessing text data
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])

# Calculate cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get cryptocurrency recommendations based on similarity
def get_recommendations(crypto_name, cosine_sim_matrix, df):
    idx = df[df['Name'] == crypto_name].index[0]
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar cryptocurrencies

    crypto_indices = [i[0] for i in sim_scores]
    return df['Name'].iloc[crypto_indices]

# Test the recommendation system
input_crypto = 'Bitcoin'
recommendations = get_recommendations(input_crypto, cosine_sim, df)

print(f"Recommendations for {input_crypto}:")
print(recommendations)
