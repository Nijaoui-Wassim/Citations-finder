import Levenshtein
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk
import glob


stopwords = stopwords.words('english')

def clean_string(text):
    text =''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text =' '.join([word for word in text.split() if word not in stopwords])
    return text

def cosine_sim_vectors(vec1,vec2):
    vec1 = vec1.reshape(1,-1)
    vec2 = vec2.reshape(1,-1)
    try:
        return (cosine_similarity(vec1, vec2)[0][0])
    except:
        return 0



def treating (parag):
    #cleaned = list(map(clean_string, sentences)) #clean the text
    vectorizer = CountVectorizer().fit_transform(parag) #tranform it into vectors
    vectors = vectorizer.toarray()
    csim = cosine_similarity(vectors)
    result = cosine_sim_vectors(vectors[0], vectors[1])

    print(result)

def get_paragraphs(Name):
    paragraphs = []
    temp = []
    file1 = open(Name + ".txt","r+", encoding="utf8")
    #print(file1)
    for parag in file1.readlines():
        temp.append(parag.split("."))
    
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if len (temp[i][j]) > 25 :
                paragraphs.append(temp[i][j])
            
    cleaned = list(map(clean_string, paragraphs)) #clean the text
    return cleaned



def get_papers(main):
    temp = glob.glob("C:/Users/nijao/Documents/text similarity/papers/*.txt") #
    files = []
        
    for i in temp:
        files.append("papers/"+i.split("\\")[1].replace(".txt",""))

    output = open("out.txt","r+")
    counter = 0
    for file in files:
        counter += 1
        print(counter/42 *100 , ' %')
        sentences = []
        
        output.write('\n\n\n *****  '+str(file)+ '   ***** \n\n\n') 
        print('\n\n\n *****  ',file, '   ***** \n\n\n')
        sentences = get_paragraphs(file)
        lmax = len(sentences)
        sentences = sentences + main
        vectorizer = CountVectorizer().fit_transform(sentences) #tranform the snetences
        vectors = vectorizer.toarray()
        csim = cosine_similarity(vectors)
        for m in range(lmax):
            for n in range(lmax,len(vectors)):
                result = cosine_sim_vectors(vectors[m], vectors[n])
                #print(result)
                if result > 0.6 :
                    
                    try:
                        output.write('\n\n accurcy =  ' +str(result*100)+' %')
                        output.write('\n\n Your sentence from the intro : \n'+sentences[m])
                        output.write('\n\n the similar sentence from the paper : \n'+sentences[n])
                        output.write('paper file name: ' + str(file)+'\n\n')
                    except:
                        output.write('\n error getting the info \n')
                        
                    print('\n accurcy = ' ,result)
                    #print(sentences[n])
                    #print(sentences[m])
                    print('I found a similarity in the file : ' + str(file) + ' in the sentence ')

    output.close()
        
    
    #print(files)
if __name__ == "__main__":
    #treating ()
    intro = get_paragraphs('TextA')
    get_papers(intro)



    
#result = Levenshtein.distance('Levenshtein.distance','Levenshtein distance')
#print(result)



