int longestPrefixLength(String[] arr) {
    if (arr.length == 0) {
        return 0;
    }
    String max_prefix = arr[0];
    for (int i = 0; i < max_prefix.length(); i++) {
        char c = max_prefix.charAt(i);
        for (int j = 1; j < arr.length; j++) {
            if (i == arr[j].length() || arr[j].charAt(i) != c) {
                return i;  
            }
        }
    }
    return max_prefix.length();
}
