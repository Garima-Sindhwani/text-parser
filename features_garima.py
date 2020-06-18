# Method to extract count of words in the resume text
def count_words(resume_text):
    words = resume_text.split()
    return len(words)
    
# Method to extract another feature
def extract_other_feature(resume_text):
    return 'dummy'
    
# Driver Method
def driver():
    result = {}
    resume_text = """
        GARIMA SINDHWANI
        gsindhwani23@gmail.com |+91  9916738773 | garima-sindhwani-linkedin
        Gurugram, Haryana

        SUMMARY
        Senior Software Engineer, currently working with big data using PySpark. Hands on experience in Data cleaning, EDA and development of machine learning models using Python scikit-learn library. A good experience in development of Web & Enterprise applications using Java and Spring.
        An active team player and a keen learner! Looking for opportunities in data science!
    """
    result['wordcount'] = count_words(resume_text)
    result['other_feature'] = extract_other_feature(resume_text)
    return result
    
 # Call Driver
 driver()
