'''
This file is for evaluating the quality of our RAG system usin the Hairy Trumpet dataset.
'''

import ragnews

class RAGEvaluator:
    def predict(self, masked_text): #self rerfers to class that we are in, x is the data point
        '''
        >>> model = RAGEvaluator()
        >>> model.predict('There is no mask token here')
        []
        >>> model.predict('[MASK0] is the democratic nominee')
        ['Harris']
        >>> model.predict('[MASK0] is the democratic nominee and [MASK1] is the republican nominee'])
        ['Harris, Trump']
        '''
        # you might think about...
        # calling the ragnews.run_llm function directly;
        # so we will call the ragnews.rag function

        db = ragnews.ArticleDB('ragnews.db')
      
        textprompt = f'''This is a fancier question that is based on standard cloze style benchmarks. 
        I am going to provide you a sentence, and that sentence will have a mask token inside of it that will look like [MASK0] or [MASK1] or [MASK2] and so on. 
        Your job is to tell me what the value of that mask token was. 
        The size of your ourput should just be a single word for each mask. 
        You should not provide any explanation or other extraneous words in the output, only provide a single word for each mask. 
        If there are multiple mask tokens, provide each token separately with whitespace in between. 

        INPUT:[MASK0] is the democratic nominee
        OUTPUT: Harris

        INPUT: [MASK0] is the democratic nominee and [MASK1] is the republican nominee
        OUTPUT:['Harris, Trump']

        INPUT: {masked_text}
        OUTPUT: '''
        output = ragnews.rag(textprompt, db, keywords_text = masked_text)
        return output
    
    #reasons for bad results - 
    #1. the code (esp the prompt) in this function is bad - be sure the prompt explains the format of the output and examples of input/output pairs
    #2. the rag function itself could be bad
    # In order to improve 1 of the above problems, and prompt engineering does not work, we must change the model that we are using

