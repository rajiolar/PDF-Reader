from pypdf import PdfReader


def myPdfReader(pdf_File_Dir):
    
    pdf_reader = PdfReader(pdf_File_Dir)
    all_text  = ""

    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        all_text += text
    
    return all_text

pdfText = myPdfReader('/Users/user/Downloads/Corning.pdf')

def encrypt(text):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) +  3 - 65) % 26 + 65)
    
    return result

encryptedPdfText = encrypt(pdfText)

print(encryptedPdfText)