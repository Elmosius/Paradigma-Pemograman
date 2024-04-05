// File : CobaArrayIndexOutOfBounds.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaArrayIndexOutOfBounds {
    public static void main(String[] args) {
        try{
            int c[] = {1,3,5};
            System.out.println("Panjang array : " + c.length);
            System.out.println("Coba akses element ke 5 : " + c[5]);
            System.out.println("Ini setelah exception");

        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("array index out of bounds : " + e);
            e.printStackTrace();
        }
    }
}
