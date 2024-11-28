def create_converter(tp):
    def converter(data):
        numbers = list(map(int, data.split()))
        
        if tp == 'list':
            return numbers
        else:
            return tuple(numbers)
    
    return converter
collection_type = input()  
data = input()            

converter_function = create_converter(collection_type)

lst = converter_function(data)

print(lst)
