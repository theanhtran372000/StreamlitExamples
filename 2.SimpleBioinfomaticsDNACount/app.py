from turtle import width
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

##############
# INPUT TEXT #
##############

st.header('Enter DNA sequence')


sequence_input = '>DNA Query\n' + 'GATAGCATA' * 20

sequence = st.text_area('Sequence input', sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skip the first line
sequence = ''.join(sequence)

st.write("""
***
""")

### Print the input sequence
st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    
    return  d

X = DNA_nucleotide_count(seq=sequence)

X_label = list(X)
X_value = list(X.values())

X

### 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine')
st.write('There are ' + str(X['T']) + ' thymine')
st.write('There are ' + str(X['G']) + ' guanine')
st.write('There are ' + str(X['C']) + ' cytosine')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# ### 4. Display bar chart
# st.subheader('4. Display bar chart')
# p = alt.Chart(df).mark_bar().encode(
#     X='nucleotide',
#     Y='count'
# )

# p = p.properties(
#     width=alt.Step(80)
# )

# st.write(p)

