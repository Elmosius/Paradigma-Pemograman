// File : TestTryCatch.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

public class TestTryCatch{
    public static void main(String[] args) {
        int i = 1;
        int j = 0;
        try
        {
            System.out.println("Masuk blok try untuk " + "i = "+
                                i + " j  = " + j );
            System.out.println(i / j); //Divide by 0 - exception thrown
            System.out.println("Mengakhiri blok try");
        }

        // Catch the exception
        catch(ArithmeticException e)
        {
            // ditangkep
            System.out.println("Arithmetic exception tertangkap");
        }
        System.out.println("Sesudah blok try");
    }
}