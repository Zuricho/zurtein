class SequenceAlignment:
    """
    A class to represent a sequence alignment and support reading from multiple file formats.
    Currently supports FASTA, Stockholm (STO), and A3M formats.
    """

    def __init__(self):
        self.sequences = {}
    
    def read_fasta(self, filename):
        """
        Reads a multiple sequence alignment from a FASTA file.
        """
        with open(filename, 'r') as file:
            sequence_id = None
            sequence_data = None
            for line in file:
                if line.startswith('>'):
                    if sequence_id is not None and sequence_data is not None:
                        self.sequences[sequence_id] = ''.join(sequence_data)
                    sequence_id = line[1:].strip()
                    sequence_data = []
                else:
                    sequence_data.append(line.strip())
            if sequence_id is not None and sequence_data is not None:
                self.sequences[sequence_id] = ''.join(sequence_data)

    def read_sto(self, filename):
        """
        Reads a multiple sequence alignment from a Stockholm file.
        """
        with open(filename, 'r') as file:
            for line in file:
                if not line.startswith('#') and not line.startswith('//') and line.strip():
                    parts = line.split()
                    if len(parts) == 2:
                        sequence_id, sequence = parts
                        if sequence_id in self.sequences:
                            self.sequences[sequence_id] += sequence
                        else:
                            self.sequences[sequence_id] = sequence

    def read_a3m(self, filename):
        """
        Reads a multiple sequence alignment from an A3M file.
        A3M files are similar to FASTA, but can include lower case letters
        and dots to represent gaps. This function will convert them to upper
        case and remove the dots for consistency.
        """
        with open(filename, 'r') as file:
            sequence_id = None
            sequence_data = None
            for line in file:
                if line.startswith('>'):
                    if sequence_id is not None and sequence_data is not None:
                        self.sequences[sequence_id] = ''.join(sequence_data).replace('.', '').upper()
                    sequence_id = line[1:].strip()
                    sequence_data = []
                else:
                    sequence_data.append(line.strip())
            if sequence_id is not None and sequence_data is not None:
                self.sequences[sequence_id] = ''.join(sequence_data).replace('.', '').upper()

    def get_sequences(self):
        """
        Returns the dictionary of sequences.
        """
        return self.sequences









class FoldSeekAlignment:
    def __init__(self, line):
        fields = line.strip().split('\t')
        
        if len(fields) == 21:
            # for most databases
            self.qseqid = fields[0]
            self.tseqid = fields[1]
            self.pident = float(fields[2])
            self.alnlen = int(fields[3])
            self.mismatch = int(fields[4])
            self.gapopen = int(fields[5])
            self.qstart = int(fields[6])
            self.qend = int(fields[7])
            self.tstart = int(fields[8])
            self.tend = int(fields[9])
            self.evalue = float(fields[10])
            self.bitscore = float(fields[11])
            self.prob = int(fields[12])
            self.qlen = int(fields[13])
            self.tlen = int(fields[14])
            self.qaln = fields[15]
            self.taln = fields[16]
            self.tca = [float(x) for x in fields[17].split(',')]
            self.tseq = fields[18]
            self.ttaxid = fields[19]
            self.ttaxname = fields[20]
        elif len(fields) == 19:
            # for GMGC and MGnify
            self.qseqid = fields[0]
            self.tseqid = fields[1]
            self.pident = float(fields[2])
            self.alnlen = int(fields[3])
            self.mismatch = int(fields[4])
            self.gapopen = int(fields[5])
            self.qstart = int(fields[6])
            self.qend = int(fields[7])
            self.tstart = int(fields[8])
            self.tend = int(fields[9])
            self.evalue = float(fields[10])
            self.bitscore = float(fields[11])
            self.prob = int(fields[12])
            self.qlen = int(fields[13])
            self.tlen = int(fields[14])
            self.qaln = fields[15]
            self.taln = fields[16]
            self.tca = [float(x) for x in fields[17].split(',')]
            self.tseq = fields[18]
            self.ttaxid = None
            self.ttaxname = None
        else:
            raise ValueError("Invalid FoldSeek .m8 line format")

    def __str__(self):
        return f"Query: {self.query_id}, target: {self.pident}, E-value: {self.evalue}, Bit Score: {self.bit_score}"
    
    def print_alignment(self):
        print(f"Query: {self.qaln}")
        print(f"Targt: {self.taln}")



class FoldSeekAlignmentParser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        with open(self.filename, 'r') as f:
            alignments = [FoldSeekAlignment(line) for line in f.readlines()]
        return alignments



