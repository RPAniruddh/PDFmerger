# PDF Merger

This Python script allows you to merge multiple PDF files into a single PDF file. It utilizes the PyPDF2 library for PDF manipulation.

## Usage

1. Ensure you have PyPDF2 installed:

```bash
pip install PyPDF2
```

2. Run the script:

```bash
python pdf_merger.py
```

3. Follow the prompts to merge PDF files:

   - Enter the number of files to be merged.
   - Provide the names of each file (without the ".pdf" extension).
   - Enter the desired name for the merged PDF file.

The script will merge the specified PDF files and save the output as a single PDF.

## Example

```plaintext
Enter the number of files to be merged: 3
Enter the name of file 1: document_1
Enter the name of file 2: document_2
Enter the name of file 3: document_3
Enter the name of the merged file: merged_document

Merging PDFs...
Merged successfully! The file 'merged_document.pdf' has been created.
```

## Note

- Make sure you have Python installed on your system.
- The input PDF files should be in the same directory as the script, or you should provide the correct file paths.

## Author

[Aniruddh R Panicker](https://github.com/RPAniruddh)

---
