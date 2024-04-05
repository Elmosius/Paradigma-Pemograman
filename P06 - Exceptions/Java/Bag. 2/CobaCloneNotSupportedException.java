// File : CobaCloneNotSupportedException.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class CobaCloneNotSupportedException {
    public static void main(String[] args) {
        ToBeClone obj1 = new ToBeClone();
        ToBeClone obj2;

        try{
            obj2 = obj1.clone(); //membuat clone(kloning) dari objek tertentu
                                //exception terjadi jika kelas objek tsb tidak implements Cloneable
        }
        catch(CloneNotSupportedException ex){
            System.out.println("ini di catch : Terjadi CloneNotSupportedException : ");
            System.out.println(ex);
            ex.printStackTrace();
        }
        finally{
            System.out.println("ini di finally");
        }
    }
}

class ToBeClone /*implements Cloneable */{
    // jika komentar di atas dibuka, maka exception tidak akan terjadi
    public ToBeClone clone() throws CloneNotSupportedException {
        return (ToBeClone) super.clone();
    }

}