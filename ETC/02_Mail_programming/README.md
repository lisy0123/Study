# Mail programming

**[Mail programming](https://mailprogramming.com/)**(It's closed now) is a site that e-mail coding problems and detailed solutions every Monday morning. 

> :star: **Goal** :star:
>
> *Make same result, including special symbols.*

---
<details>
  <summary> :clipboard: Completed </summary>
  <div markdown="1">

<details>
  <summary> d01 </summary>
  <div markdown="1">

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

  </div>
</details>

<details>
  <summary> d02 </summary>
  <div markdown="1">

피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.

Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. Given an integer N, find the sum of all even fibonacci numbers.

> Input: N = 12
>
> Output: 10 
>
> // 0,1,2,3,5,8
>
> // even numbers 2 + 8 = 10

  </div>
</details>

<details>
  <summary> d03 </summary>
  <div markdown="1">

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

  </div>
</details>

<details>
  <summary> d04 </summary>
  <div markdown="1">

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

  </div>
</details>

<details>
  <summary> d05 </summary>
  <div markdown="1">

정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오. 단, 시간복잡도 O(n) 여야 합니다.

Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.

> Input: [2, 5, 6, 1, 10], 타겟 8
>
> Output: [0, 2] // 배열[0] + 배열[2] = 8

  </div>
</details>

<details>
  <summary> d06 </summary>
  <div markdown="1">

간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

Given a list of intervals, merge intersecting intervals.

> Input: {{2,4}, {1,5}, {7,9}}
>
> Output: {{1,5}, {7,9}}

> Input: {{3,6}, {1,3}, {2,4}}
>
> Output: {{1,6}}

  </div>
</details>

<details>
  <summary> d07 </summary>
  <div markdown="1">

주어진 string 에 모든 단어를 거꾸로 하시오.

Reverse all the words in the given string.

> Input: “abc 123 apple”
>
> Output: “cba 321 elppa”

  </div>
</details>

<details>
  <summary> d08 </summary>
  <div markdown="1">

정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

Given an integer array, find the second largest element.

> Input: [10, 5, 4, 3, -1]
>
> Output: 5

> Input: [3, 3, 3]
>
> Output: Does not exist.

  </div>
</details>

<details>
  <summary> d09 </summary>
  <div markdown="1">

정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.

> Input: [0, 5, 0, 3, -1]
>
> Output: [5, 3, -1, 0, 0]

> Input: [3, 0, 3]
>
> Output: [3, 3, 0]

  </div>
</details>

<details>
  <summary> d10 </summary>
  <div markdown="1">

String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오. 

Given a string, find the longest substring that does not have duplicate characters.

> Input: “aabcbcbc”
>
> Output: 3 // “abc”

> Input: “aaaaaaaa”
>
> Output: 1 // “a”

> Input: “abbbcedd”
>
> Output: 4 // “bced”

  </div>
</details>

<details>
  <summary> d13 </summary>
  <div markdown="1">

정수 배열(int array)과 정수 N이 주어지면, N번째로 큰 배열 원소를 찾으시오.

Given an integer array and integer N, find the Nth largest element in the array.

> Input: [-1, 3, -1, 5, 4], 2
>
> Output: 4

> Input: [2, 4, -2, -3, 8], 1
>
> Output: 8

> Input: [-5, -3, 1], 3
>
> Output: -5

  </div>
</details>

<details>
  <summary> d14 </summary>
  <div markdown="1">

문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

Given an array of strings, find the longest common prefix of all strings.

> Input: [“apple”, “apps”, “ape”]
>
> Output: 2 // “ap”

> Input: [“hawaii”, “happy”]
>
> Output: 2 // “ha”

> Input: [“dog”, “dogs”, “doge”]
>
> Output: 3 // “dog”

  </div>
</details>

<details>
  <summary> d22 </summary>
  <div markdown="1">

정렬(sort)된 정수 배열과 정수 n이 주어지면, 배열안에 n이 있는지 체크하시오. 시간복잡도를 최대한 최적화하시오.

Given a sorted integer array and an integer N, check if N exists in the array.

> Input: [1, 2, 3, 7, 10], 7
>
> Output: true

> Input: [-5, -3, 0, 1], 0
>
> Output: true

> Input: [1, 4, 5, 6, 8, 9], 10
>
> Output: false

  </div>
</details>

<details>
  <summary> d23 </summary>
  <div markdown="1">

정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.

Given an array and an integer K, shift all elements in the array K times.

> Input: [1, 2, 3, 4, 5], k = 2
>
> Output: [3, 4, 5, 1, 2]

> Input: [0, 1, 2, 3, 4], k = 1
>
> Output: [1, 2, 3, 4, 0]

시간복잡도와 공간복잡도를 최대한 최적화 하시오.

  </div>
</details>

  </div>
</details>

<details>
  <summary> :fountain_pen: In progress </summary>
  <div markdown="1">

<details>
  <summary> d11 </summary>
  <div markdown="1">

길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.

Given two strings of equal length, check if two strings can be encrypted 1 to 1.

> Input: “EGG”, “FOO”
>
> Output: True // E->F, G->O

> Input: “ABBCD”, “APPLE”
>
> Output: True // A->A, B->P, C->L, D->E

> Input: “AAB”, “FOO”
>
> Output: False

  </div>
</details>

<details>
  <summary> d12 </summary>
  <div markdown="1">

정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라. 단, 나누기 사용 금지, O(n) 시간복잡도

Given an integer array, make each element a product of all element values without itself.

> Input: [1, 2, 3, 4, 5]
>
> Output: [120, 60, 40, 30, 24]

  </div>
</details>

<details>
  <summary> d15 </summary>
  <div markdown="1">

링크드 리스트(linked list)의 머리 노드(head node)와 정수 N이 주어지면, 끝에서 N번째 노드(node)를 제거하고 머리 노드(head node)를 리턴하시오.

단, 리스트를 한번만 돌면서 풀어야합니다. N은 리스트 길이보다 크지 않습니다.

Given a head node of a singly linked list, remove the Nth last element and return the head node.

> Input: 1->2->3->4->5, N=2
>
> Output: 1->2->3->5

> Input: 1->2->3, N=3
>
> Output: 2->3

> Input: 1, N=1
>
> Output: null

  </div>
</details>

<details>
  <summary> d16 </summary>
  <div markdown="1">

두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.

Given two sorted integer linked lists, merge the two linked lists. Merged linked list must also be sorted.

> Input: 1->2->3, 1->2->3
>
> Output: 1->1->2->2->3->3

> Input: 1->3->5->6, 2->4
>
> Output: 1->2->3->4->5->6

  </div>
</details>

<details>
  <summary> d17 </summary>
  <div markdown="1">

0과 1로 만들어진 2D 정수 배열이 있습니다. 0은 장애물이고 1은 도로일때, 두 좌표가 주어지면, 첫번째 좌표에서 두번째 좌표까지 가장 가까운 거리를 구하시오. 두 좌표는 모두 도로에서 시작되고 좌, 우, 아래, 위로 움직이며 대각선으로는 움직일 수 없습니다. 만약 갈 수 없다면 -1을 리턴하시오.

Given a 2D array with 0s and 1s, 0 represents an obstacle and 1 represents a road. Find the closest distance between two given points. You must only move up down right left. You cannot move through an obstacle.

> Input:
>
> {{**1**, 0, 0, **1**, **1**, 0},
>
> {**1**, 0, 0, **1**, 0, 0},
>
> {**1**, **1**, **1**, **1**, 0, 0},
>
> {1, 0, 0, 0, 0, 1},
>
> {1, 1, 1, 1, 1, 1}}
>
> Start: (0, 0)
>
> Finish: (0, 4)
>
> 
>
> Output: 8

  </div>
</details>

<details>
  <summary> d18 </summary>
  <div markdown="1">

이진 트리를 루트 노드를 기준으로 좌우반전 하시오.

이 문제는 구글이 Homebrew 창시자에게 낸 문제로 유명합니다.

Given a binary tree root node, reverse the tree horizontally.

  </div>
</details>

<details>
  <summary> d19 </summary>
  <div markdown="1">

2차 정수 배열(2D int array)가 주어지면, 소용돌이 모양으로 원소들을 프린트하시오. 예제를 보시오.

Given a 2D integer array, print all elements in a circular spiral shape starting from [0][0]. See example.

> Input:
>
> [[1, 2, 3],
>
> [8, 9, 4],
>
> [7, 6, 5]]
>
> Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

  </div>
</details>

<details>
  <summary> d20 </summary>
  <div markdown="1">

정수 배열 arr이 있습니다. arr안의 각 원소의 값은 다음 원소의 인덱스입니다. 이렇게 서로 이어지는 원소들의 배열이 있을때, arr[0]부터 시작하여 모든 원소를 들린 다음 다시 arr[0]로 도착할 수 있는지 찾으시오.

단, 시간복잡도는 O(n), 공간복잡도는 O(1).

> Input: [1, 2, 4, 0, 3]
>
> Output: True
>
> // 1 -> 2 -> 4 -> 3 -> 0 -> 1

> Input: [1, 4, 5, 0, 3, 2]
>
> Output: False
>
> // 1 -> 4 -> 3 -> 0 -> 1
>
> // arr[2], arr[5]를 들리지 않았습니다.

> Input: [1, 2, 2, 0]
>
> Output: False
>
> // 1 -> 2 -> 2 -> 2 -> …
>
> // arr[0]로 돌아오지 못합니다.

  </div>
</details>

<details>
  <summary> d21 </summary>
  <div markdown="1">

O(n log n)시간 복잡도를 가진 정수 배열 정렬 알고리즘을 구현하시오.

Implement an O(n log n) time complexity sorting algorithm.

> Input: [3, 1, 5, 6]
>
> Output: [1, 3, 5, 6]

  </div>
</details>

<details>
  <summary> d24 </summary>
  <div markdown="1">

단방향 연결 리스트(Singly linked list)가 주어지면 O(n log n) 시간복잡도로 정렬하시오.

Given a singly linked list, sort the list in O(n log n) time complexity.

  </div>
</details>

<details>
  <summary> d25 </summary>
  <div markdown="1">

정렬된 정수 배열이 있습니다. 이 배열의 모든 원소들을 오른쪽으로 랜덤하게 Z번 이동하였습니다.

예를 들면 [1, 2, 3, 4, 5] -> [3, 4, 5, 1, 2].

이런 배열과 정수 K 가 주어지면, 배열안에 K가 존재하는지 찾으시오.

존재한다면 배열의 인덱스, 존재하지 않다면 -1 을 리턴하시오.

시간복잡도 제한 O(log N).

> Input: [3, 4, 5, 1, 2], 4
>
> Output: 1

> Input: [2, 4, 5, 1], 3
>
> Output: -1

> Input: [4, 6, 7, 8, 1, 2, 3], 5
>
> Output: -1

  </div>
</details>

<details>
  <summary> d26 </summary>
  <div markdown="1">

정수 배열이 주어지면 , 배열 안의 모든 정수의 최대 공약수(GCD)를 구하시오.

시간 복잡도 제한 O(n)

Given an integer array, find the greatest common denominator of all elements.

> Input: [3, 2, 1]
>
> Output: 1

> Input: [2, 4, 6, 8]
>
> Output: 2

  </div>
</details>

<details>
  <summary> d27 </summary>
  <div markdown="1">

"./"과 "../" 이 포함된 파일 경로를 "./"과 "../"이 없는 유닉스 파일 경로로 바꾸시오. "./"는 현재의 위치를 뜻하고, "../"는 상위 디렉토리를 뜻합니다.

Given a file path containing "./" and "../", convert the path to a unix standard file path that does not contain "./" and "../".

> Input: "/usr/bin/../"
>
> Output: "/usr/"

> Input: "/usr/./bin/./test/../"
>
> Output: "/usr/bin/"

  </div>
</details>

<details>
  <summary> d28 </summary>
  <div markdown="1">

정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오. 단, 시간복잡도는 O(n) 이여야 합니다.

Given an array of positive integers, find the smallest positive integer that cannot be created by adding elements in the array.

> Input: [1, 2, 3, 8]
>
> Output: 7
>
> // 1 = 1
>
> // 2 = 2
>
> // 3 = 3
>
> // 4 = 1 + 3
>
> // 5 = 2 + 3
>
> // 6 = 1 + 2 + 3
>
> // 7 = 불가능

  </div>
</details>

<details>
  <summary> d29 </summary>
  <div markdown="1">

반복된 알파벳으로 이루어진 문자배열이 주어지면 연속으로 중복된 알파벳이 없도록 문자배열을 재배열하여 리턴하시오. 불가능 하다면 empty string을 리턴하시오.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is impossible, return an empty string.

> Input: "aaabbc"
>
> Output: "ababac"

> Input: "aaac"
>
> Output: ""

  </div>
</details>

<details>
  <summary> d30 </summary>
  <div markdown="1">

주어진 정수를 2진법으로 나타내었을때 1의 갯수를 리턴하시오.

Given an integer, count number of 1s in binary representation of an integer.

시간 복잡도: O(log n)

> Input: 6 // 110
>
> Output: 2

> Input: 13 // 1101
>
> Output: 3

  </div>
</details>

<details>
  <summary> d31 </summary>
  <div markdown="1">

백만개의 정수가 들어있는 배열을 가장 빨리 정렬하시오. 모든 정수는 1조보다 작습니다.

힌트) 퀵소트 아님.

