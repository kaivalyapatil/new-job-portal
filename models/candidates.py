class Candidate:
    id:int =0
    first_name:str=""
    last_name:str=""
    birth_date:str=""
    email:str=""
    mobile:str=""
    address:str=""
    filename:str=""

    def __init__(self,id:int,
        first_name:str, last_name:str,birth_date:str,email:str,mobile:str,address:str,filename:str)->None:
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
        self.email=email
        self.mobile=mobile
        self.address=address
        self.filename=filename

    def serialize(self) -> any:
        return {
            'id':self.id,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'email':self.email,
            'mobile':self.mobile,
            'address':self.address,
            'birth_date':self.birth_date,
            'filename':self.filename
        }