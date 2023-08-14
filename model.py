class PhoneBook :

    def __init__(self, path:str='phones.txt'):
        self.phone_book: list[dict[str,str]]= []
        self.path=path
        self.last_id=0

    def open(self):
        with open(self.path,'r' , encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact=contact.strip().split(':')
            self.phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})

    def save(self):
        data=[]
        for contact in self.phone_book:
            contact=':'.join(value for value in contact.values())
            data.append(contact)
        with open(self.path,'w', encoding='utf-8') as file:
            file.write('\n'.join(data))

    def load(self):
        return self.phone_book

    def add(self,new: dict[str,str])->str:
        self.last_id+=1
        new['id']=str(self.last_id)
        self.phone_book.append(new)
        return new.get('name')


    def del_contact(self,index : int):
        return self.phone_book.pop(index-1)

    def search(self, word:str)->list[dict[str,str]]:
        result:list[dict[str,str]]=[]
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result
    

    def change(self,new:dict, index:int)->str:
        for contact in self.phone_book:
            if index==contact.get('id'):
                contact['name']=new.get('name', contact.get('name'))
                contact['phone']=new.get('phone', contact.get('phone'))
                contact['comment']=new.get('comment', contact.get('comment'))
                return contact.get('name')