import java.util.Arrays;

/**
 * This class is a Java implementation of Bubble Sort.
 */

public class BubbleSort {
  /**
   * This method swaps two items in an array.
   *
   * @param array  an array of integers
   * @param index1 the index of the first item to be swapped
   * @param index2 the index of the second item to be swapped
   */
  public static void swap(int[] array, int index1, int index2) {
    int temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
  }

  /**
   * This is the method that sorts an array using bubble sort.
   *
   * @param array an array of integers to be sorted
   */
  public static void bubbleSort(int[] array) {
    for (int i = array.length - 1; i >= 1; i--) {
      for (int j = 0; j <= i - 1; j++) {
        if (array[j] > array[j + 1]) {
          swap(array, j, j + 1);
        }
      }
      /* verify by printing them */
      System.out.println("So far the array is:");
      System.out.print(Arrays.toString(array));
      System.out.println("\n");

    }
  }

  /**
   * The main method, consumes nothing, returns nothing.
   *
   * @param args no arguments needed here
   */
  public static void main(String[] args) {
    int[] intArray1 = {909, 76, -5, 434, 1208, -942, 23, 5, 0, -2};
    bubbleSort(intArray1);
    System.out.println("The sorted array is : ");
    for (int j : intArray1) {
      System.out.print(j + " ");
    }
    System.out.println();

    int[] intArray2 = {109, 76, 5, 44, 208, 942, 23, 5, 0, -2};
    bubbleSort(intArray2);
    System.out.println("The sorted array is : ");
    for (int j : intArray2) {
      System.out.print(j + " ");
    }
  }
}
