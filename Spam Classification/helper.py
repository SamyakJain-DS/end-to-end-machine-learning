import numpy as np
import pandas as pd
import email
from sklearn.base import BaseEstimator, TransformerMixin
from bs4 import BeautifulSoup
import regex as re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download("stopwords")

def clean_html(email):
    '''
    To clean any html content in emails.
    :param email: string of html tags and content
    :return: a clean string with no html tags or styling
    '''

    try:
        soup = BeautifulSoup(email.get_payload(), "html.parser")
        plain = soup.text.replace("=\n", "")
        plain = re.sub(r"\s+", " ", plain)
        return plain.strip()
    except:
        return "nothing"
def parse_email(path):
    with open(path, 'rb') as f:
        return email.parser.BytesParser().parse(f)

def email_to_text(mail):
    '''
    This function takes a parsed email and returns the content of the mail
    :param mail: parsed mail object
    :return: body content after cleaning any html tags present
    '''

    text_content = ""
    for part in mail.walk():
        part_content_type = part.get_content_type()
        if part_content_type not in ['text/plain', 'text/html']:
            continue
        if part_content_type == 'text/plain':
            text_content += part.get_payload()
        else:
            text_content += clean_html(part)

    return text_content

class EmailToText(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    def fit(self, mail):
        return self
    def transform(self, mail):
        return [email_to_text(parse_email(mail))]

class CleanBody(BaseEstimator, TransformerMixin):
    '''
    transform a normal english email into preprocessed text optimal for spam classification
    '''

    def __init__(self):
        self.ps = PorterStemmer()
        self.stopwords = set(stopwords.words('english'))

    def fit(self, column, y=None):
        return self

    def transform(self, column):
        if isinstance(column, str):
            self.mail = column
            self.mail = re.sub(r'\n', '', self.mail)  # remove the raw newline character
            self.mail = self.mail.lower()  # turn everything into lowercase
            self.mail = re.sub(r'http\S+|www\.\S+', '', self.mail)  # remove all links
            self.mail = re.sub(r'\b[\w.-]+?@[\w.-]+\.\w+\b', '', self.mail)  # remove all e-mail addresses

            words = self.mail.split()
            filtered = [self.ps.stem(word) for word in words if word not in self.stopwords]  # remove all the stopwords
            self.mail = ' '.join(filtered)

            self.mail = re.sub(r'([!?])', r' \1 ', self.mail)  #
            self.mail = re.sub(r'\s+', ' ', self.mail)  # Normalize spaces

            self.mail = re.sub(r'[^\p{Sc}A-Za-z0-9 !?]+', '', self.mail)  # remove all special characters except spaces and currency symbols
            self.mail = self.mail.strip()  # remove trailing and leading whitespaces
            return self.mail
        elif isinstance(column, list):
            self.mails = column
            cleaned_mails = []
            for mail in self.mails:
                mail = re.sub(r'\n', '', mail)  # remove the raw newline character
                mail = mail.lower()  # turn everything into lowercase
                mail = re.sub(r'http\S+|www\.\S+', '', mail)  # remove all links
                mail = re.sub(r'\b[\w.-]+?@[\w.-]+\.\w+\b', '', mail)  # remove all e-mail addresses

                words = mail.split()
                filtered = [self.ps.stem(word) for word in words if word not in self.stopwords]   # remove all the stopwords
                mail = ' '.join(filtered)

                mail = re.sub(r'([!?])', r' \1 ', mail)  #
                mail = re.sub(r'\s+', ' ', mail)  # Normalize spaces

                mail = re.sub(r'[^\p{Sc}A-Za-z0-9 !?]+', '', mail)    # remove all special characters except spaces and currency symbols
                mail = mail.strip()    # remove trailing and leading whitespaces
                cleaned_mails.append(mail)
            return cleaned_mails
        elif (isinstance(column, pd.Series)) or (isinstance(column, pd.DataFrame)):
            self.mails = column.values
            self.feature_names_ = ['mail']
            cleaned_mails = []
            for mail in self.mails:
                mail = re.sub(r'\n', '', mail)  # remove the raw newline character
                mail = mail.lower()  # turn everything into lowercase
                mail = re.sub(r'http\S+|www\.\S+', '', mail)  # remove all links
                mail = re.sub(r'\b[\w.-]+?@[\w.-]+\.\w+\b', '', mail)  # remove all e-mail addresses

                words = mail.split()
                filtered = [self.ps.stem(word) for word in words if word not in self.stopwords]   # remove all the stopwords
                mail = ' '.join(filtered)

                mail = re.sub(r'([!?])', r' \1 ', mail)  #
                mail = re.sub(r'\s+', ' ', mail)  # Normalize spaces

                mail = re.sub(r'[^\p{Sc}A-Za-z0-9 !?]+', '', mail)    # remove all special characters except spaces and currency symbols
                mail = mail.strip()    # remove trailing and leading whitespaces
                cleaned_mails.append(mail)

            return pd.DataFrame(np.array(cleaned_mails).reshape(-1, 1), columns=self.feature_names_)

    def get_feature_names_out(self, input_features=None):
        return np.array(self.feature_names_)

def flatten_values(df):
    if isinstance(df, pd.DataFrame):
        return df.values.ravel()
    elif isinstance(df, list):
        return df
