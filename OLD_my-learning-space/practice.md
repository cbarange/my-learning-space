# Some practice for IT
> cbarange | 16th December 2020
---

### TODO
* algo → Backpack
* algo → Rendu monnaie
* algo → Even sum & odd sum (for(i<N)i%2==N%2?res+=i:undefined print(res))
* algo → Screen Diagonal by Sides (L=int,H=int,Ratio={16:4,4:6,4:3}, print diagonal)
* algo → Dérivation d'un polynôme

#### Problème du voyageur de commerce

La donnée du problème est un ensemble de villes et de distances séparant ces villes. L'objectif du problème est de trouver un plus court circuit qui passe une et une seule fois par toutes les villes. Il existe un problème de décision associé : étant donné un ensemble de villes, les distances entre villes et un entier k, déterminer s'il existe un circuit qui passe une et une seule fois par toutes les villes de longueur inférieure à k. Ainsi, on distingue deux types de problèmes :

Entrée : 
Sortie : 
1. (Problème de décision) Existe-il oui ou non un circuit de longueur inférieure à k ?
2. (Problème de recherche d'une solution) Renvoyer une liste de ville triée tel que cette liste représente l'odre dans lequel il faut visité les villes pour faire le plus court chemin.
3. Déternimer la classe de complexité des questions 1 et 2
4. Donner la complexité algorithmique des questions 1 et 2

#### Mémoïsation & Fibonacci

Entrée : Entier N
Sortie : Fibonacci(N)
1. Ecriver un programme qui calcule la suite de fibonacci pour N
2. Ecriver ce même programme en utilisant la mémoisation, avec une table et sans table(récursivité terminale)
3. Déternimer la complexité algorithmique des questions 1 et 2

#### Programmation dynamique, Pyramide de nombres
> lvl3 google interview
Entrée :  Une pyramide de nombre 
Sortie :  Somme maximale possible en ce déplacant en diagonal vers le bas.
```
   3
  7 4
 2 4 6
9 5 9 3
```

1. Proposer une solution naive
2. Proposer une solution en PD (Programmation Dynamique)
3. Déternimer la complexité algorithmique des questions 1 et 2


## Tag

**Difficulty tag**

|level tag|rank|time|
|:--|:--|--:|
|lvl1|Newby|5'|
|lvl2|Amateur|10'|
|lvl3|Junior|10'|
|lvl4|Common|15'|
|lvl5|Experimented|20'|
|lvl6|Expert|30'|
|lvl7|Legendary|30'+|
> Why 7 levels → because most of ctf challenges contains 7 challenges which levels increases

**Common tag**

|tag|comment|
|:--|:--|
|UNSOLVED|Unsolved challenge, I'm working on|
|algo|Challenge for algorithms logic|
|google|Challenge from google|
|interview|Challenge asked during a job interview|
|codingame|Challenge from [codingame.com](https://codingame.com)|
|clashofcode|Challenge from clash of code mode of [codingame.com](https://codingame.com), resolution time must be less than 15 minutes|
|battledev|Challenge from [battledev](https://battledev.blogdumoderateur.com)|
|codegolf|Find the shortest possible solution|
|reverse|Challenge without description, you have to find logic your-self|

## Local Challenge Tips
```js
// Nodejs
let input = 
`
/* HERE YOUR INPUT*/
`
function* __readline(){
	let lines = input.split(/\n\s*/)
	while(lines.length) yield lines.shift()
}
const _readline = __readline();
function readline(){
	return _readline.next().value
}
```

## Challenge

### Ordered Sums
> lvl1 algo codegolf codingame clashofcode

* **DESCRIPTION**
	* Your job is to help Logan arrange the numbers in ascending order and print the sum in a form that his daughter can understand.
* **INPUT**
	* the string sum
* **OUTPUT**
	* A string containing the sum described in sum with each number in ascending order
* **CONSTRAINT**
	* sum contains only digits and the + character.
	* None of the numbers of sum are negative.
	* Every number of sum has a single digit.
	* sum is at most 100 characters long.
* **EXAMPLE**
	* IN : `1+3+2` / OUT : `1+2+3`

```js
// Nodejs, 57 Characters
console.log(readline().split`+`.sort((a,b)=>a-b).join`+`)
```
```py
# Python3, 43 Characters
print('+'.join(sorted(input().split('+'))))
```
---
### Square CLI
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* You should print in standard output a square hollow composed of # symbol
* **INPUT**
	* Integer N
* **OUTPUT**
	* A square of dimension N, hollow and composed of #
* **CONSTRAINT**
	* 0 < N < 100
* **EXAMPLE**
	* IN : `5`
	* OUT : 
```
#####
#   #
#   #
#   #
#####
```

```js
// Nodejs, 150 Characters
N=parseInt(readline())
console.log(Array(N).fill(Array(N).fill`#`).map((e,i)=>i==0||i==N-1?e.join``:e.map((j,o)=>o==0||o==N-1?j:' ').join``).join`\n`)
```

```js
// Nodejs, 142 Characters
N=parseInt(readline())
res=[]
for(i=0;i<N;i++)
i==0||i==N-1?res.push('#'.repeat(N)):res.push(`#${' '.repeat(N-2)}#`)
console.log(res.join`\n`)
```
---
### Hypotenuse by sides
> lvl1 algo reverse codingame clashofcode
* **EXAMPLE**
	* IN
```
2 3
```
	* OUT : `3`
	* IN
```
9 5
```
	* OUT : `10`

```js
// Nodejs
var inputs = readline().split(' ')
const x = parseInt(inputs[0])
const h = parseInt(inputs[1])

console.log(Math.floor(Math.sqrt(x**2+h**2)))
````
---
### Biggest Integer as Power
> lvl2 algo codingame clashofcode
* **DESCRIPTION**
	* Given a number N and another number P, find the biggest integer M such that P^M ≤ N
* **INPUT**
	* Line 1: An integer N
	* Line 2: An integer P
* **OUTPUT**
	* An integer M, the biggest power of P
* **CONSTRAINT**
	* 0 < N, P ≤ 2³¹-1
* **EXAMPLE**
	* IN
```
33
2
```
	* OUT : `5`, because 2^5=32 ≤ 33


```js
// Nodejs
const N = parseInt(readline())
const P = parseInt(readline())

for(i=0;i<255;i++){
    if(P**i>N){
        console.log(i-1)
        break
    }
}
```
---
### Square of digits sum
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* A bruh number of n is square of sum digits of n
* **INPUT**
	* A number n
* **OUTPUT**
	* A bruh number of n
* **CONSTRAINT**
	* n ≤ 10^18
* **EXAMPLE**
	* IN `11`
	* OUT `4`

```js
// Nodejs, 64 Characters
I=parseInt
console.log(readline().split``.reduce((r,v)=>I(r)+I(v))**2)
```

```py
# Python, 31 Characters
print(sum(map(int,input()))**2)
```
---
### Alternate Operations
> lvl1 algo codingame clashofcode reverse
* **EXAMPLE**
	* IN `6 4`
	* OUT `210`
	* IN `15 3`
	* OUT `1218`
	* IN `9 2`
	* OUT `711`
	* IN `2 9`
	* OUT `-711`
	* IN `5 5`
	* OUT `010`

```js
// Nodejs
var inputs = readline().split(' ')
const A = parseInt(inputs[0])
const B = parseInt(inputs[1])

console.log(`${A-B}${A+B}`)
```
---
### Circle Intersections
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* You are given a number of circles assuming that none are positioned on top of each other. What is the most number of points that they will intersect at? For example 3 circles: 6 points
* **INPUT**
	* One int x the number of circles
* **OUTPUT**
	* One int y the maximum number of intersecting points
* **CONSTRAINT**
	* 1<x<1000000000
* **EXAMPLE**
	* IN `3`
	* OUT `6`

```js
// Nodejs, 37 Characters
n=parseInt(readline())
print(n*(n-1))
```
```py
# Python, 27 Characters
n=int(input())
print(n*n-n)
```
```ruby
# Ruby, 19 Characters
p (x=gets.to_i)*~-x
```
---
### Polygon sides
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* Given N distances, tell if you can make a Polygon.
* **INPUT**
	* A string of N distances (separate by space)
* **OUTPUT**
	* true if you can build a polygon with those distances (even flat) or false otherwise
* **CONSTRAINT**
	* 3 <= N <= 10^6
* **EXAMPLE**
	* IN `2 3 4`
	* OUT `true`
	* IN `1 1 20 4 3`
	* OUT `false`

```js
// Nodejs, 120 Characters
D=readline().split` `.map(e=>parseInt(e)).sort((a,b)=>a-b)
B=D.pop()
console.log(D.reduce((r,v)=>r+v)>=B?'true':'false')
```
```py
# Python, 74 Characters
d=list(map(int,input().split()))
print(str(sum(d)-max(d)>=max(d)).lower())
```
---
### Math Plan Equation 
> lvl2 algo codingame clashofcode reverse
* **EXAMPLE**
  * IN
```
1 2
3 5
```
  * OUT
```
2 3.5
```
  * IN
```
0 0
10 10
```
  * OUT
```
5 5
```
  * IN

```
-99 -99
99 99
```
  * OUT 

```
0 0
```


```js
// Nodejs
var inputs = readline().split(' ');
const x1 = parseInt(inputs[0]);
const y1 = parseInt(inputs[1]);
var inputs = readline().split(' ');
const x2 = parseInt(inputs[0]);
const y2 = parseInt(inputs[1]);

console.log(`${(x1+x2)/2} ${(y1+y2)/2}`);
```
---
### Magic Array
> lvl3 algo codingame clashofcode
* **DESCRIPTION**
	* Write a program to print true or false based on whether the given array is magic array or not.
	* {8, 5, -5, 5, 3} is not a magic array because the sum of the prime numbers is 5+5+3 = 13. Note that -5 is not a prime number because prime numbers are positive.
	* If there are no prime numbers in the array, the array is a magic array if the first element is 0.
* **INPUT**
	* A space separated list of integers.
* **OUTPUT**
	* A single line containing true if the given array is a magic array or false if it isn't.
* **CONSTRAINT**
	* -50 ≤ value of elements in array ≤ 50
	* 0 < length of line ≤ 100
* **EXAMPLE**
	* IN `21 3 7 9 11 4 6`
	* OUT `true`

```js
// Nodejs
const s = readline();
const isPrime = num => {
  for(let i = 2; i < num; i++)
    if(num % i === 0) return false;
  return num > 1;
}

sum=0
exe=0
s.split` `.map((e,i)=>i==0 ? exe=parseInt(e):isPrime(parseInt(e))?sum+=parseInt(e):{})

console.log(sum==exe?'true':'false')
```
---
### Dots and Stars Matrix
> lvl3 algo codingame clashofcode
* **DESCRIPTION**
	* Given an N by M matrix of dots and stars, count the number of stars in each row and in each column.
* **INPUT**
	* Line 1: An integer N
	* Line 2: An integer M
* **OUTPUT**
	* Line 1: "ROWS:"
	* Next N lines: Integers representing the number of stars in each row, top to bottom
	* Next line: "COLUMNS:"
	* Next M lines: Integers representing the number of stars in each column, left to right
* **CONSTRAINT**
	* C is either . or *
	* 1 ≤ N,M ≤ 50
* **EXAMPLE**
	* IN
```
 3
 4
 ..**
 .**.
 ***.
```
	* OUT
```
ROWS:
2
2
3
COLUMNS:
1
2
3
1
```

```js
// Nodejs
const N = parseInt(readline());
const M = parseInt(readline());

ro=[]
co=Array(M).fill(0)

for (let i = 0; i < N; i++) {
    s = readline()
    ro.push(s.split``.filter(e=>e=='*').length)
    s.split``.forEach((e,i)=>e=='*'?co[i]++:{})
}

console.log('ROWS:')
console.log(ro.join`\n`)
console.log('COLUMNS:')
console.log(co.join`\n`)
```
---
### Mobile Number to Morse
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* let us assume that you are a CID officer and got a mobile number of a criminal your task is to convey the message to higher officials in MORSE CODE as no one else can read it ie..; in morse code
```
1 .---- 6 -....
2 ..--- 7 --...
3 ...-- 8 ---..
4 ....- 9 ----.
5 ..... 0 -----
```
	* sample input and output 1466886532 --> .---- ....- -.... -.... ---.. ---.. -.... ..... ...-- ..---
	* NOTE: if it fails to be a mobile number print 'Untransformable'
* **INPUT**
	* A string of phone number
* **OUTPUT**
	* a string which contains every digit in phone number as morse code seperated by spaces
* **CONSTRAINT**
	* no other characters except numbers are allowed
* **EXAMPLE**
	* IN `1466886532`
	* OUT `.---- ....- -.... -.... ---.. ---.. -.... ..... ...-- ..---`
	* IN `97055343e1`
	* OUT `Untransformable`
	* IN `12345567881`
	* OUT `Untransformable`
	* IN `7697653245`
	* OUT `--... -.... ----. --... -.... ..... ...-- ..--- ....- .....`

```js
// Nodejs, 177 Characters
r=readline()
console.log(r.match(/^[0-9]{10}$/)?r.split``.map(e=>["-----",".----","..---","...--","....-",".....","-....","--...","---..","----."][e]).join` `:'Untransformable')
```
```js
// Nodejs, 146 Characters
r=readline()
console.log(r.match(/^[0-9]{10}$/)?r.split``.map(e=>(e<5?'.':'-').repeat(e%5)+(e<5?'-':'.').repeat(5-e%5)).join` `:'Untransformable')
```
```py
# Python
'-.'[l<5]*(l%5)+'.-'[l<5]*(5-l%5)
'------.....----'[i+5:i:-1] # Js '-----.....-----'.slice(i,i+5).split``.reverse().join``
```
---
### Integers Dot Sequence
> lvl2 algo codingame clashofcode
* **DESCRIPTION**
	* The goal is to reformat a sequence of integers, so that each pair is separated by a number of points ('.') equal to the number on the left.
* **INPUT**
	* Line 1: Length of sequence
	* Line 2: An integer sequence spaced by space
* **OUTPUT**
	* Line 1: A string containing the sequence of integers, T, separated by the correct number of '.'s
* **CONSTRAINT**
	* 1 ≤ Length_of_T ≤ 50
	* 0 ≤ Element_of_T ≤ 500
* **EXAMPLE**
	* IN
```
5
1 2 3 4 5
```
	* OUT `1.2..3...4....5`

```js
// Nodejs
const lenT = parseInt(readline());
var inputs = readline().split(' ');
res=[]

res=inputs.map((e,i)=>i==lenT-1?e:`${e}${'.'.repeat(parseInt(e))}`)
console.log(res.join``)
```
---
### Bird Language
> lvl2 algo codingame clashofcode
* **DESCRIPTION**
	* The Birds Language has only one rule: after each vowel (a,e,i,o,u,A,E,I,O,U) you should insert the letter p followed by the vowel one more time. For a given string convert it to Birds Language.
* **INPUT**
	* string A string which contains ASCII characters.
* **OUTPUT**
	* string converted to Birds Language.
* **CONSTRAINT**
	* 1 < length of string < 1000
* **EXAMPLE**
	* IN `alex`
	* OUT `apalepex`

```js
// Nodejs
const string = readline();

res=string.split``.map(e=>['a','e','i','o','u','A','E','I','O','U'].indexOf(e)!=-1?`${e}p${e}`:e)

console.log(res.join``);
```
```py
# Python
import sys
import math
import re

string = input()
print(re.sub(r'([aeiouAEIOU])', r'\1p\1', string))
```

```py
# Python
string = input()
s = ''
for c in string:
    if c.lower() in 'aeoiu':
        s+=c+'p'
    s+=c
print(s)
```
---
### Puzzle Tabs
> lvl1 algo codingame clashofcode
* **DESCRIPTION**
	* For a given regular jigsaw puzzle of of size h x w how many tabs (the bits that stick out) are there?
	* A rectangular jigsaw puzzle has pieces arranged in a grid.
	* Each piece has a single tab or socket on each side that is in contact with an adjacent piece.
* **INPUT**
	* Line 1: Two space-separated integers h and w for the height and width of the puzzle in terms of pieces.
* **OUTPUT**
	* Line 1: The numbers of tabs as an integer.
* **CONSTRAINT**
	* 1 ≤ h, w ≤ 100
* **EXAMPLE**
	* IN `2 2`
	* OUT `4`

```js
// Nodejs
i=readline().split(' ')
w=parseInt(i[0])
h=parseInt(i[1])
console.log((w)*(h-1)+(w-1)*h)
```
```py
# Python
w,h=map(int,input().split())
print(w*h*2-w-h)
```
---
### Letters Pyramid
> lvl4 algo codingame clashofcode
* **DESCRIPTION**
	* The goal is to design a pyramid of given height. The building blocks are the letters A to Z.
* **INPUT**
	* Line 1: The height H of the pyramid
* **OUTPUT**
	* 2×H-1 lines: The design of the pyramid, i.e. letters denoting height of the block (see the example) - no trailing spaces
* **CONSTRAINT**
	* 1 ≤ H ≤ 26
* **EXAMPLE**
	* IN `3`
	* OUT
```
  A
 ABA
ABCBA
 ABA
  A
```
	* IN `1`
	* OUT
```
A
```
	* IN `5`
	* OUT
```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
 ABCDCBA
  ABCBA
   ABA
    A
```

```js
// Nodejs
N = parseInt(readline())
L = (N-1)*2+1
answer = ""
for(i=0;i<L;i++) {
        for(j=0;j<Math.abs(N-(i+1));j++)
            answer+=" "
    	cpt=65
	    for(j=0;j<Math.abs(Math.abs(N-(i+1))-N);j++){
	        answer+=String.fromCharCode(cpt)
	        cpt++
	    }
	    for(j=1;j<Math.abs(Math.abs(N-(i+1))-N);j++){
	        cpt--
	        answer+=String.fromCharCode(cpt-1)
	    }
    answer+='\n'
}
console.log(answer)
```
```js
// Nodejs
N = parseInt(readline())
L = (N-1)*2+1
answer = []
for(i=0;i<N;i++) {
    string = Array(Math.abs(N-(i+1))).fill` `.join``
    cpt=64
    for(j=0;j<Math.abs(Math.abs(N-(i+1))-N);j++){
        cpt++
        string+=String.fromCharCode(cpt)
    }
    for(j=1;j<Math.abs(Math.abs(N-(i+1))-N);j++){
        cpt--
        string+=String.fromCharCode(cpt)
    }
    answer.push(string)
}
console.log(answer.concat(answer.slice(0,-1).reverse()).join('\n'))
```
---
### Alpha Case Inverser
> lvl1 algo codingame clashofcode
* **EXAMPLE**
	* IN `AAAaaa`
	* OUT `aaaAAA`
	* IN `abCJu58Abod`
	* OUT `ABcjU58aBOD`
	* IN `?.;74526`
	* OUT `?.;74526`

```js
// Nodejs
s = readline()

res=""
s.split``.map(e=>{
    if(e.match(/[A-Z]/))
        res+=e.toLowerCase()
    else if(e.match(/[a-z]/))
        res+=e.toUpperCase()
    else 
        res+=e
})

console.log(res)
```
```py
# Python
s = input()
for c in s:
    if c.isalpha():
        c = chr(ord(c) ^ 32)
    print(end=c)
```
---
### Arithmetic Series
> lvl1 algo codingame clashofcode
* **DESCRIPTION**
	* In mathematics exam N students passed and some others failed ! The teacher John decided to give sweets to students .He will distribute the sweets to students who passed the exam in the order of 1 sweet for first student 3 sweets for second student 5 sweets for third student and so on ...
	* The sweets are in packets. Each packet contains 10 sweets. how many packets are needed for giving sweets for students. He said that next time the failed students will study because of this !
* **INPUT**
	* Line 1 : an integer N the number of students who passed the exam
* **OUTPUT**
	* Line 1 : P the number of packets needed
* **CONSTRAINT**
	* 10 ≤ N ≤ 100
	* 10 ≤ P ≤ 1000
* **EXAMPLE**
	* In `10`
	* Out `10`

```js
// Nodejs, naive solution
const n = parseInt(readline());
// For each student compute sweets number
cpt=0
for(i=0;i<=n;i++)
    cpt+=(i*2)-1
console.log(Math.floor(cpt/10)+1)
```
```js
// Nodejs recursive
U = b => b==1 ? 1 : U(b-1)+2
console.log(Math.ceil(Array(parseInt(readline())+1).fill``.reduce((r,v,i)=>r?parseInt(r+U(i)):r=0)/10))
```
```py
# Python
n = int(input())
# U(n+1) = U(n)+2
# U(n) = n*2-1
# SUM(U(n)∀n∊{1,n}) = ( ( U(0)+U(n) )/2 ) * n = n*n
print(math.ceil(n * n / 10))
```

---
### Digit Multiplication
> lvl3 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* Display the number of iterations necessary such that the result of the multiplication of the digits that make up N is less than 10, with N value is result previous operation
* **INPUT**
	* Integer N
* **OUTPUT**
	* Number of iterations
* **CONSTRAINT**
	* 0<N<1000
* **EXAMPLE**
	* IN `74`
	* OUT `3`
```
7*4=28
2*8=16
1*6=6
```

```js
// Nodejs, 109 Characters
c=-1
a=n=>{c++;n.length==1?console.log(c):a(n.split``.reduce((r,e)=>r*parseInt(e)).toString())}
a(readline())
```

---
### Reverse Word
> lvl2 algo codingame clashofcode
* **DESCRIPTION**
	* Your program should reverse the letters of each word of a given input sentence.
* **INPUT**
	* A String S
* **OUTPUT**
	* a String in which the characters of each word separated by spaces have been reversed.
* **CONSTRAINT**
	* S contains at least 1 character.
	* S contains only alpha-numeric characters and spaces.
	* S does not contain multiple spaces after or tabs.
* **EXAMPLE**
	* IN `Hello World`
	* OUT `olleH dlroW`

```js
// Nodejs
const S = readline();

res=S.split` `.map(e=>e=e.split``.reverse().join``)

console.log(res.join` `);
```

---
### Yoda translation
> lvl2 algo codingame clashofcode
* **DESCRIPTION**
	* Given a backward quote from Yoda, rewrite it in an understandable way.
	* There is no ponctuation in the sentences. A quote from Yoda will not start with a name.
* **INPUT**
	* Line 1: The number n of words to be put at the end of the sentence.
	* Line 2: A string yoda corresponding to the sentence from Yoda.
* **OUTPUT**
	* A string sentence with words in expected order.
	* Note that the output is case sensitive.
* **CONSTRAINT**
	* 0 ≤ n ≤ number of words in yoda
	* 0 < length of yoda ≤ 256
* **EXAMPLE**
	* IN
```
1
Patience you must have
```
	* OUT 
```
You must have patience
```

```js
// Nodejs
n = parseInt(readline());
yoda = readline();

r=yoda.split` `.slice(n)
s=yoda.split` `.slice(0,n)

r=r.join` `
r=r.charAt(0).toUpperCase() + r.slice(1)

s=s.join` `
s=s.charAt(0).toLowerCase() + s.slice(1)

console.log(`${r} ${s}`);
````

---
### Shifted String
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* You are given a sequence of N positive integers.
	* You have to print this sequence after a left shift (the first element becomes the last one, the second becomes the first, the third becomes the second, ...).
* **INPUT**
	* Line 1: N, the number of elements
	* Line 2: N positive integers lower than 1 000 000, the elements of the sequence
* **OUTPUT**
	* One line containing exactly N numbers : the sequence after being shifted
* **CONSTRAINT**
	* 2 ≤ N ≤ 100
* **EXAMPLE**
	* IN
```
3
3 1 2
```
	* OUT
```
1 2 3
```

```js
// Nodejs, 74 Characters
r=readline;r()
I=r().split` `
a=I.shift()
console.log(`${I.join` `} ${a}`)
```

---
### Altered Letters
> lvl2 algo codingame clashofcode reverse
* **EXAMPLE**
	* IN `codingame`
	* OUT `cpflrlgtm`
	* IN `abcdef`
	* OUT `acegik`
	* IN `cracker`
	* OUT `cscfojx`
	* IN `aaaaaa`
	* OUT `abcdef`

```js
// Nodejs
const l = readline();
res=""

l.split``.map((e,i)=>res+=String.fromCharCode(e.charCodeAt(0)+i))

console.log(res)
```

---
### Average ASCII value of the string
> lvl2 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* Given an input string s, return the character given by the average of the ASCII values of all characters in the string.
	* s can contain any ASCII characters, upper case letters, lower case letters, spaces or symbols.
	* If the average value is a float, round down (floor).
* **INPUT**
	* Line 1: integer len_s - length of s
	* Line 2: string s - the string to find the average ASCII value of.
* **OUTPUT**
	* the character associated with the average ASCII value of the string s
* **CONSTRAINT**
	* 1 <= len_s <= 50
* **EXAMPLE**
	* IN
```
5
hello
```
	* OUT `j`

```js
// Nodejs, 117 Characters
R=readline
l=parseInt(R())
s=R()
r=0
s.split``.map(v=>r+=v.charCodeAt(0))
print(String.fromCharCode(Math.floor(r/l)))
```
```py
# Python, 57 Characters
l=int(input())
print(chr(sum(ord(i)for i in input())//l))
```
```py
# Python, 57 Characters
n=int(input())
print(chr(sum(map(ord,list(input())))//n))
```

---
### Ascii Affine Graph
> lvl3 algo codingame clashofcode codegolf
* **DESCRIPTION**
	* You will receive a polynomial equation and must plot it in the interval 0 ≤ y,x ≤ 9, the value of the equation must be truncated to integer before entering it on the chart. All results of the equation after truncating that exceed the limits of the axes must be discarded.
	* For simplicity (0,0) is in the upper left corner.
* **INPUT**
	* Line 1 : An equation in the format: x = (c_0 * y**0) + (c_1 * y**1) + (c_2 * y**2) + ... + (c_n * y**n)
	* When the coefficients are 0, the term will be omitted.
* **OUTPUT**
	* Matrix 9 x 9 with the chart
* **CONSTRAINT**
	* equation length ≤ 50
* **EXAMPLE**
	* IN `x = (1 * y**1)`
	* OUT
```
o.........
.o........
..o.......
...o......
....o.....
.....o....
......o...
.......o..
........o.
.........o
```

```js
// Nodejs, 164 Characters
e=readline()
res=[]
for(y=0;y<10;y++){
a=Array(10).fill`.`
i=Math.floor(eval(e.split` = `[1]))
i<a.length?a[i]="o":{}
res.push(a.join``)
}
console.log(res.join`\n`)
```

---
### Weird Reversed Word
> lvl3 algo codingame clashofcode reverse
* **EXAMPLE**
	* IN `helloworld`
	* OUT `drwlehlool`
	* IN `hellworld`
	* OUT `lolehlwrd`
	* IN `jump`
	* OUT `pujm`
	* IN `a`
	* OUT `a`

```py
# Python 
s = input()
a=''
b=''
for i in range(len(s)):
    if i%2!=0:
        a+=s[i]
    else:
        b+=s[i]
print(a[::-1]+b)

```

---
### Diamond ASCII
> lvl3 algo codingame clashofcode
* **DESCRIPTION**
	* You must print a diamond of given size.
* **INPUT**
	* One integer N
* **OUTPUT**
	* First line with N "#", after That
	* Diamond of 2*N size 
* **CONSTRAINT**
	* 1<=N<=12
* **EXAMPLE**
	* IN `4`
	* OUT
```
####
   #
  ###
 #####
#######
#######
 #####
  ###
   #
```

```js
// Nodejs
N = parseInt(readline())
L = (N-1)*2+1
answer = []
for(i=0;i<N;i++) {
    string = Array(Math.abs(N-(i+1))).fill` `.join``
    cpt=64
    for(j=0;j<Math.abs(Math.abs(N-(i+1))-N);j++){
        cpt++
        string+='#'
    }
    for(j=1;j<Math.abs(Math.abs(N-(i+1))-N);j++){
        cpt--
        string+='#'
    }
    answer.push(string)
}
console.log(Array(N).fill('#').join``)
console.log(answer.join('\n'))
console.log(answer.reverse().join('\n'))
```
```py
# Python
import sys
import math

n = int(input())
w=2*n-1
print("#"*n)
for i in range(n):
    print(" " * (n-i-1) + "#" * (2*i+1))
for i in range(n-1,-1,-1):
    print(" " * (n-i-1) + "#" * (2*i+1))
```

---
### Weird Reverse Word
> lvl3 algo codingame clashofcode reverse UNSOLVED
* **EXAMPLE**
	* IN `Hello World`
	* OUT `deHllloorW`
	* IN `An ElePHPant`
	* OUT `AaEeHlnnPPt`
	* IN `Do you want to go to United States ? I do !`
	* OUT `aaDddeegIinnooooooSsttttttUuwy?!`
	* IN `Give me your HEART, and I give you mine...`
	* OUT `AadEeeeeGgHIiiimmnnooRrTuuvvyy,...`
	* IN `;ee-'oe,.`
	* OUT `eeeo;-',.`

```js
const entry = readline();

res=[]
res2=[]
console.error(entry)
entry.replace(' ','').split``.sort((a,b)=>a.toLowerCase().charCodeAt(0)-b.toLowerCase().charCodeAt(0)).join``.trim().split``.map(e=>{
    e.toLowerCase().match(/[a-z]/)?res.push(e):{}
})
entry.replace(' ','').split``.map(e=>{
    e.toLowerCase().match(/[a-z]|\s/)?{}:res2.push(e)
})
console.log(res.concat(res2).join``)

```
```c++
int main() {
    string entry;
    getline(cin, entry);int a[128]={0};
    for(int i=0;i<entry.length();i++){
        a[entry[i]]++;

    }
    for(int i=65;i<91;i++){
        for(int j=0;j<a[i];j++){
            cout<<(char)i;
        }
        for(int j=0;j<a[i+32];j++){
            cout<<(char)(i+32);
        }
    }
}
```
	
---
### L ASCII Chart
> lvl3 algo codingame clashofcode UNSOLVED
* **DESCRIPTION**
	* Print an L shape of width W and height H with the internal corner at the coordinate X, Y.
	* The top left character of the pattern is a X alternating with O.
	* The border corners are the character +, the top and bottom are - and the sides are |.
	* Such as:
```
 _  |- W=9 -|  
 |  +----+      
 |  |XOXO|      
H=6 |OXOX+--+ -Y=2-
 |  |XOXOXOX|  
 |  |OXOXOXO|  
 _  +-------+
         |
        X=5
```
* **INPUT**
	* First line: space-separated W H
	* Second line: space-separated X Y
* **OUTPUT**
	* The L shape
* **CONSTRAINT**
	* 3 <= W <= 20
	* 3 <= H <= 20
	* 1 <= X <= W - 2
	* 1 <= Y <= H - 2
* **EXAMPLE**
	* IN
```
5 5
2 2
```
  * OUT

```
 +-+
 |X|
 |O+-+
 |XOX|
 +---+
```

```js
var inputs = readline().split(' ');
const W = parseInt(inputs[0]);
const H = parseInt(inputs[1]);
var inputs = readline().split(' ');
const X = parseInt(inputs[0]);
const Y = parseInt(inputs[1]);

console.error(W,H,X,Y);

console.log('+'+'-'.repeat(W-X-2)+'+');

for(i=0;i<H;i++){
    if(i==Y-1){
        o=''
        for(j=0;j<X-1;j++)
            o+=i%2?j%2?o+='X':o+='O':!j%2?o+='X':o+='O'
        console.log('|'+o+'+'+'-'.repeat(W-X-2)+'+');
    }
    else if(i<Y-1){
        o=''
        for(j=0;j<X-1;j++)
            o+=i%2?j%2?o+='X':o+='O':!j%2?o+='X':o+='O'
        console.log('|'+o+'|');
    }
    else {
        o=''
        for(j=0;j<W-2;j++)
            o+=i%2?j%2?o+='X':o+='O':!j%2?o+='X':o+='O'
        console.log('|'+o+'|');
    }
        
}
console.log('+'+'-'.repeat(W-2)+'+');
```
```py
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

l = [["XO"[i+j&1] for j in range(w)] for i in range(h)]
for i in range(y):
    l[i]=l[i][:x+1]

l[0] = list("+" + "-" * (x-1) + "+")
l[-1] = list("+" + "-" * (w-2) + "+")
for i in range(1,h-1):
    l[i][0] = l[i][-1] = "|"
for i in range(x+1,w-1):
    l[y][i] = "-"
l[0][0] = l[0][x] = l[y][x] = l[y][-1] = l[-1][0] = l[-1][-1] = "+"
for x in l:
    print("".join(x))
```

---
### Chess material advantage
> lvl3 algo codingame clashofcode
* **DESCRIPTION**
	* Given a chess position, your task is to determine the material advantage (or disadvantage) from the white player's perspective. The total material a player has is the sum of the values of each remaining piece on the board that belongs to him.

	* Each chess position is represented by an 8 x 8 matrix of squares. Each piece is identified by a single letter. White pieces are designated using upper-case letters, while black pieces use lower-case letters. Empty squares are given as dots.

	* The standard value of each piece is:
	1 Pawn: P, p
	3 Knight: N, n
	3 Bishop: B, b
	5 Rook: R, r
	9 Queen: Q, q
	0 King: K, k (not counted)
* **INPUT**
	* Line 1: an integer N for the height of the board.
	* N next lines: a string S representing the squares in that row.
* **OUTPUT**
	* A single line with an integer D, representing the difference between white's material and black's. If the difference is 0, print equal instead. 
* **CONSTRAINT**
	* Since the chess board is fixed in a size of 8 x 8:
	* N = 8
	* size(S) = 8
	* -103 <= D <= 103
* **EXAMPLE**
	* IN
```
8
.R......
n.......
........
k.K.....
........
.......P
........
........
```
	* OUT `3`
	* IN
```
8
.r..k...
.....p.p
......p.
.r.....P
.....QP.
......K.
.....P..
........
```
	* OUT `-1`
	* IN
```
8
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
```
	* OUT `equal`
	* IN
```
8
q.....k.
......q.
.......q
........
........
........
......R.
......K.
```
	* OUT `-22`


```js
R=readline
N=R()
o={p:1,n:3,b:3,r:5,q:9,k:0}
A=e=>o[e.toLowerCase()]?o[e.toLowerCase()]:0
W=0
for(i=0;i<+N;i++)
R().split``.forEach(e=>e==e.toUpperCase()?W+=A(e):W-=A(e))
print(W?W:'equal')
```

---
### Text decoration
> 
* **DESCRIPTION**
	* Decorate text by surrounding it with the given decoration character, N number of times. Provide one space before & after the text as shown in the examples below.
* **INPUT**
	* A line containing 3 parameters namely text , decoration character and N number of times.
* **OUTPUT**
	* print text with decoration
* **CONSTRAINT**
	* 1 < N < 10
* **EXAMPLE**

* IN `HELLO * 2`
* OUT

```
***********
***********
** HELLO **
***********
***********
```
* IN `welcome * 1`
* OUT

```
***********
* welcome *
***********
```
* IN `Awesome $ 4`
* OUT

```
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$ Awesome $$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
```
* IN `wow * 5`
* OUT

```
***************
***************
***************
***************
***************
***** wow *****
***************
***************
***************
***************
***************
```

```js
I=readline().split` `
o=+I[2]
a=e=>I[1].repeat(e)
for(i=0;i<o*2+1;i++)
print(i==o?a(o)+" "+I[0]+" "+a(o):a(I[0].length+2+o*2))
```

```py
i,n,p=input().split()
p=int(p)
m=(n*len(i)+n*2*p+n*2+"\n")*p
print(m,end="")
print(p*n+" "+i+" "+p*n+"\n"+m)
```

---
### Comming soon ...
> 
* **DESCRIPTION**
* **INPUT**
* **OUTPUT**
* **CONSTRAINT**
* **EXAMPLE**






