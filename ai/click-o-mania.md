General
-----------------------------------
* target color if only one cluster is present
* target color if <= 2 clusters remain (?)
* never leave a single color board score == 1 (ie., only one cell left in a color)

Cluster Score
-----------------------------------
* how many points is this cell worth to the game if taken
* cells that can not be taken are worth 0
* (a) count the cluster size for this cell
* score = a
* higher score is better

Neighbor Score Minimum Strategy
-----------------------------------
* target cells that have the lowest neighboring cell score when an average is taken, only count neighbors of different colors
* (a) sum then avg cluster score for all cells of a different color, touching target cell
* score = a
* lower score is better

Total Board Winnability Score Strategy
-----------------------------------
* how likely is a board to be completed (a score) after your considered move - give this score per cell (if that cell were to be taken)
	* (a) count all 1 point cells
	* (b) count all clusters on the board
	* score = a - b
* lower score is better

Color Winnability Score
-----------------------------------
* (a) count how many clusters per color
* score = a
* lower score is better

Cell
-----------------------------------
* compute a number of values for each cell on the board (see above for instructions on computation) - TBD what to do with these scores...
	* c_score (cluster score) - higher is better
	* nm_score (neighbor minimum score) - lower score is better
	* tbw_score (total board winnability) - lower score is better
	* cw_score (color winnability score) - lower score is better

    * take_score = pow(tbw_score, 2) + pow(cw_score, 2) + pow(nm_score, 2)
* A lower take_score is a better cell to take

* cw and tbw scores are really good if they are low - maybe they matter less when higher (pow(n, 2))
* nm score is TBD
* c score is TBD


print(math.pow(1, 2))
print(math.pow(2, 2))
print(math.pow(3, 2))
print(math.pow(4, 2))
print(math.pow(5, 2))

