// File : CobaArrayStoreException.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaArrayStoreException {
    public static void main(String[] args) {
        try{
            Object x[] = new Integer[3];
            x[0] = new Integer(5);
            x[1] = new Float(3.14); //penyebab exception, hanya boleh tipe integer
        }
        catch(ArrayStoreException ex){
            System.out.println("ini di catch: Terjadi ArrayStoreException : ");
            System.out.println(ex);
            ex.printStackTrace();
    
        }
        finally{
            System.out.println("ini di finally");
        }   
    }
}
