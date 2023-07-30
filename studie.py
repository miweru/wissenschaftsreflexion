import random
from org.transcrypt.stubs.browser import document

def Studie(props):
    participantCount, setParticipantCount = React.useState(0)
    splitRatio, setSplitRatio = React.useState(0.5)
    isSplit, setIsSplit = React.useState(False)
    truePainLevel = 0.5
    studyInterval = None  # Declare a variable to hold the interval

    painEventsA, setPainEventsA = React.useState({})  # Counter for pain events in group A
    painEventsB, setPainEventsB = React.useState({})  # Counter for pain events in group B


    emojis = ['👩', '👩🏻', '👩🏼', '👩🏽', '👩🏾', '👩🏿', '👨', '👨🏻', '👨🏼', '👨🏽', '👨🏾', '👨🏿',
              '🧓', '🧓🏻', '🧓🏼', '🧓🏽', '🧓🏾', '🧓🏿', '👴', '👴🏻', '👴🏼', '👴🏽', '👴🏾', '👴🏿',
              '👵', '👵🏻', '👵🏼', '👵🏽', '👵🏾', '👵🏿', '👧', '👧🏻', '👧🏼', '👧🏽', '👧🏾', '👧🏿',
              '👦', '👦🏻', '👦🏼', '👦🏽', '👦🏾', '👦🏿', '👶', '👶🏻', '👶🏼', '👶🏽', '👶🏾', '👶🏿',
              '🧕', '🧕🏻', '🧕🏼', '🧕🏽', '🧕🏾', '🧕🏿', '👳‍♂️', '👳🏻‍♂️', '👳🏼‍♂️', '👳🏽‍♂️', '👳🏾‍♂️', '👳🏿‍♂️',
              '👳‍♀️', '👳🏻‍♀️', '👳🏼‍♀️', '👳🏽‍♀️', '👳🏾‍♀️', '👳🏿‍♀️', '👲', '👲🏻', '👲🏼', '👲🏽', '👲🏾', '👲🏿',
              '🧔', '🧔🏻', '🧔🏼', '🧔🏽', '🧔🏾', '🧔🏿', '👱‍♀️', '👱🏻‍♀️', '👱🏼‍♀️', '👱🏽‍♀️', '👱🏾‍♀️', '👱🏿‍♀️',
              '👱‍♂️', '👱🏻‍♂️', '👱🏼‍♂️', '👱🏽‍♂️', '👱🏾‍♂️', '👱🏿‍♂️']

    # Create a list of participant emojis
    participants, setParticipants = React.useState([])
    emoji_string = ' '.join([emoji for emoji, id in participants])


    # Create a list of participant emojis with unique IDs
    React.useEffect(lambda: setParticipants([(random.choice(emojis), i) for i in range(participantCount)]),
                    [participantCount])

    # Split the participants into groups
    splitPoint = int(len(participants) * splitRatio)
    groupA = participants[:splitPoint]
    groupB = participants[splitPoint:]

    def handleParticipantChange(event):
        setParticipantCount(int(event.target.value))

    def handleSplitChange(event):
        setSplitRatio(float(event.target.value))

    studyDuration, setStudyDuration = React.useState(30)
    timeElapsed, setTimeElapsed = React.useState(0)

    def handleDurationChange(event):
        setStudyDuration(int(event.target.value))

    def simulatePain():
        return random.choice(range(1, 11))

    def startStudy():
        nonlocal timeElapsed
        nonlocal studyInterval  # Declare studyInterval as nonlocal
        newPainEventsA = dict(painEventsA)  # Copy the dictionary
        #print(painEventsA)
        newPainEventsB = dict(painEventsB)  # Copy the dictionary

        for participant in participants:
            emoji, id = participant
            if random.random() < truePainLevel:
                if participant in groupA:
                    #print(newPainEventsA[id])
                    if id not in newPainEventsA:
                        newPainEventsA[id] = 0
                    newPainEventsA[id] += 1
                    #print(newPainEventsA[id])
                else:
                    if id not in newPainEventsB:
                        newPainEventsB[id] = 0
                    newPainEventsB[id] += 1

        timeElapsed += 1
        if timeElapsed >= studyDuration:
            clearInterval(studyInterval)

        setPainEventsA(newPainEventsA)
        setPainEventsB(newPainEventsB)
        #print(painEventsA)
        setTimeElapsed(timeElapsed)

    def handleButtonClick(event):
        setIsSplit(True)
        nonlocal studyInterval  # Declare studyInterval as nonlocal
        studyInterval = setInterval(startStudy, 1000)  # Set an interval to repeat the study every second

    # render code ...
    # Add another input for study duration
    return React.createElement('div', {},
                               React.createElement('h1', {}, 'Studiensimulator'),
                               React.createElement('p', {}, 'Anzahl der Teilnehmer*innen: ' + str(participantCount)),
                               React.createElement('input', {'type': 'range', 'min': '0', 'max': '1000',
                                                             'value': str(participantCount),
                                                             'onChange': handleParticipantChange}),
                               React.createElement('p', {}, 'Split-Verhältnis: ' + str(splitRatio)),
                               React.createElement('input', {'type': 'range', 'min': '0', 'max': '1', 'step': '0.01',
                                                             'value': str(splitRatio),
                                                             'onChange': handleSplitChange}),
                               React.createElement('p', {}, 'Studiendauer: ' + str(studyDuration)),
                               React.createElement('input', {'type': 'range', 'min': '0', 'max': '100',
                                                             'value': str(studyDuration),
                                                             'onChange': handleDurationChange}),
                               React.createElement('p', {}, 'Zeit vergangen: ' + str(timeElapsed)),
                               React.createElement('p', {}, emoji_string),
                               React.createElement('button', {'onClick': handleButtonClick}, 'Studie starten'),
                               React.createElement('p', {}, 'Kopfschmerzereignisse in Gruppe A: ' + str(
                                   sum(painEventsA.values())) if isSplit else ''),
                               # Show the total number of pain events in group A
                               React.createElement('div', {}, ' '.join(
                                   [emoji for emoji, id in groupA]) if isSplit else emoji_string),
                               React.createElement('p', {}, 'Kopfschmerzereignisse in Gruppe B: ' + str(
                                   sum(painEventsB.values())) if isSplit else ''),
                               # Show the total number of pain events in group B
                               React.createElement('div', {},
                                                   ' '.join([emoji for emoji, id in groupB]) if isSplit else '')
                               )

react_element = React.createElement(Studie, {})
ReactDOM.render(react_element, document.getElementById('content'))