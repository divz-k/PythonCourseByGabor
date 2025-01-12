import argparse
from Bio import SeqIO
import re
import os

# Function to find the longest repeating subsequence
def find_longest_dup(seq):
    n = len(seq)
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    longest_subseq = ""
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):  # Start j from i+1 to avoid overlap
            if seq[i - 1] == seq[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update longest substring if needed
                if dp[i][j] > len(longest_subseq):
                    longest_subseq = seq[i - dp[i][j]:i]
    return longest_subseq


# Function to calculate GC content
def calculate_gc_content(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    return (g_count + c_count) / len(seq) * 100

# Function to find palindromes
def count_motifs(seq, patterns=["AGGGG", "ATGCT"]):
    counts = {pattern: seq.count(pattern) for pattern in patterns}
    return counts

# Main analysis function

def analyse_sequence(file_path, find_duplicates=False, find_gc=False, find_motifs=False):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Determine format based on the extension
    if file_extension == ".fasta":
        file_format = "fasta"
    elif file_extension == ".gb" or file_extension == ".genbank":
        file_format = "genbank"
    else:
        raise ValueError("Unsupported file format. Please provide a '.fasta' or '.genbank' file.")
    
    # Parse the sequence file
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, file_format):
            seq = str(record.seq)
            #print(f"Analyzing sequence: {record.id}")
            
            if find_duplicates:
                print("Longest repeating subsequence: ", find_longest_dup(seq))
            
            if find_gc:
                print(f"GC content: {calculate_gc_content(seq):.2f}%")
            
            if count_motifs:
                motif_counts = count_motifs(seq)
                if motif_counts:
                    print("Motifs found:")
                    for motif, count in motif_counts.items():
                        print(f"{motif}: {count} occurrences")
                else:
                    print("No motifs found.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Analyse sequences in FASTA format.")
    parser.add_argument("file", help="Path to the sequence file")
    parser.add_argument("--duplicates", action="store_true", help="Find longest repeating subsequence")
    parser.add_argument("--GCcontent", action="store_true", help="Perform the second analysis (GC content)")
    parser.add_argument("--motifs", action="store_true", help="Find AGGGG ATGCT motifs in the sequence")
    args = parser.parse_args()
    
    analyse_sequence(args.file, find_duplicates=args.duplicates, find_gc=args.GCcontent, find_motifs=args.motifs)
