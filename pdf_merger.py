import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_file):
    # Create a PdfMerger object
    merger = PdfMerger()
    
    # Get a list of PDF files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    
    # Sort the files to merge them in a particular order if necessary
    pdf_files.sort()
    
    # Loop through each PDF file and append it to the merger object
    for pdf_file in pdf_files:
        with open(os.path.join(folder_path, pdf_file), 'rb') as f:
            merger.append(f)
    
    # Write the merged PDF to the output file
    with open(os.path.join(folder_path, output_file), 'wb') as f:
        merger.write(f)

if __name__ == "__main__":
    # Prompt the user to input the folder path and output file name
    folder_path = input("Enter the folder path containing the PDF files: ")
    output_file = input("Enter the output file name for the merged PDF (e.g., merged_output.pdf): ")

    # Call the merge_pdfs_in_folder function with user inputs
    merge_pdfs_in_folder(folder_path, output_file)
