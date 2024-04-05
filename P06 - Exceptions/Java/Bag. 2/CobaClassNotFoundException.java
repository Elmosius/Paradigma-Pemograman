// File : CobaClassNotFoundException.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaClassNotFoundException {
    public static void main(String[] args) {
        try{
            Object x = new Integer(0);
            Class t = Class.forName("KelasKU"); //mengambil objek dari kelas tertentu
                                               //penyebab exception, jika kelas tsb tidak ada
        }
        catch(ClassNotFoundException ex){
            System.out.println("ini di catch : Terjadi ClassNotFoundException : ");
            System.out.println(ex);
            ex.printStackTrace();
        } 
        finally{
            System.out.println("ini di finally");
        }
    }
}
