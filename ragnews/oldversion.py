# '''
# This file is for evaluating the quality of our RAG system usin the Hairy Trumpet dataset.
# '''

# import ragnews

# class RAGEvaluator:
#     # def __init__(self, labels):
#     #     self.valid_labels = labels
#     #     self.db = ragnews.ArticleDB('ragnews.db')
#     def predict(self, masked_text): #self refers to class that we are in, x is the data point
#         '''
#         >>> model = RAGEvaluator()
#         >>> model.predict('There is no mask token here')
#         []
#         >>> model.predict('[MASK0] is the democratic nominee')
#         ['Harris']
#         >>> model.predict('[MASK0] is the democratic nominee and [MASK1] is the republican nominee')
#         ['Harris, Trump']
#         '''
#         # you might think about...
#         # calling the ragnews.run_llm function directly;
#         # so we will call the ragnews.rag function

#         labels = ['Harris', 'Trump']

#         db = ragnews.ArticleDB('ragnews.db')
      
#         textprompt = f'''
# This is a fancier question that is based on standard cloze style benchmarks. 
# I am going to provide you a sentence, and that sentence will have a mask token inside of it that will look like [MASK0] or [MASK1] or [MASK2] and so on. 
# Your job is to tell me what the value of that mask token was. 
# The size of your output should just be a single word for each mask. If there is one mask, output one word. If there are two masks, output two words. Separate the masks with commas.
# You should not provide any explanation or other extraneous words in the output, only provide a single word for each mask, with absolutely nothing else. 
# You will get a prize if you respond with just the masked token(s). You will be punished if you output your thought proecss, a description of the information you're learning from, or any information that is not the masked tokens.
# If there are multiple mask tokens, provide each token separately with whitespace in between. 
# Valid values include: {labels}

# INPUT:[MASK0] is the current democratic presidential nominee
# OUTPUT: Harris

# INPUT: [MASK0] is the democratic nominee and [MASK1] is the republican nominee
# OUTPUT:['Harris, Trump']

# INPUT: {masked_text}
# OUTPUT: '''
        
#         output = ragnews.rag(textprompt, db, keywords_text = masked_text)
#         print(output)
# import logging 
# logging.basicConfig(
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     level=logging.INFO
    
    #Next steps:
    # load labels from the file
    #create the RAGEvaluator passing in the labels 
    #then calculate the accuracy
    
    #reasons for bad results - 
    #1. the code (esp the prompt) in this function is bad - be sure the prompt explains the format of the output and examples of input/output pairs
    #2. the rag function itself could be bad
    # In order to improve 1 of the above problems, and prompt engineering does not work, we must change the model that we are using

from sklearn.metrics import accuracy_score

true_labels = ['Harris', 'Trump', 'Biden', 'Harris']
predicted_labels = ['Harris', 'Biden', 'Trump', 'Harris']

accuracy = accuracy_score(true_labels, predicted_labels)
print(f'Accuracy: {accuracy:.2f}')

