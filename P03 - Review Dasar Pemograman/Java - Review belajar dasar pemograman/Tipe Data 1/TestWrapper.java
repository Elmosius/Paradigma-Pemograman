package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;

// File : TestWrapper.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : mencoba wrapper class untuk semua tipe data primitif

public class TestWrapper {
    public static void main(String[] args) {
        byte p_byte         = 16;
        short p_short       = 127;
        int p_int           = 70000;
        long p_long         = 300000000;
        float p_float       = 3.14f;
        double p_double     = 77000000000.33;
        boolean p_boolean   = true;
        char p_char         = 'B';

        // cetak nilai di dalam variabel primitif
        System.out.println("\nNilai di dalam tipe data primitif : ");
        System.out.println("byte      : " + p_byte);
        System.out.println("short     : " + p_short);
        System.out.println("int       : " + p_int);
        System.out.println("long      : " + p_long);
        System.out.println("float     : " + p_float);
        System.out.println("double    : " + p_double);
        System.out.println("boolean   : " + p_boolean);
        System.out.println("char      : " + p_char);

        // masukkan ke dalam wrapper class (boxing)
        Byte       w_byte     = new Byte(p_byte);
        Short      w_short    = new Short(p_short);
        Integer    w_int      = new Integer(p_int);
        Long       w_long     = new Long(p_long);
        Float      w_float    = new Float(p_float);
        Double     w_double   = new Double(p_double);
        Boolean    w_boolean  = new Boolean(p_boolean);
        Character  w_char     = new Character(p_char);      
    
        // cetak nilai di dalam wrapper class
        System.out.println("\nNilai di dalam wrapper class : ");
        System.out.println("byte      : " + w_byte.byteValue());
        System.out.println("short     : " + w_short.shortValue());
        System.out.println("int       : " + w_int.intValue());
        System.out.println("long      : " + w_long.longValue());
        System.out.println("float     : " + w_float.floatValue());
        System.out.println("double    : " + w_double.doubleValue());
        System.out.println("boolean   : " + w_boolean.booleanValue());
        System.out.println("char      : " + w_char.charValue());

        // ambil nilai dari wrapper class (unboxing)
        byte       p2_byte     = w_byte.byteValue();
        short      p2_short    = w_short.shortValue();
        int        p2_int      = w_int.intValue();
        long       p2_long     = w_long.longValue();
        float      p2_float    = w_float.floatValue();
        double     p2_double   = w_double.doubleValue();
        boolean    p2_boolean  = w_boolean.booleanValue();
        char       p2_char     = w_char.charValue();  
    
        // cetak nilai di dalam wrapper class
        System.out.println("\nNilai di dalam tipe data primitif baru : ");
        System.out.println("byte      : " + p2_byte);
        System.out.println("short     : " + p2_short);
        System.out.println("int       : " + p2_int);
        System.out.println("long      : " + p2_long);
        System.out.println("float     : " + p2_float);
        System.out.println("double    : " + p2_double);
        System.out.println("boolean   : " + p2_boolean);
        System.out.println("char      : " + p2_char);
    
    }

}