# #Project - CRUD Operations
# """
# try
# except
# """
# from pathlib import Path
# import os #Operating System

# def readfileandfolder():
#         try:
#             p = Path('')
#             items = list(p.rglob('*'))
#             for index , file in enumerate(items):
#                 print(f'{index+1} - {file}')
#         except Exception as e:
#             print(e)


# def create_file():
#     try:
#         readfileandfolder()
#         # C:\Users\tanis\Desktop\File Handling\hello.txt
#         file_name = input('Enter name of your file: ')
#         p = Path(file_name)
#         if p.exists():
#             print('FILE ALREADY EXISTS')
#         else:
#             with open(file_name,'w') as file:
#                 content = input('Enter your file content: ')
#                 file.write(content)
#                 print('FILE ADDED!')
    
#     except Exception as e:
#         print(e)

# def read_file():
#     try:
#         readfileandfolder()
#         file_name = input('Enter name of your file: ')
#         p = Path(file_name)
#         if p.exists():
#             with open(file_name,'r') as file:
#                 print(file.read())
#         else:
#             print('FILE NOT FOUND!')
#     except Exception as e:
#         print(e)



# def update_file():
#     try:
#         readfileandfolder()
#         file_name = input('Enter name of your file: ')
#         p = Path(file_name)
#         if p.exists():
#             print('Press 1 to overwrite the content')
#             print('Press 2 to append new content')
            
#             option = int(input('Enter your choice for updating a file: '))
#             if option == 1:
#                 with open(file_name,'w') as file:
#                     content = input('Enter your content: ')
#                     file.write(content)
#                     print('CONTENT CHANGED...') 

#             elif option == 2:
#                 with open(file_name,'a') as file:
#                     content = input('Enter your content: ')
#                     file.write(content)
#                     print('CONTENT CHANGED...') 
            
#             else:
#                 print("INVALID INPUT")
#         else:
#             print("FILE DOES NOT EXISTS!")
    
#     except Exception as e:
#         print(e)

# def delete_file():
#     try:

#         readfileandfolder()
#         file_name = input('Enter name of your file: ')
#         p = Path(file_name)
#         if p.exists():
#             os.remove(p)
#             print("FILE DELETED")
#         else:
#             print('FILE DOES NOT EXISTS!!')
#     except Exception as e:
#         print(e)



# def rename_file():
#     try:
#         readfileandfolder()
#         file_name = input('enter name of your file:')
#         p = Path(file_name)
#         if p.exists():
#             new_file = input('enter new name of your file:')
#             p.rename(new_file)
#             print('FILE RENAME!')
#         else:
#             print('FILE NOT FOUND!')
#     except Exception as e:
#         print(e)


# def create_folder():
#     try:
#         readfileandfolder()
#         folder_name = input('enter name of your folder:')
#         p = Path(folder_name)
#         if p.exists():
#             print('FOLDER ALREADY EXISIS!')
#         else:
#             p.mkdir()
#             print('FOLDER CREATED!')

#     except Exception as e:
#         print(e)



# def delete_folder():
#     try:
#         readfileandfolder()
#         folder_name = input('enter name of your folder:')
#         p = Path(folder_name)
#         if p.exists():
#             p.rmdir()
#             print('FOLDER DElETED!')
#         else:
#             print('FOLDER NOT FOUND!')

#     except Exception as e:
#         print(e)


# def create_file_in_folder():
#     folder_name = input('enter name of your folder:')
#     file_name = input('enter name of your file:')
#     p = Path(folder_name/file_name)
#     if p.exists():
#         print('FILE ALREADY EXSIS!')
#     else:
#         pass

# while True:
#     print("Press 1 for creating a file")
#     print("Press 2 for reading a file")
#     print("Press 3 for updating a file")
#     print("Press 4 for deleting a file")
#     print("press 5 for renameing a file")
#     print("press 6 for creating a folder")
#     print("press 7 for deleting a folder")
#     print("Press 0 for exiting....")

#     option = int(input("Enter your choice: "))
#     if option ==1:
#         create_file()

#     if option ==2:
#         read_file()

#     if option == 3:
#         update_file()

#     if option == 4:
#         delete_file()
    
#     if option == 5:
#         rename_file()

#     if option == 6:
#         create_folder()

#     if option == 7:
#         delete_folder()

#     if option == 0:
#         break


# ==============================================================================








