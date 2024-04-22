Each round consists of turns.
A new turn happens when someone fires a shot.
A new rounds happens when someones health reaches 0.
If there are no more shots left but players are still alive, the gun is loaded with more random rounds.

-New Game-
Health for both players is set back up to full.
Gun is loaded with a certain amount of rounds.
Each round is either live or a blank.

Player 1 goes first in choosing to turn the gun at themself, or shoot Player 2.
Player 2 does the same next turn.
If a live round is shot, it will deplet its target's health by 1, go onto next turn.
If a blank round is shot, it will do nothing, go onto next turn.
Game ends when one of the player's health is at 0.

-A new round-
Players healths are reset to a new max.
Gun is reloaded with a new amount of live and blanks.

Implement player class, containing p1name, p2name (always "The Dealer"), p1health, p2health
no it just has name and health, create two different objects player_1 and player_2 and assign different vars

TODO:
- add items
- add waiver ✅
- change colour of text
- add some sort of image
- add quotes around Dealer speach
- use rich to make colour words better e.g. Round 1
- add revive text/image after you shoot yourself with live
- smarter ai for Dealer, higher chance of live round = shoot player

SHOOTING YOURSELF WITH A BLANK SKIPS THE DEALER'S TURN


# Items
1. Beer can - eject current cartridge from chamber
2. Cigarette - increase 1 health
3. Saw - double damage on next shot
4. Magnifying glass - see what is in chamber
5. Handcuffs - take two turns

Iventory is wiped at the beginning of each round.
Items are only added at the start of round 2.
A player can have 2 items before each reload in round 2.
Once an item is used, it is removed from the inv.

Items are the very first thing to be done at the beginning of round 2.