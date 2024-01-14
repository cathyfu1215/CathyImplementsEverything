
/** A Java implementation of binary search. */
public class Main {

  /**
   * Run binary search on a given integer list.
   * @param  list of integers
   * @param  item int item to find
   * @return the index of the item if found, -1 if not found
   */
  public static int binarySearch(int[] list, int item) {

    int low = 0;
    int high = list.length - 1;
    int mid;

    while (low <= high) {

      mid = ((high + low) / 2);
      int guess = list[mid];
      if (guess == item) {
        return mid;
      } else {
        if (guess < item) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

    }
    return -1;
  }

  /**
   The main function. Actually I should write JUnit test?
   @param args no parameters needed
   */
  public static void main(String[] args) {

    int[] listOfNumbers = {1, 2, 3, 5, 8, 13};
    System.out.println(binarySearch(listOfNumbers, 5)); // should be 3
    System.out.println(binarySearch(listOfNumbers, -5)); // should be -1
    System.out.println(binarySearch(listOfNumbers, 13)); // should be 5
    System.out.println(binarySearch(listOfNumbers, 1)); // should be 0

  }
}