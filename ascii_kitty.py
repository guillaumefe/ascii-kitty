import time
import yaml
import os

story = 'basic'
states = {}

for filename in os.listdir('states'):
    state = os.path.splitext(os.path.basename(filename))[0]
    states[state] = yaml.load(open(f'states/{state}.yaml', 'r'))

stream = open('stories/'+story+'.yaml', 'r')
story = yaml.load(stream)

msg1 = "world!"
msg2= "hello"
duration = 1
max = 100

def build_story(story, states):

    movie = []

    for event in story:
        for duration in range(event['duration']):
            for key in states[event['state']]['state']:
                if 'env' in states[event['state']]:
                    states[event['state']]['state'][key] = states[event['state']]['state'][key].format(**states[event['state']]['env'])
            movie.append(states[event['state']])
    return movie 
    

movie = build_story(story, states)

cursor = -1
for a in range(1,len(movie) * max):

    if cursor >= len(movie) - 1:
        cursor = 0
    else:
        cursor = cursor + 1

    print(chr(27) + "[2J")
    for key in movie[cursor]['state']:
        print(movie[cursor]['state'][key])
    time.sleep(1)
