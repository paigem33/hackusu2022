## Server



## Client



## Common

### Domino

#### Properties:

- A Number
- B Number
- Image of domino

#### Methods:
    *Creates a new domino with two numbers and an image*
    constructor(a, b, image)
    *Returns the a value*
    get_a()
    *Returns the b value*
    get_b()
    *Returns the image*
    get_image()


### Player Deck

The deck that the player uses in thier rounds to play dominoes.

#### Properties:

- List of Dominos

#### Methods:
    * Adds a domino to the end of the collection *
    add_domino(domino)
    * Removes the domino at the index in the collection and returns it * 
    remove_domino(index) -> domino

### Bonyard

#### Properties:

- List of dominos

#### Methods:
    * Creates a new boneyard from a domino set. This set will be randomized in the list intially. *
    constructor(domino_set)
    * Pops the top domino from the collection and returns it *
    pop() -> domino

### Hub
#### Properties:

- List of tracks
- Starting Domino

#### Methods:
    * Creates a new hub with the tracks and the starting domino *
    constructor(tracks, starting_domino)
    * Returns a reference to a track *
    get_track(index) -> &Track

### Track
#### Properties:

- List of dominos
- bool public

#### Methods:
    * Trys to push a domino to the end of the track. If it cannot be added, return the domino back to the caller *
    push(domino) -> Result<Domino>
    * Removes all dominos except the end one and returns them to the caller *
    get_all_except_end() -> [Domino]
    * sets the publicity of this track *
    set_public(public)
    * gets the publicity of this track *
    get_public() -> bool

