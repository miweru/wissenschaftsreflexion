import random
from org.transcrypt.stubs.browser import document


def t_to_p(t, df):
    print(t, df)
    # Umwandeln eines T-Wertes in einen P-Wert
    pValue = window.calculate_p_value(t, df)
    return pValue




class PainEvents:
    def __init__(self):
        self.state = {}
    def add_one(self,id):
        if id not in self.state:
            self.state[id]=0
        self.state[id]+=1
        #print(self.state[id])

    def add_zero(self,id):
        if id not in self.state:
            self.state[id]=0
        #print(self.state[id])
    def get(self, id):
        return self.state[id]

    def values(self):
        return self.state.values()

def calculate_t_value(group1, group2):
    mean1 = sum(group1) / len(group1)
    mean2 = sum(group2) / len(group2)
    print(mean1,mean2,group1,group2)
    var1 = sum((xi - mean1) ** 2 for xi in group1) / len(group1)
    var2 = sum((xi - mean2) ** 2 for xi in group2) / len(group2)
    t_value = (mean1 - mean2) / ((var1 / len(group1) + var2 / len(group2)) ** 0.5)
    print(t_value)
    return t_value


def Studie(props):
    participantCount, setParticipantCount = React.useState(0)
    splitRatio, setSplitRatio = React.useState(0.5)
    isSplit, setIsSplit = React.useState(False)
    truePainLevel = 0.005
    studyInterval = None  # Declare a variable to hold the interval


    #painEventsA, setPainEventsA = React.useState({})  # Counter for pain events in group A
    #painEventsB, setPainEventsB = React.useState({})  # Counter for pain events in group B

    painEventsA = PainEvents()
    painEventsB = PainEvents()
    painEventsAcum, setpainEventsAcum = React.useState(0)
    painEventsBcum, setpainEventsBcum = React.useState(0)
    pValue, setPValue = React.useState(-1)

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
        nonlocal painEventsA
        nonlocal painEventsB
        #newPainEventsA = dict(painEventsA)  # Copy the dictionary
        #print(painEventsA)
        #newPainEventsB = dict(painEventsB)  # Copy the dictionary

        for participant in participants:
            emoji, id = participant

            if participant in groupA:
                if random.random() < truePainLevel:
                    painEventsA.add_one(id)
                    #print(newPainEventsA[id])
                else:
                    painEventsA.add_zero(id)
            else:
                if random.random() < truePainLevel:
                    painEventsB.add_one(id)
                else:
                    painEventsB.add_zero(id)

        timeElapsed += 1
        if timeElapsed >= studyDuration:
            clearInterval(studyInterval)

        #setPainEventsA(newPainEventsA)
        #setPainEventsB(newPainEventsB)
        setpainEventsAcum(sum(painEventsA.values()))
        setpainEventsBcum(sum(painEventsB.values()))
        #print(painEventsA)
        setTimeElapsed(timeElapsed)
        if timeElapsed >= studyDuration:
            clearInterval(studyInterval)
            #print(painEventsA.values())
            setPValue(t_to_p(calculate_t_value(list(painEventsA.values()), list(painEventsB.values())),len(painEventsA.values())+len(painEventsB.values())))

    def handleButtonClick(event):
        setIsSplit(True)
        nonlocal studyInterval  # Declare studyInterval as nonlocal
        studyInterval = setInterval(startStudy, 333)  # Set an interval to repeat the study every second

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
                                   painEventsAcum) if isSplit else ''),
                               # Show the total number of pain events in group A
                               React.createElement('div', {}, ' '.join(
                                   [emoji for emoji, id in groupA]) if isSplit else emoji_string),
                               React.createElement('p', {}, 'Kopfschmerzereignisse in Gruppe B: ' + str(
                                   painEventsBcum) if isSplit else ''),
                               # Show the total number of pain events in group B
                               React.createElement('div', {},
                                                   ' '.join([emoji for emoji, id in groupB]) if isSplit else ''),
                               React.createElement('p', {}, 'p-Wert: ' + str(pValue)),
                               )

react_element = React.createElement(Studie, {})
ReactDOM.render(react_element, document.getElementById('content'))