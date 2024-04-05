// File : TryBlockTestFirst.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.io.IOException;

public class TryBlockTestFirst {
    public static void main(String[] args) throws IOException{
        int[] x = {10, 5, 0}; // Array dari tiga integer
        // Blok ini hanya akan melempar exception jika method divide()
        // melempar
        try{
            System.out.println("Pertama kali blok try di main() dimasuki");
            System.out.println("hasil = " + divide(x,0));  // No error
            x[1] = 0;  // Will cause a divide by zero
            // Arithmetic error
            System.out.println("hasil = " + divide(x,0));
            x[1] = 1;  // Reset nilai untuk mencegah pembagian dengan nol
            System.out.println("hasil = " + divide(x,1));  // Index error
        }
        catch(ArithmeticException e)
        {
            System.out.println("Arithmetic exception caught in main()");
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Index out of bounds exception tertangkap di main()");
        }
        System.out.println("pertama blok try di main()");
        System.out.println("\nPress Enter to exit");
    }
        // Divide method
        public static int divide(int[] array, int index) {
            try{
                System.out.println("\nPertama kali blok try di divide() dimasuki");
                array[index + 2] = array[index] / array[index + 1];
                System.out.println("Kode di akhir blok try di method divide()");
                return array[index + 2];
            }
            catch(ArithmeticException e){
                System.out.println("Arithmetic exception tertangkap di divide()");
            }
            catch(ArrayIndexOutOfBoundsException e)
            {
                System.out.println("Index-out-of-bounds exception tertangkap di divide()");
            }
            finally
            {
                System.out.println("finally block di divide()");
            }
            System.out.println("Mengeksekusi kode setelah blok try di divide()");
            return array[index + 2];
        }
}
