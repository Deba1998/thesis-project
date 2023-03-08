import socket
from ftplib import FTP

def sendClientStatus(host,message):
    # host = "10.129.7.11"# as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    # message=["ExtractLogs",testName,str(numLinesExtract)]
    if message[0]=="ExtractLogs" or message[0]=="CloseFTPServer":
        message= ",".join(message)
        print(message)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        client_socket.close()  # close the connection
        return data
    else:
        print("No message Received at client check for errors")
        exit(1)

def ftpClient(host,testName):
    port=5001
    fileName = testName+".tar.gz"
    ftp = FTP()
    ftp.connect(host,port)
    ftp.login()
    ftp.retrbinary("RETR " +fileName,open(fileName,"wb").write)
    print("log files received")

def clientRun(testName,logHost,numLinesExtract):
    message = ["ExtractLogs",testName,str(numLinesExtract)]
    extractionStatus=sendClientStatus(logHost,message)
    if extractionStatus != "ExtractionComplete":
        print("Unable to Extract Logs")
        exit(1)
    print(extractionStatus)
    print("Fetching log files")
    ftpClient(logHost,testName)
    message=["CloseFTPServer"]
    FTPServerStatus=sendClientStatus(logHost,message)
    if  FTPServerStatus!= "FTPServerClosed":
        print("Unable to close FTP server")
        exit(1)
    print(FTPServerStatus)


if __name__ == '__main__':
    # logHost="127.0.0.1"
    # testName="XXXX"
    logHost="10.129.7.11"
    testName="8508a123f22114d0"
    numLinesExtract=50000 # change this in the future
    message = ["ExtractLogs",testName,str(numLinesExtract)]
    extractionStatus=sendClientStatus(logHost,message)
    if extractionStatus != "ExtractionComplete":
        print("Unable to Extract Logs")
        exit(1)
    print(extractionStatus)
    print("Fetching log files")
    ftpClient(logHost,testName)
    message=["CloseFTPServer"]
    FTPServerStatus=sendClientStatus(logHost,message)
    if  FTPServerStatus!= "FTPServerClosed":
        print("Unable to close FTP server")
        exit(1)
    print(FTPServerStatus)

    
