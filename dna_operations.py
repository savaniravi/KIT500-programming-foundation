# this file is dna_operations.py

__author__ = 'Savani Ravikumar'

import re

def clean_sequence(sequence: str) -> str:
    """
    Clean a DNA sequence by replacing non-DNA characters with '.'.
    """
    return re.sub(r'[^ATGC]', '.', sequence)

def calculate_error_rate(sequence: str) -> float:
    """
    Calculate the error rate of a DNA sequence.
    """
    error_count = sequence.count('.')
    return (error_count / len(sequence)) * 100

def display_complement(sequence: str) -> None:
    """
    Display the complement of a DNA sequence.
    """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '.': '.'}
    complement_sequence = ''.join(complement[base] for base in sequence)
    print(sequence)
    print('|' * len(sequence))
    print(complement_sequence)

def transcribe_sequence(sequence: str) -> None:
    """
    Transcribe a DNA sequence into RNA.
    """
    rna_sequence = sequence.replace('T', 'U')
    print(rna_sequence)

def transcribe_section(sequence: str) -> str:
    """
    Transcribe a section of a DNA sequence into RNA.
    """
    start = int(input("Enter the start position (1-based index): ")) - 1
    length = int(input("Enter the length of the section: "))
    rna_section = sequence[start:start + length].replace('T', 'U')
    print(rna_section)
    return sequence

def splice_sequence(sequence: str) -> str:
    """
    Splice another DNA sequence onto the end of the current sequence.
    """
    new_sequence = input("Enter another DNA sequence to splice: ").upper()
    cleaned_new_sequence = clean_sequence(new_sequence)
    return sequence + cleaned_new_sequence
