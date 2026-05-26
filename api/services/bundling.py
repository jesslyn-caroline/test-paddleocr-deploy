from collections import Counter
from itertools import combinations

def get_bundling(data):
    item_counter = Counter()
    pair_counter = Counter()

    for items in data:
        items = list(set(items))
        for item in items:
            item_counter[item] += 1
        for pair in combinations(items, 2):
            pair = tuple(sorted(pair))
            pair_counter[pair] += 1
    
    bundle_results = []
    MIN_FREQUENCY = 3

    for (product_1, product_2), frequency in pair_counter.items():
        if frequency < MIN_FREQUENCY:
            continue

        confidence_1 = frequency / item_counter[product_1]
        confidence_2 = frequency / item_counter[product_2]

        score = (confidence_1 + confidence_2) / 2

        bundle_results.append({
            "product_1": product_1.title(),
            "product_2": product_2.title(),
            "score": round(score * 100),
            "frequency": frequency
        })

    bundle_results = sorted(bundle_results, key=lambda result: result["score"], reverse=True)

    top_n = 5 if len(bundle_results) > 5 else len(bundle_results)

    top_n_bundle = bundle_results[:top_n]
    top_n_bundle = [
        f"{result['product_1']} dan {result['product_2']} dibeli bersama {result['frequency']} kali. Sekitar {result['score']}% dari pembelian yang membeli salah satu produk akan membeli keduanya."
        for result in top_n_bundle
    ]

    return top_n_bundle