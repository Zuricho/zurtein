from typing import List
# Parses fasta file and returns sequence header and sequence in a list
class Sequence:
    def __init__(self, header: str, sequence: str):
        """
        Initialize a Sequence object with a header and sequence.

        Args:
            header (str): The header of the sequence.
            sequence (str): The sequence data.

        Returns:
            None
        """
        self.header = header
        self.sequence = sequence
        self.sequence_fix()

    def __str__(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __iter__(self):
        return iter(self.sequence)
    
    def __bool__(self):
        return bool(self.sequence)

    def sequence_fix(self):
        """
        Fixes the sequence by replacing any characters that are not valid amino acids or asterisk with 'U'.
        """
        amino_acids = "ACDEFGHIKLMNPQRSTVWY"
        fixed_sequence = []
        for char in self.sequence:
            if char != '*':
                if char.strip() and char.upper() in amino_acids:
                    fixed_sequence.append(char.upper())
                else:
                    fixed_sequence.append('U')
        self.sequence = ''.join(fixed_sequence)



def parse_fasta(filename: str) -> List[Sequence]:
    """
    Parses a FASTA file and returns a list of Sequence objects.

    Args:
        filename (str): The path to the FASTA file.

    Returns:
        List[Sequence]: A list of Sequence objects, each representing a sequence in the FASTA file.
    """
    with open(filename, 'r') as f:
        contents = f.read().split('>')[1:]
        data = []
        for entry in contents:
            lines = entry.split('\n')
            header = lines[0]
            sequence = ''.join(lines[1:])
            sequence = sequence.replace("*", "") if "*" in sequence else sequence
            data.append(Sequence(header, sequence))
    return data








