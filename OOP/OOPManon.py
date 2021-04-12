class Books:

    def __init__(self,title,author):
        self.title=title
        self.author=author
        
    def getTitle(self):
        return self.name
    
    def getAuthor(self):
        return self.author
    
    def lotsOfPages(self):
        print("This book is huge !")

class Novels(Books):
    
    def __init__(self,title,author,protagonist,language):
        super().__init__(self,title,author)
        self.protagonist=protagonist
        self.language=language
    
    def summary(self):
        print("The main character in"+ self.getTitle() + "is" + self.protagonist+".")
        
    def thrilling(self):
        print("This book is thrilling !")
    
    def language(self):
        print("This book is in"+self.language)
        
    
class Theater(Books):
    
    def __init__(self,title,author,acts,year):
        super().__init__(self,title,author)
        self.acts=acts
        self.year=year
    
    def representation(director,theatre):
        print("This theatre piece written in" + self.year+ "by" +self.getAuthor()+"is performed at the" + theatre + "and is directed by" + director)
        
    def adaptation(year,author):
        print("In"+year+","+author+"adapted the theater piece of "+self.getAuthor())
        self.author=author
        self.year=year
    
book1= Novels("The Testaments","Margaret Atwood","Aunt Lydia","English")
book2= Theater("Fin de Partie", "Samuel Beckett",1,1957)
    
    