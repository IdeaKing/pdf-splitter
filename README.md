# PDF Merger

PDF Merger is a command-line tool that can split or merge PDF files.

## Installation

To install PDF Merger, download the pdf.exe file from the [releases page](https://github.com/user/pdf-merger/releases) and place it in a folder of your choice.

## Usage

To use PDF Merger, open a terminal and navigate to the folder where you downloaded pdf.exe. Then, type the following command:

```
pdf.exe --split-or-merge <option> --path <path> --output <output>
```

where:

- `<option>` is either `split` or `merge`, depending on whether you want to split a single PDF file into multiple files or merge multiple PDF files into a single file.
- `<path>` is the path to the folder or file containing the PDF(s) that you want to split or merge. If you want to split a PDF file, provide the path to the file. If you want to merge PDF files, provide the path to the folder containing the files. The files in the folder should be named in ascending order (e.g. 1.pdf, 2.pdf, 3.pdf, etc.).
- `<output>` is the name of the output file or folder that you want to create. If you want to split a PDF file, provide the name of the folder where you want to save the split files. If you want to merge PDF files, provide the name of the file that you want to create.

For example, if you want to split a PDF file called report.pdf into three files and save them in a folder called report_parts, type:

```
pdf.exe --split-or-merge split --path report.pdf --output report_parts
```

If you want to merge three PDF files called 1.pdf, 2.pdf and 3.pdf in a folder called slides into a single file called presentation.pdf, type:

```
pdf.exe --split-or-merge merge --path slides --output presentation.pdf
```

## Help

To see the help message and exit, type:

```
pdf.exe -h
```
