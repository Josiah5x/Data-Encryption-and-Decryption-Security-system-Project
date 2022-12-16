import dropbox
from dropbox.exceptions import AuthError
import pathlib
import pandas as pd

TOKEN = "sl.BS-ye15L41dTzqyaeW6BZsrP3rt5R5ECi6yo22RJ7s7dih9DSuRKBa9e11Nf01TANd5LFUXo1iFnbfsMNbxlU6a4f_8ng5D6vK2e1v-wqs20Rrdaq7jV3Bp6jtyoq9ib-5ZrXzs"


def connect_to_dropbox():
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print("Dropbox Connected")
    except AuthError as e:
        print(str(e))
    return dbx
# dbx = connect_to_dropbox()



def dropbox_list_files(path):
    """Return a Pandas dataframe of files in a given Dropbox folder path in the Apps directory.
    """

    dbx = connect_to_dropbox()

    try:
        files = dbx.files_list_folder(path).entries
        files_list = []
        for file in files:
            if isinstance(file, dropbox.files.FileMetadata):
                metadata = {
                    'name': file.name,
                    'path_display': file.path_display,
                    'client_modified': file.client_modified,
                    'server_modified': file.server_modified
                }
                files_list.append(metadata)

        df = pd.DataFrame.from_records(files_list)
        return df.sort_values(by='server_modified', ascending=False)

    except Exception as e:
        print('Error getting list of files from Dropbox: ' + str(e))