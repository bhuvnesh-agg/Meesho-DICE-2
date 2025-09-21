# Meesho-DICE-2
This repository contains a Proof of Concept (PoC) for the **M-trusted 2.0** framework, a proposed solution for the Meesho DICE Challenge. It simulates the core components of a system designed to fix trust and discovery on the Meesho platform.

## **The Problem: A Broken Trust Loop**

Meesho's current trust ecosystem suffers from two core failures:

1. **Signal Fragmentation & Opacity:** Multiple, confusing labels ("M-trusted", "Gold") with no clear, transparent meaning.  
2. **Algorithmic Invisibility:** The platform's search algorithm fails to prioritize its own quality-certified products, making them invisible to users.

This leads to a "quality roulette" for users and punishes high-quality sellers.

## **The Solution: M-trusted 2.0**

We propose a unified framework to fix this broken loop, built on three pillars:

1. **A Single, Unified Trust Badge:** Retire all confusing labels and use a single **M-trusted** badge.  
2. **An AI Review Summary:** Provide at-a-glance, unbiased proof of a product's pros and cons.  
3. **Inherently Trusted Search:** Re-architect the search algorithm to use trust as a primary ranking factor.

## **Architecture Overview**

The proposed solution is a scalable, microservices-based architecture.

* **Data Ingestion:** Real-time event streams (orders, returns, reviews).  
* **M-trusted Engine:** A set of microservices to calculate scores and analyze reviews.  
* **Data Storage:** A Data Warehouse for analytics and a NoSQL DB for serving live data.

## **Proof of Concept: Simulating the Core Logic**

This repository contains Python scripts that simulate the two core backend services.

### **1\. Seller Trust Score (STS) Engine**

This service calculates a data-driven score for each seller to determine if they earn the M-trusted badge.  
**To run the simulation:**  
```
cd services/sts-engine  
python simulate\_sts.py
```

The script reads from sample\_seller\_data.csv and calculates the STS based on quality returns, fulfillment accuracy, and average ratings.

### **2\. AI Review Analyzer**

This service simulates the NLP model that generates a "pros and cons" summary from user reviews. For this PoC, it uses a keyword-based approach to demonstrate the principle.  
**Note on the implementation:** Our final proposed solution uses a sophisticated transformer model like BERT for contextual understanding. For this Proof of Concept, we have built a smart, keyword-based script that effectively simulates the intended functionality and demonstrates the value of the AI summary feature without the overhead of a full ML model.
**To run the simulation:**  
```
cd services/review-analyzer  
python analyze\_reviews.py
```

The script reads from sample\_reviews.csv and extracts key themes to generate a summary for each product.

## **Mockups & Diagrams**

Visual artifacts for this project can be found in the /docs folder:
* **System diagrams:** [STS Pipeline](https://github.com/bhuvnesh-agg/Meesho-DICE-2/blob/main/docs/flow1.png?raw=true), [AI Review Flow](https://github.com/bhuvnesh-agg/Meesho-DICE-2/blob/main/docs/flow2.png?raw=true)
* **Mockups:**

  * The Search UI: [Before](https://github.com/bhuvnesh-agg/Meesho-DICE-2/blob/main/docs/meesho_before.png?raw=true) → [After](https://github.com/bhuvnesh-agg/Meesho-DICE-2/blob/main/docs/meesho_after.png?raw=true)
  * [M-trusted explainer page](https://github.com/bhuvnesh-agg/Meesho-DICE-2/blob/main/docs/meesho_description.png?raw=true)
