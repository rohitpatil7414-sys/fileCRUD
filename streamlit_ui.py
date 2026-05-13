import streamlit_ui as st
from pathlib import Path
import os

st.title("📁 File Manager App")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# ---------------- CREATE FILE ---------------- #

if menu == "Create File":

    st.header("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create"):

        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("File created successfully!")

# ---------------- READ FILE ---------------- #

elif menu == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                data = file.read()

            st.text_area("File Content", data, height=300)

        else:
            st.error("File not found!")

# ---------------- UPDATE FILE ---------------- #

elif menu == "Update File":

    st.header("Update File")

    file_name = st.text_input("Enter file name")

    update_type = st.radio(
        "Choose Update Type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update"):

        p = Path(file_name)

        if p.exists():

            mode = 'w' if update_type == "Overwrite" else 'a'

            with open(file_name, mode) as file:
                file.write(content)

            st.success("File updated successfully!")

        else:
            st.error("File does not exist!")

# ---------------- DELETE FILE ---------------- #

elif menu == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete"):

        p = Path(file_name)

        if p.exists():
            os.remove(p)
            st.success("File deleted!")

        else:
            st.error("File not found!")

# ---------------- RENAME FILE ---------------- #

elif menu == "Rename File":

    st.header("Rename File")

    old_name = st.text_input("Enter old file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename"):

        p = Path(old_name)

        if p.exists():
            p.rename(new_name)
            st.success("File renamed!")

        else:
            st.error("File not found!")

# ---------------- CREATE FOLDER ---------------- #

elif menu == "Create Folder":

    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("Folder already exists!")

        else:
            p.mkdir()
            st.success("Folder created!")

# ---------------- DELETE FOLDER ---------------- #

elif menu == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():
            p.rmdir()
            st.success("Folder deleted!")

        else:
            st.error("Folder not found!")