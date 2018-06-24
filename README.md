# Find out what your website is really about

Using TF.IDF (Term Frequency times Inverse Document Frequency) to report back
what your website is about. 

Give it text files, common words are ignored (stopwords), but also the use of
Inverse Document Frequency reduces these. 

## Running

    python main.py file1.txt,file2.txt

You can also pass words to ignore (somewhat reducing the point of Inverse 
Document Frequency) by passing them after the file names:

    python main.py file1.txt,file2.txt bob,cat
In the above example, 'bob' and 'cat' would be ignored

Credit
 J.Dimopoulos for assistance with the math 