Sort an array with million integers.

  </div>
</details>

<details>
  <summary> d32 </summary>
  <div markdown="1">

이진 트리가 주어지면 루트 노드부터 레벨별로 프린트 하시오. 프린트 방식은 홀수 레벨은 왼쪽에서 오른쪽으로, 짝수 레벨은 오른쪽에서 왼쪽으로 프린트 하시오. 루트노드는 레벨 1입니다. 예제를 보시오.

> 1
>
> / \
>
> 2 3
>
> / \ / \
>
> 4 5 6 7
>
> 프린트: 1, 3, 2, 4, 5, 6, 7.

  </div>
</details>

<details>
  <summary> d33 </summary>
  <div markdown="1">

스택(Stack)을 이용해서 큐(Queue)를 구현하시오.

Implement a queue using stacks.

  </div>
</details>

<details>
  <summary> d34 </summary>
  <div markdown="1">

퀵정렬(quick sort)와 합병정렬(merge sort)이 차이점을 서술 하시오.

Describe differences between quick sort and merge sort.

  </div>
</details>

<details>
  <summary> d35 </summary>
  <div markdown="1">

중복된 원소가 없는 정렬된 배열이 있습니다. 이 배열에서 원소의 값이 원소의 인덱스 값과 같다면 프린트 하시오. 시간복잡도 O(log n).

