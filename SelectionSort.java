/**
 * This class is a Java implementation of Selection Sort.
 * Learned from <a href="https://www.geeksforgeeks.org/selection-sort/">...</a>
 */

public class SelectionSort {
  /**
   * This method performs in-place selection sort.
   * @param array is an array of integers
   */
  public static void selectionSort(int[] array) {
    int size = array.length;
    int smallest;
    for (int i = 0; i < size; i++) {
      smallest = array[i];
      for (int j = i + 1; j < size; j++) {
        if (array[j] < smallest) {
          smallest = array[j];
          int temp = array[i];
          array[i] = array[j];
          array[j] = temp;
        }
      }
    }

  }

  /**
   * The main method, consumes nothing, returns nothing.
   * @param args no arguments needed here
   */
  public static void main(String[] args) {
    int[] intArray = {1, 76, 5, 44, 208, 942};
    selectionSort(intArray);
    System.out.println("The sorted array is : ");
    for (int j : intArray) {
      System.out.print(j + " ");
    }
    System.out.println("\n");

    int[] intArray2 = {109, 76, 5, 44, 208, 942, 23, 5, 0, -2};
    selectionSort(intArray2);
    System.out.println("The sorted array is : ");
    for (int j : intArray2) {
      System.out.print(j + " ");
    }

    // I wonder how to write Unit test for this method...

  }
}