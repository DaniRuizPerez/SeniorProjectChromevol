Senior Project Chromevol Web
============

<p align="center">
<img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/chromevaloa.png" width="500">
</p>

This was part of the senior project of my undergrad in computer science at UDC (Spain). The 165 pages report (Spanish) can be viewed [here](https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/Report.pdf) for further explanations.







A demonstration video of the game can be viewed [here](https://github.com/DaniRuizPerez/Pygame/blob/master/VideoDemo.mp4).


We developed the history and background for the game and implemented different maps, each with their own enemies and bosses. We designed the sprites of all the characters and implemented different levels of AIs and powers ensure a good time for every level of skill.


## Game engine design

Everything that is not a static background is considered an actor, whidh extends pygame.sprite.Sprite. In addition to that, it has a reference to the phase in which it is, the graphic aspect, physics, behaviour (state) and stats. All the attributes can be viewed in this UML diagram: 

<p align="center">
<img src="https://github.com/DaniRuizPerez/Pygame/blob/master/ImagesAndUML/UML 5 actorOverview.png" width="800"></p>


The state class is one of the most complex ones, which gives each character its behavior and transition strategy between states. We mixed the design patters strategy and state so the implementation of the specific action taken can be abstracted.


<p align="center">
<img src="https://github.com/DaniRuizPerez/Pygame/blob/master/ImagesAndUML/UML 3 actorStateFinal.png" width="800">
</p>

The Physics class calculates the new position in each frame based on the changes in the state.


## Enemy AI

The enemies are smarter and tougher each level, which was implemented with a probability of failure of taking certain actions that decrease as the level increase. The enemies:
- Dodge bullets
- Jump through obstacles and avoid falling into traps or pits
- Allways try to be inside the screen for the actual scroll value
- Try to follow the player and be at the same height

On top of that, each type of regular enemy has its own personality, and they follow a state diagram which includes things like chase, scape, attack, etc.

Each boss has a personalized state diagram, with things like run, fire one or several bullets in different directions, etc.

## Phase design

Everything is managed by a resource manager which extracts information for the phase (platforms, sprites, background or not, trap...) from a resource manager. 
Custom phases with different enemies and all sort of customizations can created very easilty with our XML format as can be seen here:

<p align="center">
<img src="https://github.com/DaniRuizPerez/Pygame/blob/master/ImagesAndUML/faseDefinition.png" width="500">
</p>

## Graphic design

We designed and created every sprite and sprite sheet that is on the game from scratch with vectorial design.


## Tools and execution

The project was developed with the following tools

- Python
- Pygame
- Pyglet

Installation:
```
pip install pygame
pip install pyglet
```


To execute the game, simply run the following command line instruction: 
```
python main.py 
```

## How to play
Move with the arrows, shoot with X and attack with Z


## Contact

Contact [Daniel Ruiz Perez](mailto:druiz072@fiu.edu) for requests, bug reports and good jokes.


## License

The software in this repository is available under the GNU General Public License, version 3. See the [LICENSE](https://github.com/DaniRuizPerez/PyGame/blob/master/LICENSE) file for more information.
