void main() {
  String str = "ABC";
  solve(str, 0, str.length() - 1);
}

void solve(String str, int l, int r) {
  if (l == r) {
    System.out.println(str);
  }
  else {
    for (int i = l; i <= r; i++) {
      str = swap(str, l, i);
      solve(str, l + 1, r);
      str = swap(str, l, i);
    }
  }
}

String swap(String str, int i, int j) {
  StringBuilder sb = new StringBuilder(str);
  sb.setCharAt(i, str.charAt(j));
  sb.setCharAt(j, str.charAt(i));
  return sb.toString();
}