Given a sorted array of unique values, find an element where its value is equal to the index.

> Input: [-30, 1, 4, 60]
>
> Output: 1 // input[1] = 1

> Input: [0, 3, 10, 60]
>
> Output: 0 // input[0] = 0

> Input: [-40, -30, -20, 3]
>
> Output: 3 // input[3] = 3

  </div>
</details>

<details>
  <summary> d36 </summary>
  <div markdown="1">

주어진 정수가 4의 거듭제곱인지 확인하시오.

Given an integer, check if it is a power of 4.

  </div>
</details>

<details>
  <summary> d37 </summary>
  <div markdown="1">

이진탐색트리안에 X보다 크고 Y보다 작은 모든 노드 값을 프린트 하시오.

Given a binary search tree, print all node values that are bigger than X and smaller than Y.

  </div>
</details>

<details>
  <summary> d38 </summary>
  <div markdown="1">

1~N 까지 있는 정수 배열에 원소 하나가 없어졌습니다. 없어진 원소의 값을 구하시오.

Given an integer array of 1~N except one number, find the missing integer.

  </div>
</details>

<details>
  <summary> d39 </summary>
  <div markdown="1">

단방향 연결 리스트(singly linked list)가 주어지면 총 합이 0으로 되는 연결된 노드들을 뺀 뒤 남은 노드의 값을 프린트 하시오.

