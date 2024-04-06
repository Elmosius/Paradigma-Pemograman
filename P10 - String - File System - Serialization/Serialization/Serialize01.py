# Serialize data list

import pickle
def main():
    data = [
            "sebuah list", "memiliki", 5, "item", 
            {"termasuk": ["str", "int", "dict"]} 
        
    ]
    print("data di tulis:\n", data)
    
    with open("pickled_list", 'wb') as file:
        pickle.dump(data, file)
        
    with open("pickled_list", 'rb') as file:
        loaded_data = pickle.load(file)
    print("data di baca:\n", loaded_data)
    
    assert loaded_data == data
if __name__ == "__main__":
    main()