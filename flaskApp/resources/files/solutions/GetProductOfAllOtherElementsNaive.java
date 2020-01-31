import java.util.Arrays;

public class GetProductOfAllOtherElementsNaive
{
    public static void main(String[] args) {
        //Recieves the method to use and the array of numbers as arguments from the terminal
        //Usage: java GetProductOfAllOtherElements --noDivision[--division] [numbers separated with space]
        int[] arr = new int[args.length];
        arr = getResult(args);
        System.out.println(Arrays.toString(arr));
    }
    //Utility function
    public static int[] getResult(String[] args)
    {
        int[] numbers;
        if(args[0].equals("--division"))
        {
            System.out.println("Using the naive division algorithm...");
            numbers = loadArgumentsIntoArray(args, 1, args.length);
            return getProductUsingDivision(numbers);
        }
        else if(args[0].equals("--noDivision"))
        {
            System.out.println("Not using the naive division algorithm");
            numbers = loadArgumentsIntoArray(args,1, args.length);
            return getProduct(numbers);
        }
        else
        {
            System.out.println("No algorithm mehod provided.");
            System.out.println("Using the naive division algorithm...");
            numbers = loadArgumentsIntoArray(args, 0, args.length);
            return getProductUsingDivision(numbers);
        }
    }
    //Utility function. Load the argument number passed in the terminal into the int array
    
    public static int[] loadArgumentsIntoArray(String[] args, int startIndex, int endIndex)
    {
        //@returns a new int array from startIndex to endIndex(not included) containing the numbers in args
        int[] res = new int[endIndex - startIndex];
        for(int i = startIndex; i < endIndex; i++)
        {
            res[i - startIndex] = Integer.parseInt(args[i]);
        }
        return res;
    }

    /*This way resolves the problem without using 
    division, but at the same time the time complexity increased; O(n*n)*/
    public static int[] getProduct(int[] array)
    {
        int[] product = new int[array.length];
        for(int i = 0; i < array.length; i++)
        {
            product[i] = 1;
            for(int j = 0; j < array.length; j++)
            {
                if(i == j)
                    continue;
                else
                    product[i] *= array[j];

            }
        }
        return product;
    }

    /*
    Another way to do this is by multiplying the whole list and then
    the i element in the result will be the division of the total product 
    and the i element in the list.
    Pros: O(n) time complexity
    Cons: Uses division
    */
    public static int[] getProductUsingDivision(int[] array)
    {
        int[] result = new int[array.length];
        int product = 1;
        for(int i: array)
            product *= i;
        for(int i = 0; i < array.length; i++)
            result[i] = product/array[i];
        return result;
    }
}