import streamlit as st
from pathlib import Path
import os

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="File Manager", page_icon="🗂️", layout="wide")

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sora:wght@400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Sora', sans-serif; }
    code, .stCode { font-family: 'JetBrains Mono', monospace; }

    .stApp { background: #0f1117; color: #e2e8f0; }

    .main-title {
        font-size: 2.4rem; font-weight: 700; letter-spacing: -1px;
        background: linear-gradient(135deg, #38bdf8, #818cf8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle { color: #64748b; font-size: 0.9rem; margin-bottom: 2rem; }

    .file-card {
        background: #1e2433; border: 1px solid #2d3748;
        border-radius: 10px; padding: 0.6rem 1rem;
        margin: 0.3rem 0; display: flex; align-items: center; gap: 0.6rem;
        font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #94a3b8;
    }
    .file-card .icon { font-size: 1rem; }
    .success-box {
        background: #052e16; border-left: 4px solid #22c55e;
        border-radius: 6px; padding: 0.7rem 1rem; color: #86efac;
        font-weight: 600; margin: 0.5rem 0;
    }
    .error-box {
        background: #2d0a0a; border-left: 4px solid #ef4444;
        border-radius: 6px; padding: 0.7rem 1rem; color: #fca5a5;
        font-weight: 600; margin: 0.5rem 0;
    }
    .info-box {
        background: #0c1a2e; border-left: 4px solid #38bdf8;
        border-radius: 6px; padding: 0.7rem 1rem; color: #7dd3fc;
        margin: 0.5rem 0;
    }
    .content-display {
        background: #0d1117; border: 1px solid #2d3748; border-radius: 8px;
        padding: 1rem; font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem; color: #a5f3fc; white-space: pre-wrap;
        min-height: 80px; margin: 0.5rem 0;
    }
    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextInput"] label,
    div[data-testid="stTextArea"] label { color: #94a3b8 !important; font-weight: 600; font-size: 0.85rem; }
    .stButton > button {
        background: linear-gradient(135deg, #38bdf8, #818cf8);
        color: #0f1117; border: none; border-radius: 8px;
        font-weight: 700; font-size: 0.9rem; padding: 0.5rem 1.5rem;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.85; }
    .stRadio > label { color: #94a3b8 !important; }
    .section-header {
        color: #818cf8; font-weight: 700; font-size: 1rem;
        border-bottom: 1px solid #2d3748; padding-bottom: 0.4rem; margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# ─── Helpers ────────────────────────────────────────────────────────────────
def get_all_items():
    p = Path('')
    return list(p.rglob('*'))

def success(msg): st.markdown(f'<div class="success-box">✅ {msg}</div>', unsafe_allow_html=True)
def error(msg):   st.markdown(f'<div class="error-box">❌ {msg}</div>', unsafe_allow_html=True)
def info(msg):    st.markdown(f'<div class="info-box">ℹ️ {msg}</div>', unsafe_allow_html=True)

def show_file_browser():
    items = get_all_items()
    if not items:
        info("No files or folders found in the current directory.")
        return
    st.markdown('<div class="section-header">📁 Current Directory Contents</div>', unsafe_allow_html=True)
    for item in items:
        icon = "📁" if item.is_dir() else "📄"
        st.markdown(f'<div class="file-card"><span class="icon">{icon}</span>{item}</div>', unsafe_allow_html=True)


# ─── Header ─────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🗂️ File Manager</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">CRUD Operations · Files & Folders</div>', unsafe_allow_html=True)

col_main, col_browser = st.columns([3, 2], gap="large")

# ─── Right Panel: File Browser ───────────────────────────────────────────────
with col_browser:
    st.markdown('<div class="section-header">📂 File Browser</div>', unsafe_allow_html=True)
    if st.button("🔄 Refresh", key="refresh"):
        st.rerun()
    show_file_browser()

# ─── Left Panel: Operations ──────────────────────────────────────────────────
with col_main:
    operation = st.selectbox(
        "Choose Operation",
        ["➕ Create File", "📖 Read File", "✏️ Update File",
         "🗑️ Delete File", "🔁 Rename File",
         "📁 Create Folder", "🗑️ Delete Folder"],
        label_visibility="visible"
    )

    st.markdown("---")

    # ── Create File ──────────────────────────────────────────────────────────
    if operation == "➕ Create File":
        st.markdown('<div class="section-header">Create a New File</div>', unsafe_allow_html=True)
        file_name = st.text_input("File name (e.g. notes.txt)")
        content   = st.text_area("File content", height=150)
        if st.button("Create File"):
            if not file_name.strip():
                error("Please enter a file name.")
            else:
                p = Path(file_name)
                if p.exists():
                    error("FILE ALREADY EXISTS")
                else:
                    try:
                        with open(file_name, 'w') as f:
                            f.write(content)
                        success(f'"{file_name}" created successfully!')
                    except Exception as e:
                        error(str(e))

    # ── Read File ─────────────────────────────────────────────────────────────
    elif operation == "📖 Read File":
        st.markdown('<div class="section-header">Read a File</div>', unsafe_allow_html=True)
        file_name = st.text_input("File name to read")
        if st.button("Read File"):
            if not file_name.strip():
                error("Please enter a file name.")
            else:
                p = Path(file_name)
                if p.exists():
                    try:
                        with open(file_name, 'r') as f:
                            content = f.read()
                        st.markdown('<div class="section-header">File Contents</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="content-display">{content if content else "(empty file)"}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        error(str(e))
                else:
                    error("FILE NOT FOUND!")

    # ── Update File ───────────────────────────────────────────────────────────
    elif operation == "✏️ Update File":
        st.markdown('<div class="section-header">Update a File</div>', unsafe_allow_html=True)
        file_name = st.text_input("File name to update")
        mode      = st.radio("Update mode", ["Overwrite", "Append"], horizontal=True)
        new_content = st.text_area("New content", height=150)
        if st.button("Update File"):
            if not file_name.strip():
                error("Please enter a file name.")
            else:
                p = Path(file_name)
                if p.exists():
                    try:
                        write_mode = 'w' if mode == "Overwrite" else 'a'
                        with open(file_name, write_mode) as f:
                            f.write(new_content)
                        success(f'"{file_name}" updated successfully!')
                    except Exception as e:
                        error(str(e))
                else:
                    error("FILE DOES NOT EXIST!")

    # ── Delete File ───────────────────────────────────────────────────────────
    elif operation == "🗑️ Delete File":
        st.markdown('<div class="section-header">Delete a File</div>', unsafe_allow_html=True)
        file_name = st.text_input("File name to delete")
        confirm   = st.checkbox("I confirm I want to delete this file")
        if st.button("Delete File"):
            if not file_name.strip():
                error("Please enter a file name.")
            elif not confirm:
                info("Please check the confirmation box first.")
            else:
                p = Path(file_name)
                if p.exists():
                    try:
                        os.remove(p)
                        success(f'"{file_name}" deleted successfully!')
                    except Exception as e:
                        error(str(e))
                else:
                    error("FILE DOES NOT EXIST!")

    # ── Rename File ───────────────────────────────────────────────────────────
    elif operation == "🔁 Rename File":
        st.markdown('<div class="section-header">Rename a File</div>', unsafe_allow_html=True)
        file_name     = st.text_input("Current file name")
        new_file_name = st.text_input("New file name")
        if st.button("Rename File"):
            if not file_name.strip() or not new_file_name.strip():
                error("Please fill in both fields.")
            else:
                p = Path(file_name)
                if p.exists():
                    try:
                        p.rename(new_file_name)
                        success(f'"{file_name}" renamed to "{new_file_name}"!')
                    except Exception as e:
                        error(str(e))
                else:
                    error("FILE NOT FOUND!")

    # ── Create Folder ─────────────────────────────────────────────────────────
    elif operation == "📁 Create Folder":
        st.markdown('<div class="section-header">Create a New Folder</div>', unsafe_allow_html=True)
        folder_name = st.text_input("Folder name")
        if st.button("Create Folder"):
            if not folder_name.strip():
                error("Please enter a folder name.")
            else:
                p = Path(folder_name)
                if p.exists():
                    error("FOLDER ALREADY EXISTS!")
                else:
                    try:
                        p.mkdir()
                        success(f'Folder "{folder_name}" created!')
                    except Exception as e:
                        error(str(e))

    # ── Delete Folder ─────────────────────────────────────────────────────────
    elif operation == "🗑️ Delete Folder":
        st.markdown('<div class="section-header">Delete a Folder</div>', unsafe_allow_html=True)
        folder_name = st.text_input("Folder name to delete")
        confirm     = st.checkbox("I confirm I want to delete this folder")
        if st.button("Delete Folder"):
            if not folder_name.strip():
                error("Please enter a folder name.")
            elif not confirm:
                info("Please check the confirmation box first.")
            else:
                p = Path(folder_name)
                if p.exists():
                    try:
                        p.rmdir()
                        success(f'Folder "{folder_name}" deleted!')
                    except Exception as e:
                        error(str(e))
                else:
                    error("FOLDER NOT FOUND!") 
                    
