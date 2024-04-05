// File : ZeroDivideException.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class ZeroDivideException extends Exception {
  private int index = -1; // Index of array element causing error
    // Default Constructor
    
    public ZeroDivideException()
    {}

    // Standart constructor
    public ZeroDivideException(String s){
        super(s); // Call the base constructor
    }

    public ZeroDivideException(int index){
        super("/ by zero"); //Call the base constructor
        this.index = index; // Set the dindex value

    }

    // Get the array index value for the error
    public int getIndex(){
        return index; //Return the index value
    }
}
