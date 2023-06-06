import PyPDF2

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()

    # Loop through each input file
    for file in input_files:
        # Open the input PDF file
        with open(file, 'rb') as f:
            # Add the file to the merger
            merger.append(f)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as f:
        merger.write(f)


input_files = []
count = int(input("Enter the number of files to be merged"))

for i in range(count):
    name = input("Enter the name of file ")
    input_files.append(f"{name}.pdf")

updated_name = input("Enter the name of the merged file")
output_file = f'{updated_name}.pdf'

merge_pdfs(input_files, output_file)
