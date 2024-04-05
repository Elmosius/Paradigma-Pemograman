// File : InheritingExceptions.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : Creating your own exceptions.

public class InheritingExceptions {
    public void f() throws SimpleException{
        System.out.println("Throw SimpleException from f()");
        throw new SimpleException();
    }
    public static void main(String[] args) {
        InheritingExceptions sed = new InheritingExceptions();
        try{
            sed.f();
        }catch(SimpleException e){
            System.out.println("Caught it");
        } 
    }
}

class SimpleException extends Exception{}