// File : TryBlockTestSecond.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.io.IOException;

public class TryBlockTestSecond {
    public static void main(String[] args) throws IOException {
        int[] x = {10, 5, 0}; // Array of three integers
         // This block only throws an exception if method divide() does

        try{
            System.out.println("result = " + divide(x,0)); // No error
            x[1] = 0; // Will cause a divide by zero
            // Arithmetic error
            System.out.println("result = " + divide(x,0));
            x[1] = 1;  // Reset to prevent divide by zero
            System.out.println("result = " + divide(x,1)); // Index error
         }
        catch(ArithmeticException e){
            System.out.println("Arithmetic exception caught in main()");
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Index-out-of-bounds exception caught in main()");
        }
        System.out.println("Outside first try block in main()");
        System.out.println("\nPress Enter to exit");
    }

    // Divide Method
    public static int divide(int[] array, int index){
        try{
            System.out.println("\nFirst try block in divide() entered");
            array[index + 2] = array[index]/array[index + 1];
            System.out.println("Code at end of first try block in divide()");
            return array[index + 2];
        }
        catch(ArithmeticException e){
            System.out.println("Arithmetic exception caught in divide()\n" +
                               "\nMessage in exception object:\n\t" + e.getMessage());
            System.out.println("\nStack trace output:\n");
            e.printStackTrace();
            System.out.println("\nEnd of stack trace output\n");
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Index-out-of-bounds exception caught in divide()\n" +
                                "\nMessage in exception object:\n\t" +e.getMessage());
            System.out.println("\nStack trace output:\n");
            e.printStackTrace();
            System.out.println("\nEnd of stack trace output\n");
        }
        finally{
            System.out.println("finally clause in divide()");
        }
        System.out.println("finally clause in divide()");
        return array[index + 2];
    }

}