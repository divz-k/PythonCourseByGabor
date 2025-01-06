from Bio import Entrez, SeqIO

# Configure Entrez email
Entrez.email = "your_email@example.com"

def fetch_and_save(database, doc_id):
    # Fetch data
    handle = Entrez.efetch(db=database, id=doc_id, rettype="gb", retmode="text")
    data = handle.read()
    handle.close()

    # Save to file
    filename = f"{doc_id}.gb"
    with open(filename, "w") as fh:
        fh.write(data)

    # Parse and print sequence details
    for seq_record in SeqIO.parse(filename, "genbank"):
        print(f"ID: {seq_record.id}")
        print(f"Sequence: {repr(seq_record.seq)}")
        print(f"Length: {len(seq_record.seq)}")
        print(f"Name: {seq_record.name}")
        print(f"Annotations: {seq_record.annotations}")

# Example usage
fetch_and_save(database="nucleotide", doc_id="EU490707")
