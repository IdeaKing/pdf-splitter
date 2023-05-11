import os
import argparse
import PyPDF2


def main(
    args: argparse.Namespace):
    if args.split_or_merge == "split":
        split(args.path, args.output)
    elif args.split_or_merge == "merge":
        merge(args.path, args.output)
    else:
        print("No argument given")



def split(path: str, 
          output: str):
    """
    Splits a PDF into multiple PDFs
    """
    # Open the PDF File
    pdfFileObj = open(path, 'rb')
    # Read the PDF File with PyPDF2
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # Create the output directory if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)
    # Loop through all the pages of the PDF
    for i in range(len(pdfReader.pages)):
        # Create a new PDF Writer for each page
        pdfWriter = PyPDF2.PdfWriter()
        # Add the page to the PDF Writer object
        pdfWriter.add_page(pdfReader.pages[i])
        # create the output String
        path_name = os.path.join(output, str(i) + ".pdf")
        # Create the output PDF File
        pdfOutput = open(path_name, 'wb')
        # Write the PDF File to the output file
        pdfWriter.write(pdfOutput)
        # Close the output PDF File
        pdfOutput.close()

    print("Splitting done")


def merge(path: str, 
          output: str):
    """
    Merges all PDFs in a folder into one PDF
    """
    pdfWriter = PyPDF2.PdfWriter()
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            _path = os.path.join(path, filename)
            pdfFileObj = open(_path, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            for i in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[i])
            pdfFileObj.close()

    pdfOutput = open(output, 'wb+')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

    print("Merging done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="PDF Merger")
    parser.add_argument("--split-or-merge", 
                        help="Path to the folder containing the PDFs",
                        type=str)
    parser.add_argument("--path", \
                        help="Path to the folder/file containing the PDF(s)",
                        type=str)
    parser.add_argument("--output", 
                        help="Name of the output file/folder",
                        type=str)
    args = parser.parse_args()

    main(args)
