import streamlit as st
from pathlib import Path
import os
import shutil

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

        if not file_name.strip():
            st.warning("Please enter a file name.")

        else:
            p = Path(file_name)

            if p.exists():
                st.error("File already exists!")

            else:
                try:
                    with open(p, "w", encoding="utf-8") as file:
                        file.write(content)

                    st.success("File created successfully!")

                except Exception as e:
                    st.error(f"Error: {e}")

# ---------------- READ FILE ---------------- #

elif menu == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read"):

        p = Path(file_name)

        if p.exists() and p.is_file():

            try:
                with open(p, "r", encoding="utf-8") as file:
                    data = file.read()

                st.text_area("File Content", data, height=300)

            except Exception as e:
                st.error(f"Error reading file: {e}")

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

        if p.exists() and p.is_file():

            mode = "w" if update_type == "Overwrite" else "a"

            try:
                with open(p, mode, encoding="utf-8") as file:
                    file.write(content)

                st.success("File updated successfully!")

            except Exception as e:
                st.error(f"Error updating file: {e}")

        else:
            st.error("File does not exist!")

# ---------------- DELETE FILE ---------------- #

elif menu == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete"):

        p = Path(file_name)

        if p.exists() and p.is_file():

            try:
                os.remove(p)
                st.success("File deleted!")

            except Exception as e:
                st.error(f"Error deleting file: {e}")

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

            try:
                p.rename(new_name)
                st.success("File renamed!")

            except Exception as e:
                st.error(f"Error renaming file: {e}")

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
            try:
                p.mkdir(parents=True)
                st.success("Folder created!")

            except Exception as e:
                st.error(f"Error creating folder: {e}")

# ---------------- DELETE FOLDER ---------------- #

elif menu == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    delete_type = st.radio(
        "Delete Type",
        ["Empty Folder Only", "Delete Non-Empty Folder"]
    )

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists() and p.is_dir():

            try:
                if delete_type == "Empty Folder Only":
                    p.rmdir()
                else:
                    shutil.rmtree(p)

                st.success("Folder deleted!")

            except Exception as e:
                st.error(f"Error deleting folder: {e}")

        else:
            st.error("Folder not found!")