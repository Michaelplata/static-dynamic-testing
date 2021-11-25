### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# to check if the card is equal to 1 double equals to sign should be used ("==" instead of "=") also colon sign is missing after the "else" on line 23
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# to define a function "def" should be used instead of "dif", the comma is missing after card1 on line 28
# also "card" is not defined 
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# to get the total, first of all a zero should be assigned to it on line 37, also return on line 40 should be indented to the left
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
  