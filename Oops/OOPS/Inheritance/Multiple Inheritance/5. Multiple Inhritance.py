class Cars:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def show_name(self):
        return self.name
    
    def show_model(self):
        return self.model
    

class ids:
    def __init__(self,id):
        self.id=id

    def show_id(self):
        return self.id
    


class Main(Cars,ids):
    def __init__(self,name,model,id):
     Cars.__init__(self,name,model)
     ids.__init__(self,id)



a=Main("Swift","swift desire",123333)
print(a.show_name())
print(a.show_model())
print(a.show_id())
