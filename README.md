# ascii-kitty
Little ascii kitty that can speak and move

             ^  ^  hello
            (ù.ù )___(
             //||-//||
             
             ^  ^  world!
            ( ô.ô)___(
             //||-//||


## Add a state

```
ls -l states/
... state1.yaml
... state2.yaml
... state3.yaml
```

### A state is a single snapshot that describe the cat
```
Example:

state:
    ears : '             ^   ^'
    face : '            (ù.ù )___('
    paws : '             ||\\-||\\'

```

### Add chit-chat in a state
```
Example:

state:
    sky : '                     hello world!'
    ears : '             ^   ^  /  '
    face : '            (ù.ù )___( '
    paws : '             ||\\-||\\ '

```

## Build Stories

```
ls -l stories/
... story1.yaml
... story2.yaml
... story3.yaml
```

## A story is a yaml file that describes a sequence of states

```
Example:

- state: "state1"
  duration: 1

- state: "state2"
  duration: 1

- state: 'state2'
  duration: 1

- state: 'state3'
  duration: 1

- state: 'state2'
  duration: 1

```
