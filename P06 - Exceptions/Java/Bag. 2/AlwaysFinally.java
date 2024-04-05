// File : AlwaysFinally.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : Membuat ekception sendiri. Perhatikan bahwa finally selalu dieksekusi dulu
public class AlwaysFinally {
    public static void main(String[] args) {
        System.out.println("Memasuki blok try pertama");
        try {
            throw new FirstException("Eksepsi pertama");
        } catch (FirstException e) {
            System.out.println("FirstException tertangkap: " + e.getMessage());
        } finally {
            System.out.println("Blok finally pertama");
        }

        System.out.println("\nMemasuki blok try kedua");
        try {
            throw new SecondException("Eksepsi kedua");
        } catch (SecondException e) {
            System.out.println("SecondException tertangkap: " + e.getMessage());
        } finally {
            System.out.println("Blok finally kedua");
        }

        System.out.println("\nMemasuki blok try ketiga");
        try {
            throw new ThirdException("Eksepsi ketiga");
        } catch (ThirdException e) {
            System.out.println("ThirdException tertangkap: " + e.getMessage());
        } finally {
            System.out.println("Blok finally ketiga");
        }

        System.out.println("\nMemasuki blok try keempat");
        try {
            throw new FourthException("Eksepsi keempat");
        } catch (FourthException e) {
            System.out.println("FourthException tertangkap: " + e.getMessage());
        } finally {
            System.out.println("Blok finally keempat");
        }
    }
}

class FirstException extends Exception {
    public FirstException(String message) {
        super(message);
    }
}

class SecondException extends Exception {
    public SecondException(String message) {
        super(message);
    }
}

class ThirdException extends Exception {
    public ThirdException(String message) {
        super(message);
    }
}

class FourthException extends Exception {
    public FourthException(String message) {
        super(message);
    }
}

