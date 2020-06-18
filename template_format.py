import docx

def parse_details(file_path):
    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    print('\n'.join(fullText))

if __name__ == '__main__':
    file_path = raw_input("Enter file path:")
    parse_details(file_path)