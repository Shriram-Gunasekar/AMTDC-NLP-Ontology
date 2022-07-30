# NLP Data Classes

class Holder:
    class Full:
        def __init__(self, catalog_number, order_number):
            self.data = catalog_number
            self.data = order_number
    class Coating:
        def __init__(self, group, subgroup, subdetail):
            self.group = group
            self.subgroup = subgroup
            self.subdetail = subdetail

    class Material:
        def __init__(self, material, description):
            self.material = material
            self.description = description
    
    class NameGrade :
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

class Insert:
    class Full:
        def __init__(self, catalog_number, order_number):
            self.data = catalog_number
            self.data = order_number
    class Coating:
        def __init__(self, group, subgroup, subdetail):
            self.group = group
            self.subgroup = subgroup
            self.subdetail = subdetail

    class Material:
        def __init__(self, material, description):
            self.material = material
            self.description = description
    
    class NameGrade :
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

def getquery():
    query = input("Use as many identifiers as possible and enter the query: ")
    return query


            

