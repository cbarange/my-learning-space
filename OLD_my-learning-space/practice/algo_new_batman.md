### Comming soon ...
> lvl3 algo codingame clashofcode
* **DESCRIPTION**
	* In the city of Gotham, crime lurks at every corner. The city's vigilante Batman is single-handedly responsible for eliminating the major crime gangs and thwarting their plans.
	* However, Batman has just recently announced his retirement, and the evil crooks are now beginning to reappear from the slums.

	* In order to ensure peace and stability to the city of Gotham, the mayor of Gotham has announced that there will be a new Batman selected from a pool of participants N. Anyone is free to join the competition: the only eligibility criteria is that one must have a passion to fight injustice and demonstrate wit and verve.

	* The tournament will be done in a knockout fashion, pitting one participant with another in a fair competition. In each competition, there are three tasks:
	* 1) playing a game of chess
	* 2) playing a game of arm wrestling
	* 3) navigating through the city of Gotham to find 20 clues
	* each of the tasks testing one of three traits: wit, strength and navigation ability respectively.

	* Each participant has differing wit w, strength s and navigation ability na, and the winner of each task is the one with the highest trait score for that respective task. It is possible to draw in the task if both participants have a similar trait score. The participant who wins the most number of tasks wins. In the event of a draw after considering all three tasks, the one with the smallest participant index wins. Hence, each competition will result in the elimination of one participant.

	* In order to decide the match-ups for the competition, the participants will be sorted according to the X formula:
	* Number of matches already won*1000 + w + s + na.
	* The two participants which have the lowest score of the X formula will be matched up with each other. In the event of a tie, the participant with the lowest index will be chosen first.

	* The participants are then eliminated sequentially until the final two battle it out. The final match will have increased stakes and involve the two participants equipped with Batman's high-tech gear and the winner will be the first to complete an unknown mission. The winner will be the one with the highest w+s+na score. Again, in a tie, the participant with the smallest index will be the winner and there will be no rematch.

	* Each competition between a pair of participants will last exactly one day, and due to space and manpower constraints, only one competition can be carried out each day. Find out the number of days required to host this competition.
* **INPUT**
	* Line 1:The number of participants N
	* Next N Lines:Each participant's wit w, strength s and navigation ability na, separated by a space. Participant with index 0 is the first line, followed by participant with index 1 and so on.
* **OUTPUT**
	* Line 1:The number of days required for the tournament
* **CONSTRAINT**
	* 1 <= N <= 1000
	* 0 <= w, s, na <= 100
* **EXAMPLE**
	* IN
```
5
3 10 4
40 2 5
32 5 43
46 87 43
99 99 99
```
	* OUT `4`

```js
const N = parseInt(readline());
console.error(N)

for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    console.error(inputs)
    const w = parseInt(inputs[0]);
    const s = parseInt(inputs[1]);
    const na = parseInt(inputs[2]);
}

console.log(N-1)
```

* Other example
	* IN 
```
50
43 21 4
39 4 23
49 34 24
39 48 34
29 49 59
10 30 49
50 38 23
30 48 39
29 48 20
30 29 38
43 21 4
39 4 23
49 34 24
39 48 34
29 49 59
10 30 49
50 38 23
30 48 39
29 48 20
30 29 38
43 21 4
39 4 23
49 34 24
39 48 34
29 49 59
10 30 49
50 38 23
30 48 39
29 48 20
30 29 38
43 21 4
39 4 23
49 34 24
39 48 34
29 49 59
10 30 49
50 38 23
30 48 39
29 48 20
30 29 38
43 21 4
39 4 23
49 34 24
39 48 34
29 49 59
10 30 49
50 38 23
30 48 39
29 48 20
30 29 38
```
	* OUT `48` 
	* IN 
```
100
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
3 10 4
40 2 5
32 5 43
46 87 43
49 59 92
34 59 2
6 39 3
34 58 23
93 48 28
49 39 43
``` 
	* OUT `99` 
