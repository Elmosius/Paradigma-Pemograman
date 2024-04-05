// File : TestLoopTryCatchFirst.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class TestLoopTryCatchFirst {
    public static void main(String[] args) {
        int i = 12;
        try
        {
            System.out.println("Masuk blok try");
            for(int j = 3; j >= -1 ; j--)
            {
                System.out.println("Masuk Loop " + "i = "+ i + " j = "+j);
                System.out.println(i/j); //Dibagi 0 - exception thrown
            }
            System.out.println("Mengakhiri blok try");
        }
        // Catch the exception
        catch(ArithmeticException e)
        {
            System.out.println("Arithmetic exception ditangkap");
        }
        System.out.println("Sesudah blok try");
    }
}
