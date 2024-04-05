package Praktikum.P02;

import java.time.LocalDate;

// Behaviout / method & pembuatan objek
public class Kelas09 {
    private int age;

    public Kelas09(int age){   // konstuktor
        this.age = age;
    }

    public int computeYob(){
        LocalDate now = LocalDate.now();
        return now.getYear() - this.age;
    }

    public int getAge(){      // accessor / getter method
        return this.age;
    }

    public void setAge(int age){    // mutator / setter method
        this.age = age;
    } 

    public static void main(String[] args){
        Kelas09 k;
        k = new Kelas09(21);     // membuat objek k dari kelas Kelas09
        System.out.println("Age: " + k.getAge());   // berhasil, lewat accesor / getter
        System.out.println("Tahun lahir: " + k.computeYob());   
        k.setAge(17);                           // berhasil, lewat mutator / setter
        System.out.println("Age: " + k.getAge());
        System.out.println("Tahun lahir: " + k.computeYob());   
    }



}
