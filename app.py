import os
import streamlit as st
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Page configuration
st.set_page_config(
    page_title="Secure File Sharing System", page_icon="🔒", layout="centered"
)


def generate_key_file():
  return AESGCM.generate_key(bit_length=256)


def encrypt_file(file_data, key):
  aesgcm = AESGCM(key)
  nonce = os.urandom(12)
  encrypted_data = aesgcm.encrypt(nonce, file_data, None)
  return nonce + encrypted_data


def decrypt_file(token, key):
  aesgcm = AESGCM(key)
  nonce = token[:12]
  encrypted_data = token[12:]
  return aesgcm.decrypt(nonce, encrypted_data, None)


st.title("🔒 Secure File Sharing System")
st.write(
    "Encrypt files before transmission and decrypt them securely using AES"
    " encryption."
)

tabs = st.tabs(["Encrypt File", "Decrypt File"])

# TAB 1: ENCRYPT
with tabs[0]:
  st.header("Upload & Encrypt File")
  uploaded_file = st.file_uploader(
      "Choose a file to secure", type=None, key="encrypt_upload"
  )

  if uploaded_file is not None:
    file_bytes = uploaded_file.read()

    if st.button("Generate Key & Encrypt"):
      key = generate_key_file()
      encrypted_bytes = encrypt_file(file_bytes, key)

      st.success("File encrypted successfully!")

      st.download_button(
          label="Download Encrypted File (.enc)",
          data=encrypted_bytes,
          file_name=uploaded_file.name + ".enc",
          mime="application/octet-stream",
      )

      st.download_button(
          label="Download Secret Key (Keep Safe!)",
          data=key,
          file_name="secret.key",
          mime="application/octet-stream",
      )

# TAB 2: DECRYPT
with tabs[1]:
  st.header("Upload & Decrypt File")
  encrypted_upload = st.file_uploader(
      "Upload Encrypted File (.enc)", type=["enc"], key="decrypt_upload"
  )
  key_upload = st.file_uploader(
      "Upload Secret Key (.key)", type=["key"], key="key_upload"
  )

  if encrypted_upload is not None and key_upload is not None:
    enc_data = encrypted_upload.read()
    key_data = key_upload.read()

    if st.button("Decrypt File"):
      try:
        decrypted_bytes = decrypt_file(enc_data, key_data)
        original_filename = encrypted_upload.name.replace(".enc", "")

        st.success("File decrypted successfully!")
        st.download_button(
            label=f"Download Decrypted File ({original_filename})",
            data=decrypted_bytes,
            file_name=original_filename,
            mime="application/octet-stream",
        )
      except Exception as e:
        st.error(
            "❌ Decryption failed! Invalid key or corrupted file."
            f" Details: {str(e)}"
        )
