from flask import Flask,jsonify,request
import re
from nltk.corpus import stopwords
import joblib
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

s=set(stopwords.words('english'))
stemmer = SnowballStemmer('english', ignore_stopwords=True)
count=0
classifier = joblib.load('clf.txt')
multibin = joblib.load('multibin.txt')
vectorizer_2=CountVectorizer()

app = Flask(__name__)

@app.route('/')
def predictTags():
    question = request.args.get('q')
    print("QUESTION: ",question)
    T=[]
    words = str(question)
    words = re.sub('\n',' ',words)
    words = re.sub('[!@%^&*()$:"?<>=~,;`{}|]',' ',words)
    words = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?]))''',' ',words)
    words = re.sub('_','-',words)
    words = words.replace('[',' ')
    words = words.replace(']',' ')
    words = words.replace('/',' ')
    words = words.replace('\\',' ')
    words = re.sub(r'(\s)\-+(\s)',r'\1', words)
    words = re.sub(r'\.+(\s)',r'\1', words)
    words = re.sub(r'\.+\.(\w)',r'\1', words)
    words = re.sub(r'(\s)\.+(\s)',r'\1', words)
    words = re.sub("'",'', words)
    words = re.sub(r'\s\d+[\.\-\+]+\d+|\s[\.\-\+]+\d+|\s+\d+\s+|\s\d+[\+\-]+',' ',words)
    words = re.sub("^\d+\s|\s\d+\s|\s\d+$"," ", words)
    words = re.sub(r'\s\#+\s|\s\++\s',' ',words)
    stemmed_words = [stemmer.stem(word) for word in words.split()]
    clean_text = filter(lambda w: not w in s,stemmed_words)
    words=''
    for word in clean_text:
            words+=word+' '
    T.append(words)
    print("T",T)
    results=classifier.predict(T)
    results=multibin.inverse_transform(results)
    tag_arr=[]
    for result in results[0]:
        tag_arr.append(result)
    print(tag_arr)
    return (jsonify({"tags":tag_arr}))

if __name__ == "__main__":
    app.run(debug=True)




