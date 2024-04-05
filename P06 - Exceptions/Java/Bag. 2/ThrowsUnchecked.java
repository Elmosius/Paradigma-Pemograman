// File : ThrowsUnchecked.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : exception tidak ada yg menangani

public class ThrowsUnchecked {
    public static void main(String[] args) {
        new ThrowsUnchecked().doTheWork();
    }

    // memanggil method yg berbahaya tanpa melakukan pengecekan (try...catch)
    public void doTheWork(){
        String s = " 42";
        int i = testit(s); // no try/catch.
        System.out.println("paseit(" + s + ") returned " + i);
    }

    // method yg men-throw exception
    public int testit(String input) throws NumberFormatException {
        return Integer.parseInt(input);
    }
}
