// File : CobaIllegalAccess.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaIllegalAccess {
    public static void main(String[] args) {
        System.out.println("Mencoba generate IllegalAccessException");
        try {
            throw new IllegalAccessException("Demo IllegalAccessException");
        } catch (IllegalAccessException e) {
            System.err.println("Terjadi IllegalAccessException: " + e.getMessage());
        }
    }
}

