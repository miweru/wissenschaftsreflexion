import random
from org.transcrypt.stubs.browser import document
import math


class math:
    pi = 3.14159265359
    e = 2.718281828459045

    @staticmethod
    def ln(x, n_terms=100):
        return sum([((-1) ** (n - 1)) * (x - 1) ** n / n for n in range(1, n_terms + 1)])

    @staticmethod
    def ln_gamma(z, n_terms=100):
        g = [7.1562499999993797, 0.1659470187408462e-06,
             0.1659470187408462e-06, 0.1659470187408462e-06,
             0.1659470187408462e-06, 0.16060597132059125e-01,
             0.16060597132059125e-01, 0.53320781342957658,
             0.53320781342957658, 0.53320781342957658,
             0.20580808427784533e+01, 0.14065092762033e+03,
             0.14065092762033e+03, 0.49094141100024683e+05,
             0.4930417745369179e+07, 0.4922931438387461e+09,
             0.999165130434776587, 0.99999999999980993, 1.000000000000000]

        x = 0.99999999999980993
        for i in range(1, 18):
            x += g[i] / (z + i)
        c = 2 * math.pi / (x * g[0])
        log_c = math.ln(c, n_terms)
        return log_c + (z + 0.5) * math.ln(z + 5.5, n_terms) - (z + 5.5) + math.ln(x * g[0], n_terms)


    @staticmethod
    def ln_factorial(n):
        return sum(math.ln(i) for i in range(1, n + 1))

    @staticmethod
    def exp(x, n_terms=100):
        return sum((x ** n) / math.ln_factorial(n) for n in range(n_terms))

    @staticmethod
    def gamma(z, n_terms=100):
        return math.exp(math.ln_gamma(z, n_terms), n_terms)

    @staticmethod
    def sqrt(x):
        return x ** 0.5

    @staticmethod
    def beta(x, y):
        return math.gamma(x) * math.gamma(y) / math.gamma(x + y)




def beta(x, y):
    # Die Beta-Funktion basierend auf der Gamma-Funktion
    return math.gamma(x) * math.gamma(y) / math.gamma(x+y)

def t_distribution(x, df):
    # Die Dichtefunktion der T-Verteilung
    ln_result = (math.gamma((df+1)/2) - math.ln(math.sqrt(df*math.pi))
                 - math.gamma(df/2) - ((df+1)/2) * math.ln(1 + (x**2/df)))
    print(ln_result)
    return math.exp(ln_result)

def t_cdf(t, df):
    # Die kumulative Dichtefunktion der T-Verteilung
    # Anwendung der Simpson-Regel zur numerischen Integration
    x = abs(t)
    a = 0
    b = x
    n = 1000  # Anzahl der Teilintervalle
    h = (b-a) / n
    print(h)
    integral = t_distribution(a, df) + t_distribution(b, df) + 4*t_distribution(b-h, df)
    print(integral)
    for i in range(1, n//2):
        integral += 4*t_distribution(a + 2*i*h, df) + 2*t_distribution(a + (2*i-1)*h, df)
        print(integral)
    integral *= h / 3
    return 0.5 + (integral / math.sqrt(df*math.pi/beta(0.5, df/2)))

def t_to_p(t, df):
    print(t,df)
    # Umwandeln eines T-Wertes in einen P-Wert
    cdf = t_cdf(t, df)
    if t > 0:
        return 1-cdf
    else:
        return cdf

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