import csv
import re

# --- Configuration ---
POSITIVE_KEYWORDS = {
    'quality': ['good quality', 'great fabric', 'excellent material', 'well made', 'durable'],
    'fit': ['perfect fit', 'fits well', 'true to size'],
    'look': ['looks beautiful', 'color is vibrant', 'stylish design'],
    'delivery': ['fast delivery', 'on time']
}

NEGATIVE_KEYWORDS = {
    'quality': ['poor quality', 'bad fabric', 'cheap material', 'tore easily', 'stitching is bad'],
    'fit': ['too small', 'too large', 'does not fit', 'wrong size'],
    'look': ['color faded', 'looks different', 'not as pictured'],
    'delivery': ['late delivery', 'slow shipping']
}

def analyze_product_reviews(product_id, reviews):
    """Analyzes all reviews for a single product and generates a summary."""
    pros = []
    cons = []

    for review in reviews:
        review_lower = review.lower()
        for theme, keywords in POSITIVE_KEYWORDS.items():
            if any(keyword in review_lower for keyword in keywords):
                if theme not in pros:
                    pros.append(theme)
        
        for theme, keywords in NEGATIVE_KEYWORDS.items():
            if any(keyword in review_lower for keyword in keywords):
                if theme not in cons:
                    cons.append(theme)

    return {
        'product_id': product_id,
        'summary': {
            'pros': pros if pros else ['Generally positive feedback'],
            'cons': cons if cons else ['No major issues reported']
        }
    }

def main():
    """Main function to run the review analysis simulation."""
    print("--- Running AI Review Summary Simulation ---")
    
    reviews_by_product = {}
    with open('sample_reviews.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            product_id = row['product_id']
            if product_id not in reviews_by_product:
                reviews_by_product[product_id] = []
            reviews_by_product[product_id].append(row['review_text'])

    for product_id, reviews in reviews_by_product.items():
        result = analyze_product_reviews(product_id, reviews)
        print(f"\nAnalysis for Product ID: {result['product_id']}")
        print(f"  Pros: {', '.join(result['summary']['pros'])}")
        print(f"  Cons: {', '.join(result['summary']['cons'])}")

if __name__ == '__main__':
    main()
