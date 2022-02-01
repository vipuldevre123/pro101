import dropbox

class Transfer:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def upload(self,filefrom,fileto):
        d=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,'rb')
        d.files_upload(f.read(),fileto)

#creating object of class
accesstoken="sl.BBL2wZlIrx3MKvdsEiSjHCBWj_4wif3LXVhJwFbg3bsl0NWP0ek_kARyykEt3D1nnVJYrcJ0yOwkRMu00BTO6ftELDQirnP9C5ywyb5bEzB5ERCGc7s1ut_hdESgE5vA8tJo6xEDXMM"
t=Transfer(accesstoken)  
filefrom=input("Enter the file path to transfer")   
fileto=input("Enter the full path to upload in dropbox")   
t.upload(filefrom,fileto)
print("files are uploaded")
