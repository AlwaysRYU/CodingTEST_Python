public class employee{
    // public static int modify(int k){
    //    k += 10;
    //     return k;

    // }
    class product{
        void info() {
            System.out.println("dkdk");
        }
    }
    class TV extends product {
        void info() {
            product.info();
            System.out.println("gngn");
        }
    }
    // String name = "Hello~~    ";
    // public String toString(){return name;}
    public static void main(String args[]){
        TV a = new TV();
        boolean bb = a.info();
        System.out.print(bb);

    }
}
