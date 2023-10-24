# AI-Aerial-Assault

Aerial Assault is a board game in which two players confront each other. It is usually played on paper in a Human vs. Human scenario, but this implementation is console based, Human vs. Computer.

The game consists in two 10 x 10 boards, one for each player. Both players have three planes available and they must choose where to position them on their own board. A plane has a head (1 cell), wings (5 cells), body (1 cell) and tail (3 cells). For now, a player has no information about the opponent's planes. After positioning the planes, the players take turns in guessing positions on the enemy's board (examples: C9, J2, A4, E10, G1). The goal is to destroy your rival's planes. A plane is considered destroyed only if its head has been hit. 

Let's assume that Player 1 should say a position now. There are three possible outcomes, based on what can be found at that position on the board of Player 2: air (if there is nothing there), hit (if a part of the wings, body or tail of any plane is there) or dead (if the head of a plane is there). Player 2 must communicate the outcome to Player 1. Depending on the guessings, a player can deduce where the heads of opponent's planes may be.

Aerial Assault is implemented using the following classes: Board, ComputerStrategy, Game and UI. ComputerStrategy is composed of two strategies - one for positioning the planes and one for choosing which positions to guess. 

After some testing was done, positioning the planes in a random manner proved to be a very clever strategy because many positionings are unintuitive for the human brain (especially the ones where the planes are right next to each other). 

When it comes to choosing which positions to guess, picking randomly is not a great idea. After all, only 3/100 cells contain heads of planes. Instead, the odds of actually hitting something are higher if positions closer to the centre of the board are tried first. For example, a part of a plane can never be in a corner of the board (A1, A10, J1, J10) due to the nature of the plane. 
