import ftplib

def upload_file(ftp_server, username, password, local_file_path, remote_file_path):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(user=username, passwd=password)

        # Open the local file
        with open(local_file_path, 'rb') as file:
            # Upload the file to the remote server
            ftp.storbinary(f'STOR {remote_file_path}', file)

        print(f"File uploaded successfully to {ftp_server}")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

    finally:
        # Close the FTP connection
        ftp.quit()

# Example usage
ftp_server = 'ftp.example.com'
username = 'your_username'
password = 'your_password'
local_file_path = 'path/to/your/file.php'
remote_file_path = 'path/on/remote/server/index.php'

upload_file(ftp_server, username, password, local_file_path, remote_file_path)