import os
from pypdf import PdfMerger


def merge_pdfs(directory, output_file):
    merger = PdfMerger()

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            merger.append(filepath)

    merger.write(output_file)
    merger.close()
