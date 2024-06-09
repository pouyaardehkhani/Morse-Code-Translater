import streamlit as st

# Morse code dictionary for English and Persian characters
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',
}

# Reverse dictionary for decryption
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

# Function to encrypt the text
def encrypt(text):
    encrypted_text = ''
    for char in text.upper():
        if char in morse_code_dict:
            encrypted_text += morse_code_dict[char] + ' '
        else:
            encrypted_text += '? '  # Unknown character
    return encrypted_text.strip()

# Function to decrypt the text
def decrypt(morse_code):
    morse_words = morse_code.split(' / ')
    decrypted_text = ''
    for word in morse_words:
        for morse_char in word.split():
            if morse_char in reverse_morse_code_dict:
                decrypted_text += reverse_morse_code_dict[morse_char]
            else:
                decrypted_text += '?'  # Unknown morse code
        decrypted_text += ' '
    return decrypted_text.strip()

# Streamlit app
st.title("Morse Code Encrypter and Decrypter")
st.write("This app handles English alphabets.")

option = st.selectbox("Choose an option:", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    user_input = st.text_area("Enter text to encrypt (English or Persian):")
    if st.button("Encrypt"):
        result = encrypt(user_input)
        st.text_area("Encrypted Morse Code:", value=result, height=200)

elif option == "Decrypt":
    user_input = st.text_area("Enter Morse code to decrypt:")
    if st.button("Decrypt"):
        result = decrypt(user_input)
        st.text_area("Decrypted Text:", value=result, height=200)
