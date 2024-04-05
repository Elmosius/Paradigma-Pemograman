# Exception
class Numbers:
    def __init__(self) -> None:
        self.__nums: list[int] = [0,1,2,3,4]
        
    def get(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.__nums):
            raise Exception("Index out of range")
        return self.__nums[idx]
        
        
def main():
    nums = Numbers()
    try:
        val = nums.get(8)
        print(val)
    except Exception as e:
        print("Masalah index: " + e.__str__())

    
if __name__ == "__main__":
    main( )  
        