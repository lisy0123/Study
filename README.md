# Mail programming

## :clipboard: [d01](https://github.com/lisy0123/Mail_Programming/tree/master/d01)

정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).

Given an inter array, find the largest consecutive sum of elements. 

> Input: -1, 3, -1, 5
>
> Output: 7
>
> // 3 + (-1) + 5

> Input: -5, -3, -1
>
> Output: -1 
>
> // -1

> Input: 2, 4, -2, -3, 8
>
> Output: 9 
>
> // 2 + 4 + (-2) + (-3) + 8

---

## :clipboard: [d02](https://github.com/lisy0123/Mail_Programming/tree/master/d02)

피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.

Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. Given an integer N, find the sum of all even fibonacci numbers.

> Input: N = 12
>
> Output: 10 
>
> // 0,1,2,3,5,8
>
> // even numbers 2 + 8 = 10

---

## [d03](https://github.com/lisy0123/Mail_Programming/tree/master/d03)

정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).

Given an inter N, find the number of possible balanced parentheses with N opening and closing brackets.

> Input: 1
>
> Ouput: ["()"]

> Input: 2
>
> Ouput: ["(())", "()()"]

> Input: 3
>
> Ouput: ["((()))", "(()())", "()(())", "(())()", "()()()"]

---

## [d04](https://github.com/lisy0123/Mail_Programming/tree/master/d04)

정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.

Given an integer, check if it is a palindrome.

> Input: 12345
>
> Output: False

> Input: -101
>
> Output: False

> Input: 11111
>
> Output: True

> Input: 12421
>
> Output: True

---

## [d05](https://github.com/lisy0123/Mail_Programming/tree/master/d05)

정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오. 단, 시간복잡도 O(n) 여야 합니다.

Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.

> Input: [2, 5, 6, 1, 10], 타겟 8
>
> Output: [0, 2] // 배열[0] + 배열[2] = 8

---

## [d06](https://github.com/lisy0123/Mail_Programming/tree/master/d06)

간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

Given a list of intervals, merge intersecting intervals.

> Input: {{2,4}, {1,5}, {7,9}}
>
> Output: {{1,5}, {7,9}}

> Input: {{3,6}, {1,3}, {2,4}}
>
> Output: {{1,6}}

---

## [d07](https://github.com/lisy0123/Mail_Programming/tree/master/d07)

주어진 string 에 모든 단어를 거꾸로 하시오.

Reverse all the words in the given string.

> Input: “abc 123 apple”
>
> Output: “cba 321 elppa”

---

## [d08](https://github.com/lisy0123/Mail_Programming/tree/master/d08)

정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

Given an integer array, find the second largest element.

> Input: [10, 5, 4, 3, -1]
>
> Output: 5

> Input: [3, 3, 3]
>
> Output: Does not exist.

----

## [d09](https://github.com/lisy0123/Mail_Programming/tree/master/d09)

정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.

> Input: [0, 5, 0, 3, -1]
>
> Output: [5, 3, -1, 0, 0]

> Input: [3, 0, 3]
>
> Output: [3, 3, 0]