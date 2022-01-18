void rotate(int[] arr, int k) {
  int n = arr.length;
  k %= n;
  reverse(arr, 0, k-1);
  reverse(arr, k, n-1);
  reverse(arr, 0, n-1);
}

void reverse(int[] nums, int start, int end) {
  while (start < end) {
    int temp = nums[start];
    nums[start] = nums[end];
    nums[end] = temp;
    start++;
    end--;
  }
}
