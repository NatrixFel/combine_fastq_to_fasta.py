import argparse
from Bio import SeqIO

def combine_fastq_to_fasta(forward_fastq, reverse_fastq, output_fasta):
        with open(forward_fastq, "r") as forward, open(reverse_fastq, "r") as reverse, open(output_fasta, "w") as output:
                forward_records = SeqIO.parse(forward, "fastq")
                reverse_records = SeqIO.parse(reverse, "fastq")

                for fwd_record, rev_record in zip(forward_records, reverse_records):
                        SeqIO.write(fwd_record, output, "fasta")
                        SeqIO.write(rev_record, output, "fasta")

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Combine paired-end FASTQ files into a single FASTA file.")
        parser.add_argument("forward_fastq", help="Path to the forward FASTQ file.")
        parser.add_argument("reverse_fastq", help="Path to the reverse FASTQ file.")
        parser.add_argument("output_fasta", help="Path to the output FASTA file.")

        args = parser.parse_args()
        combine_fastq_to_fasta(args.forward_fastq, args.reverse_fastq, args.output_fasta)
