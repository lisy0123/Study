// solved in cs
public class Q3
{
	void	recurse(List<String> ans, String cur, int open, int close, int n)
	{
		if (cur.length() == n * 2)
		{
			ans.add(cur);
			return ;
		}
		if (open < n)
		{
			recurse(ans, cur + "(", open + 1, close, n);
		}
		if (close < open)
		{
			recurse(ans, cur + ")", open, close + 1, n);
		}
	}

	public static void main(String[] args)
	{
		Q3 q3 = new Q3();
		List<String> ans = new Q3();
		q3.solution3(ans, "", 0, 0, 2);
	}
}
