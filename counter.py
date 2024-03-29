import streamlit as st

def count_lines(input_string):
    lines = input_string.split('\n')
    return len(lines)

def main():
    st.title('Hi, Ahemd add the code below')
    input_string = st.text_area('Enter your text here:')
    
    if st.button('Count Lines'):
        num_lines = count_lines(input_string)
        st.write(f'Number of lines: {num_lines}')

if __name__ == '__main__':
    main()