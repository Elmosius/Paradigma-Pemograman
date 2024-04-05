package Praktikum.P02;

// Accesor & Mutator (getter & setter method)
public class Kelas08 {
    private int age;

    public Kelas08(int age){   // konstuktor
        this.age = age;
    }

    public int getAge(){      // accessor / getter method
        return this.age;
    }

    public void setAge(int age){    // mutator / setter method
        this.age = age;
    } 

    public static void main(String[] args){
        Kelas08 k;
        k = new Kelas08(21);
        // meskipun age private, masih bisa karena main() berada dalam kelas yg sama

        System.out.println("Age: " + k.age);
        System.out.println("Age: " + k.getAge());   // berhasil, lewat accesor / getter
        k.setAge(17);                           // berhasil, lewat mutator / setter
        System.out.println("Age: " + k.getAge());
    }



}
