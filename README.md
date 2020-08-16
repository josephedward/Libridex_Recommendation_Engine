**Setup :**
*source ./local_init.sh*

**Test :**
visit https://gentle-tundra-97522.herokuapp.com/recommend/*YOUR_BOOK_HERE*/

*EX :*
'https://gentle-tundra-97522.herokuapp.com/recommend/Count of Monte Cristo/'

Returns JSON of recommendations based upon Cosine Similarity of TFIDF scores of book descriptions(provided this is a public-domain book that is in their library). Will be integrated as service into Node-React audiobook app @ https://morning-journey-07307.herokuapp.com/ Will improve model and documentation with time. Need to run scraper again. Many thanks to Librivox for not throttling my requests while scraping their entire API. 


https://en.wikipedia.org/wiki/Tf%E2%80%93idf

https://www.machinelearningplus.com/nlp/cosine-similarity/


