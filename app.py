import streamlit as st
import pandas as pd

from txtai import Embeddings


embeddings = Embeddings()
embeddings.load("av-strip")

st.header(':blue[Semantic KJV Bible Search]')
st.subheader('Search the *King James Bible* in a New Way!', divider=True)
#st.subheader('Prototype', divider=True)

c1, c2 = st.columns([0.8, 0.2])
with c1: 
	query = st.text_input('Enter a word or phrase:')
with c2: 
	limit = st.text_input('Result Limit', value="5")
	
if query:	
	hits = embeddings.search("""select text, ref, score from txtai where similar('%s')""" % query, int(limit))

	df = pd.DataFrame(hits)
	# To sort columns
	df = df[['ref', 'text', 'score']]
	df.columns = ['Ref','Text', 'Score']

	cols = list(df.columns.values)

	st.dataframe(df, width = 800)

st.write(':blue-background[*(Double-click a cell to view entire verse)*]')

st.write("""Unlike a *Keyword Search* where specific words are searched for, *Semantic Search* is a search technology that interprets the *meaning* of words and phrases. It is a search based on *intent* rather than exact matches and is also known as *Natural Language Search*.  
  
Semantic search is powered by a mathematical *vector search* which enables it to deliver and rank content based on context and intent relevance. For this page the entire text of the King James Bible was vectored and each word and passage given a ranking based on the data of a pre-trained language model. When a query is entered above it is also vectored and then mathematically matched to the closest vectors of the KJV data. The score listed in the results reflect the strength of the similarity.""")

st.write(":blue-background[This app is a prototype to test semantic search of the Bible.]")