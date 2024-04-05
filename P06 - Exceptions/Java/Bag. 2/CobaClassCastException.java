// File : CobaClassCastException.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaClassCastException {
    public static void main(String[] args) {
        try{
            Object x = new Integer(0);
            System.out.println((String) x);
        }
        catch(ClassCastException ex){
            System.out.println("ini di catch : Terjadi ClassCastException : ");
            System.out.println(ex);
            ex.printStackTrace();
        }
        finally{
            System.out.println("ini di finally");
        }
    }
}