Given a linked list, remove consecutive nodes that sum to zero. Print the values of leftover nodes.

> Input: 3 -> (-5) -> 5 -> 1 -> 2 -> 3
>
> Output: 3 -> 1 -> 2 -> 3

> Input: 1 -> 2 -> 3 -> 4 -> (-10) -> 5
>
> Output: 5

> Input: 10 -> (-3) -> (-4) -> (-3) -> 1
>
> Output: 1

  </div>
</details>

<details>
  <summary> d40 </summary>
  <div markdown="1">

"Look and say" sequence (보고 말하는 수열)은 다음과 같습니다.

1 - 1개의 1

11 - 2개의 1

21 - 1개의 2, 1개의 1

1211 - 1개의 1, 1개의 2, 2개의 1

111221 - ...

위와 같이 수열의 N 번째 수는 N-1번째 수의 조합을 풀어놓은 수 입니다. 정수 N이 주어졌을때, "Look and say" 수열의 N번째 수까지 프린트 하시오.

Given an integer N, print the first N numbers in "look and say" sequence.

  </div>
</details>

<details>
  <summary> d41 </summary>
  <div markdown="1">

정렬된 정수 배열이 주어지면, 발란스된 이진탐색트리로 바꾸시오.

Convert a given integer array into a balanced binary search tree.

  </div>
