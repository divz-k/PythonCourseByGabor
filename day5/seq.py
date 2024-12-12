import sys
from collections import Counter

def calculate_statistics(sequence):
    total = len(sequence)
    counts = Counter(sequence.upper())
    bases = ['A', 'C', 'G', 'T']

    stats = {base: counts.get(base, 0) for base in bases}
    stats['Unknown'] = total - sum(stats.values())
    stats['Total'] = total

    return stats

def print_statistics(stats, title):
    print(title)
    total = stats['Total']
    for base in ['A', 'C', 'G', 'T', 'Unknown']:
        count = stats[base]
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{base}: {count:>8} {percentage:6.1f}%")
    print(f"Total: {total:8}")
    print()

def merge_statistics(all_stats):
    merged = Counter()
    for stats in all_stats:
        merged.update(stats)
    merged['Total'] = sum(stats['Total'] for stats in all_stats)
    return dict(merged)

def main(files):
    all_stats = []

    for file in files:
        try:
            with open(file, 'r') as f:
                sequence = f.read().strip()
                stats = calculate_statistics(sequence)
                print_statistics(stats, file)
                all_stats.append(stats)
        except Exception as e:
            print(f"Error reading file {file}: {e}")

    if all_stats:
        combined_stats = merge_statistics(all_stats)
        print_statistics(combined_stats, "All")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seq.py <file1> <file2> ...")
        sys.exit(1)
    main(sys.argv[1:])
