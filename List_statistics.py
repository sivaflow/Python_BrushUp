def analyze_list(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    mean_value = sum(numbers) / len(numbers)
    
    stats = {
        "min": min_value,
        "max": max_value,
        "mean": mean_value
    }
    
    return stats

numbers = [500, 900, 340, 210, 560]
stats = analyze_list(numbers)
print(f"List statistics: {stats}")
