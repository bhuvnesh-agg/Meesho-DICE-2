import csv

# --- Configuration ---
WEIGHTS = {
    'quality_score': 0.5,
    'fulfillment_score': 0.3,
    'rating_score': 0.2
}
M_TRUSTED_THRESHOLD = 85

def calculate_quality_score(returns__total_orders):
    """Calculates score based on quality-related returns. Lower is better."""
    quality_return_rate = returns_total_orders
    return max(0, 100 - (quality_return_rate * 2000)) 

def calculate_fulfillment_score(accuracy_rate, on_time_rate):
    """Calculates score based on order accuracy and dispatch speed."""
    return (accuracy_rate + on_time_rate) / 2

def calculate_rating_score(avg_rating):
    """Converts a 1-5 star rating to a 0-100 scale."""
    return ((avg_rating - 1) / 4) * 100

def calculate_sts(seller_data):
    """Calculates the final Seller Trust Score (STS)."""
    quality_score = calculate_quality_score(float(seller_data['quality_returns_rate']))
    fulfillment_score = calculate_fulfillment_score(float(seller_data['order_accuracy_rate']), float(seller_data['on_time_dispatch_rate']))
    rating_score = calculate_rating_score(float(seller_data['avg_rating']))

    final_sts = (
        quality_score * WEIGHTS['quality_score'] +
        fulfillment_score * WEIGHTS['fulfillment_score'] +
        rating_score * WEIGHTS['rating_score']
    )
    
    return {
        'seller_id': seller_data['seller_id'],
        'final_sts': round(final_sts, 2),
        'is_mtrusted': final_sts >= M_TRUSTED_THRESHOLD,
        'components': {
            'quality_score': round(quality_score, 2),
            'fulfillment_score': round(fulfillment_score, 2),
            'rating_score': round(rating_score, 2)
        }
    }

def main():
    """Main function to run the simulation."""
    print("--- Running M-trusted Seller Trust Score (STS) Simulation ---")
    
    with open('sample_seller_data.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            result = calculate_sts(row)
            print(f"\nProcessing Seller ID: {result['seller_id']}")
            print(f"  Component Scores -> Quality: {result['components']['quality_score']}, Fulfillment: {result['components']['fulfillment_score']}, Rating: {result['components']['rating_score']}")
            print(f"  Final STS Score: {result['final_sts']}")
            if result['is_mtrusted']:
                print(f"  Result: QUALIFIES for M-trusted Badge.")
            else:
                print(f"  Result: Does NOT qualify for M-trusted Badge.")

if __name__ == '__main__':
    main()
