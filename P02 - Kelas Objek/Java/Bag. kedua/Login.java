package Praktikum.P02;

import java.util.Scanner;

public class Login {
    private static String USERNAME = "elmo123"; 
    private static String PASSWORD = "elmo123"; 

    public static boolean login() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=======================");
        System.out.println("Silakan login:");

        System.out.print("Username: ");
        String username = scanner.nextLine();

        System.out.print("Password: ");
        String password = scanner.nextLine();
        System.out.println("=======================");

        if (USERNAME.equals(username) && PASSWORD.equals(password)) {
            System.out.println("Login berhasil. \n");
            return true;
        } else {
            System.out.println("Login gagal. Username atau password salah.");
            return false;
        }

    }
   
}