</details>

<details>
  <summary> d42 </summary>
  <div markdown="1">

이진트리안에 모든 단말노드(leaf node)의 갯수를 구하시오. 트리의 루트노드가 주어집니다.

Given a root node of a binary tree, count all leaf nodes.

  </div>
</details>

<details>
  <summary> d43 </summary>
  <div markdown="1">

이번주 문제는 인터뷰 팁입니다.

1. 문제의 가장 효율적인 답을 못찾겠을때 어떻게 해야하나요?
2. 문제를 받으면 바로 답변 코드를 종이에 적으면 되나요?
3. 답변은 무슨 언어로 쓰는게 제일 좋은가요?
4. 답변 코드를 쓴 후 코드를 어떻게 설명하나요?

  </div>
</details>

<details>
  <summary> d44 </summary>
  <div markdown="1">

정수 배열과 정수 K가 주어지면 원소 3개의 합으로 K가 만들어지는지 체크하시오.

Given an integer array and an integer K, check if sum of 3 elements from the array equals to K.

  </div>
</details>

<details>
  <summary> d45 </summary>
  <div markdown="1">

양수 K가 주어지면 K 길이의 이진법 숫자를 모두 프린트하시오. 단, 연속으로 1이 있으면 안됩니다.

Given an integer K, print all binary strings of length K without consecutive 1s.

> Input:5
>
> Output: 00000 00001 00010 00100 00101 01000 01001 01010 10000 10001 10010 10100 10101

  </div>
</details>

<details>
  <summary> d46 </summary>
  <div markdown="1">

문자배열이 주어지면, 주어진 문자로 만들수 있는 모든 문자배열 조합을 프린트 하시오.

Given a string, print all permutations of characters in the string.

> Input: ABC
>
> Output: ABC ACB BAC BCA CBA CAB

  </div>
</details>

<details>
  <summary> d47 </summary>
  <div markdown="1">

0, 1, 2로 이루어진 배열을 가장 효율적으로 정렬 하시오. 시간복잡도 O(n).

Given an array consisting of 0, 1 and 2s, sort this array.

> Input: [0, 1, 2, 2, 0, 0, 0, 1]
>
> Output: [0, 0, 0, 0, 1, 1, 2, 2]

  </div>
</details>

<details>
  <summary> d48 </summary>
  <div markdown="1">

단일 연결 리스트(singly linked list)가 주어지면 리스트의 중간 노드 값을 프린트 하시오. (제일 효율적인 방법으로)

Given a singly linked list, print the value of the node that is in the middle of the list.

  </div>
</details>

  </div>
</details>

[↩️ Go Back](https://github.com/lisy0123/Study/tree/master/ETC)

