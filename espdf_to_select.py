import PyPDF2
import os
import sys

def pdf_to_select(source):
    reader = PyPDF2.PdfFileReader(source)
    number_of_pages = reader.getNumPages()
    reference_numbers = []
    for page in range(number_of_pages):
        pdf_to_string = reader.getPage(page).extractText()
        amount_of_references = pdf_to_string.count("Nº nota: ")
        for _ in range(amount_of_references):
            slice_start = pdf_to_string.find("Nº nota: ") + 9
            current_reference = pdf_to_string[slice_start:]
            if amount_of_references > 1:
                if current_reference not in reference_numbers:
                    pdf_to_string = pdf_to_string[slice_start:]
                    reference_numbers.append(current_reference[: current_reference.find("\n")])
            else:
                reference_numbers.append(current_reference[: current_reference.find("\n")])
    return f"select * from selosutils where referencia in ({', '.join(reference_numbers)})"

if __name__ == '__main__':
    path = sys.argv[1]
    print(pdf_to_select(path))
