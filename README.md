![](https://github.com/aopsahl25/ragnews/workflows/tests/badge.svg)

```Ragnews``` runs an interactive question and answer system for news articles using the Groq LLM API and retrieval augmented generation (RAG). It works by fetching articles from a database and using them to answer questions from users about current-events. 

An exmaple of how this works is as follows:

```
$ python3 ragnews.py
>ragnews Who is the democratic presidential nominee?
The democratic presidential nominee is Kamala Harris.
```
We can also use the ```evaluate.py``` file in ```ragnews``` to evaluate the quality of our RAG system using the Hairy Trumpet dataset. An example of how this evaluation works is as follows: 
```
$ python3 ragnews/evaluate.py "hairy-trumpet/data/wiki__page=2024_United_States_presidential_election,recursive_depth=0__dpsize=paragraph,transformations=[canonicalize, group, rmtitles, split]"
predicted labels =  ['Biden', 'Harris', 'Walz', 'Biden, Trump', 'Trump', 'Vance', 'Trump', 'Trump', 'Biden', 'Trump', 'Trump', 'Trump', 'Biden', 'Trump', 'Trump', 'Biden', 'Biden', 'Trump', 'Trump, Trump', 'Biden', 'Harris', 'Trump', 'Biden', 'Trump', 'Trump, Trump, Trump', 'Trump', 'Trump', 'Trump, Trump, Trump, Trump', 'Trump', 'Biden', 'Biden', 'Biden, Biden, Biden', 'Trump', 'Trump, Trump, Trump', 'Biden', 'Biden', 'Trump', 'Biden', 'Trump', 'Harris', 'Trump', 'Biden', 'Trump', 'Biden', 'Trump', 'Biden', 'Harris', 'Trump', 'Trump', 'Trump', 'Harris', 'Trump, Trump', 'Trump', 'Trump', 'Trump', 'Harris', 'Biden', 'Trump', 'Trump', 'Biden', 'Trump, Trump, Trump, Trump, Trump', 'Trump', 'Harris', 'Biden', 'Harris', 'Harris', 'Biden', 'Harris', 'Trump', 'Biden', 'Trump, Trump, Trump, Trump, Trump, Trump, Trump, Trump', 'Biden', 'Harris', 'Harris', 'Harris', 'Biden', 'Trump', 'Biden', 'Trump', 'Biden', 'Biden', 'Biden', 'Trump, Trump', 'Biden', 'Trump', 'Harris', 'Trump', 'Biden', 'Biden, Biden', 'Harris', 'Biden', 'Biden', 'Biden', 'Biden, Biden', 'Trump', 'Harris', 'Harris', 'Harris', 'Harris, Harris', 'Biden', 'Trump', 'Biden', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump, Trump, Trump', 'Trump', 'Trump', 'Trump', 'Vance', 'Trump', 'Ware', 'Stein', 'Ware', 'Trump', 'Trump, Trump', 'Trump', 'Biden', 'Trump', 'Biden', 'Biden', 'Trump', 'Biden', 'Trump', 'Harris', 'Harris']
labels = ['Biden', 'Harris', 'Walz', 'Biden', 'Trump', 'Vance', 'Trump', 'Trump', 'Biden', 'Trump', 'Trump', 'Trump', 'Biden', 'Trump', 'Trump', 'Biden', 'Biden', 'Trump', 'Trump', 'Biden', 'Harris', 'Trump', 'Biden', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Biden', 'Biden', 'Trump', 'Trump', 'Trump', 'Trump', 'Biden', 'Trump', 'Biden', 'Trump', 'Harris', 'Trump', 'Biden', 'Trump', 'Harris', 'Trump', 'Harris', 'Harris', 'Trump', 'Trump', 'Biden', 'Harris', 'Trump', 'Trump', 'Trump', 'Trump', 'Harris', 'Biden', 'Trump', 'Trump', 'Biden', 'Trump', 'Trump', 'Harris', 'Biden', 'Harris', 'Harris', 'Biden', 'Harris', 'Trump', 'Harris', 'Trump', 'Biden', 'Trump', 'Harris', 'Harris', 'Biden', 'Trump', 'Biden', 'Trump', 'Biden', 'Harris', 'Biden', 'Trump', 'Harris', 'Trump', 'Harris', 'Trump', 'Biden', 'Biden', 'Harris', 'Biden', 'Biden', 'Biden', 'Biden', 'Trump', 'Harris', 'Biden', 'Walz', 'Harris', 'Walz', 'Trump', 'Biden', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Trump', 'Vance', 'Trump', 'Oliver', 'Stein', 'Ware', 'Trump', 'Biden', 'Trump', 'Harris', 'Trump', 'Biden', 'Biden', 'Trump', 'Harris', 'Trump', 'Vance', 'Walz']
2024-09-27 11:36:05 INFO     Accuracy: 0.76
```
