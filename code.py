#importing the required library to read the dicom files
import pydicom

def main():
    read_dicom_file()

def read_dicom_file():
    """
        Takes DICOM file as an input process it and then call the write
        function to store the required information.
    """
    path_dicom_file = input('Enter the path for the DICOM file')
    print(path_dicom_file)
    global datafile
    datafile = pydicom.dcmread(path_dicom_file)
    print('The files has been read now calling the write function to convert to text:')
    write_to_text()

def write_to_text():
    """
        Takes the tag names from the DICOM and store it in text format.
        Enter the path to store the text file, it opens the specific file
        and write the required information in the text form.
    """
    text_file_path = input('Enter the text file path')
    print(text_file_path)
    file = open(text_file_path,'w')
    data = datafile.dir()
    data_string = ','.join(data)
    file.write(data_string)
    file.close()
    print('The DICOM file has been read and the required tags are stored in the text file under this path\n',text_file_path)

if __name__ == "__main__":
    main()
