# Python CustomTkinter PDF Reader

A desktop PDF text reader built with Python, CustomTkinter, and PyPDF2. The application allows users to select a PDF file and display its extracted text in a graphical interface.

## Features

- **Open PDF files:** Select a PDF using a file dialog.
- **Extract text:** Read text from each page of the selected PDF.
- **Multi-page support:** Extract text from all pages in the document.
- **Text display:** Show extracted content in a text box.
- **File selection display:** Display the selected file path.
- **Scrollable text area:** Browse longer extracted documents using the text widget's scrollbar.

## Technologies Used

- Python
- CustomTkinter
- PyPDF2
- Tkinter file dialogs
- File handling
- Loops and functions

## Installation

Install the required libraries:

```bash
pip install customtkinter PyPDF2
```

## How to Run

1. Save the code as `pdf_reader.py`.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python pdf_reader.py
   ```

4. Click **Open File**.
5. Select a PDF to display its extracted text.

## How It Works

1. The application opens a file-selection dialog.
2. The user chooses a PDF file.
3. PyPDF2 reads the PDF document.
4. The program iterates through each page and extracts available text.
5. The extracted content is displayed in the text box.

## Project Structure

```text
python-customtkinter-pdf-reader/
└── pdf_reader.py
```

## Limitations

- Scanned PDFs containing only images may not produce extractable text.
- Some PDFs may have unusual layouts that cause text to appear out of order.
- The application currently does not handle PDF-reading errors explicitly.
- The selected file's full path is displayed in the interface.

## Learning Outcomes

This project demonstrates GUI development, file dialogs, PDF processing, page iteration, text extraction, and displaying file content in a desktop application.
