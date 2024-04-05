// File : ExceptionSilencer.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class ExceptionSilencer {
    public static void main(String[] args) {
        try {
            throw new RuntimeException();
        }finally {
            // Using 'return' inside the finally block
            // will silence any thrown exception.
            return;
        }
    }
}
