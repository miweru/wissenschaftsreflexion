'use strict';var random={};import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,
__ipow__,__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,
getattr,hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import*as __module_random__ from"./random.js";__nest__(random,"",__module_random__);var __name__="__main__";export var Studie=function(props){var __left0__=React.useState(0);var participantCount=__left0__[0];var setParticipantCount=__left0__[1];var __left0__=
React.useState(.5);var splitRatio=__left0__[0];var setSplitRatio=__left0__[1];var __left0__=React.useState(false);var isSplit=__left0__[0];var setIsSplit=__left0__[1];var truePainLevel=.5;var studyInterval=null;var __left0__=React.useState(dict({}));var painEventsA=__left0__[0];var setPainEventsA=__left0__[1];var __left0__=React.useState(dict({}));var painEventsB=__left0__[0];var setPainEventsB=__left0__[1];var emojis=["\ud83d\udc69","\ud83d\udc69\ud83c\udffb","\ud83d\udc69\ud83c\udffc","\ud83d\udc69\ud83c\udffd",
"\ud83d\udc69\ud83c\udffe","\ud83d\udc69\ud83c\udfff","\ud83d\udc68","\ud83d\udc68\ud83c\udffb","\ud83d\udc68\ud83c\udffc","\ud83d\udc68\ud83c\udffd","\ud83d\udc68\ud83c\udffe","\ud83d\udc68\ud83c\udfff","\ud83e\uddd3","\ud83e\uddd3\ud83c\udffb","\ud83e\uddd3\ud83c\udffc","\ud83e\uddd3\ud83c\udffd","\ud83e\uddd3\ud83c\udffe","\ud83e\uddd3\ud83c\udfff","\ud83d\udc74","\ud83d\udc74\ud83c\udffb","\ud83d\udc74\ud83c\udffc","\ud83d\udc74\ud83c\udffd","\ud83d\udc74\ud83c\udffe","\ud83d\udc74\ud83c\udfff",
"\ud83d\udc75","\ud83d\udc75\ud83c\udffb","\ud83d\udc75\ud83c\udffc","\ud83d\udc75\ud83c\udffd","\ud83d\udc75\ud83c\udffe","\ud83d\udc75\ud83c\udfff","\ud83d\udc67","\ud83d\udc67\ud83c\udffb","\ud83d\udc67\ud83c\udffc","\ud83d\udc67\ud83c\udffd","\ud83d\udc67\ud83c\udffe","\ud83d\udc67\ud83c\udfff","\ud83d\udc66","\ud83d\udc66\ud83c\udffb","\ud83d\udc66\ud83c\udffc","\ud83d\udc66\ud83c\udffd","\ud83d\udc66\ud83c\udffe","\ud83d\udc66\ud83c\udfff","\ud83d\udc76","\ud83d\udc76\ud83c\udffb","\ud83d\udc76\ud83c\udffc",
"\ud83d\udc76\ud83c\udffd","\ud83d\udc76\ud83c\udffe","\ud83d\udc76\ud83c\udfff","\ud83e\uddd5","\ud83e\uddd5\ud83c\udffb","\ud83e\uddd5\ud83c\udffc","\ud83e\uddd5\ud83c\udffd","\ud83e\uddd5\ud83c\udffe","\ud83e\uddd5\ud83c\udfff","\ud83d\udc73\u200d\u2642\ufe0f","\ud83d\udc73\ud83c\udffb\u200d\u2642\ufe0f","\ud83d\udc73\ud83c\udffc\u200d\u2642\ufe0f","\ud83d\udc73\ud83c\udffd\u200d\u2642\ufe0f","\ud83d\udc73\ud83c\udffe\u200d\u2642\ufe0f","\ud83d\udc73\ud83c\udfff\u200d\u2642\ufe0f","\ud83d\udc73\u200d\u2640\ufe0f",
"\ud83d\udc73\ud83c\udffb\u200d\u2640\ufe0f","\ud83d\udc73\ud83c\udffc\u200d\u2640\ufe0f","\ud83d\udc73\ud83c\udffd\u200d\u2640\ufe0f","\ud83d\udc73\ud83c\udffe\u200d\u2640\ufe0f","\ud83d\udc73\ud83c\udfff\u200d\u2640\ufe0f","\ud83d\udc72","\ud83d\udc72\ud83c\udffb","\ud83d\udc72\ud83c\udffc","\ud83d\udc72\ud83c\udffd","\ud83d\udc72\ud83c\udffe","\ud83d\udc72\ud83c\udfff","\ud83e\uddd4","\ud83e\uddd4\ud83c\udffb","\ud83e\uddd4\ud83c\udffc","\ud83e\uddd4\ud83c\udffd","\ud83e\uddd4\ud83c\udffe","\ud83e\uddd4\ud83c\udfff",
"\ud83d\udc71\u200d\u2640\ufe0f","\ud83d\udc71\ud83c\udffb\u200d\u2640\ufe0f","\ud83d\udc71\ud83c\udffc\u200d\u2640\ufe0f","\ud83d\udc71\ud83c\udffd\u200d\u2640\ufe0f","\ud83d\udc71\ud83c\udffe\u200d\u2640\ufe0f","\ud83d\udc71\ud83c\udfff\u200d\u2640\ufe0f","\ud83d\udc71\u200d\u2642\ufe0f","\ud83d\udc71\ud83c\udffb\u200d\u2642\ufe0f","\ud83d\udc71\ud83c\udffc\u200d\u2642\ufe0f","\ud83d\udc71\ud83c\udffd\u200d\u2642\ufe0f","\ud83d\udc71\ud83c\udffe\u200d\u2642\ufe0f","\ud83d\udc71\ud83c\udfff\u200d\u2642\ufe0f"];
var __left0__=React.useState([]);var participants=__left0__[0];var setParticipants=__left0__[1];var emoji_string=" ".join(participants);React.useEffect(function __lambda__(){return setParticipants(function(){var __accu0__=[];for(var _=0;_<participantCount;_++)__accu0__.append(random.choice(emojis));return __accu0__}())},[participantCount]);var splitPoint=int(len(participants)*splitRatio);var groupA=participants.__getslice__(0,splitPoint,1);var groupB=participants.__getslice__(splitPoint,null,1);var handleParticipantChange=
function(event){setParticipantCount(int(event.target.value))};var handleSplitChange=function(event){setSplitRatio(float(event.target.value))};var __left0__=React.useState(30);var studyDuration=__left0__[0];var setStudyDuration=__left0__[1];var __left0__=React.useState(0);var timeElapsed=__left0__[0];var setTimeElapsed=__left0__[1];var handleDurationChange=function(event){setStudyDuration(int(event.target.value))};var simulatePain=function(){return random.choice(range(1,11))};var startStudy=function(){var newPainEventsA=
dict(painEventsA);var newPainEventsB=dict(painEventsB);for(var emoji of participants)if(random.random()<truePainLevel)if(__in__(emoji,groupA)){if(!__in__(emoji,newPainEventsA))newPainEventsA[emoji]=0;newPainEventsA[emoji]++}else{if(!__in__(emoji,newPainEventsB))newPainEventsB[emoji]=0;newPainEventsB[emoji]++}timeElapsed++;if(timeElapsed>=studyDuration)clearInterval(studyInterval);setPainEventsA(newPainEventsA);setPainEventsB(newPainEventsB);setTimeElapsed(timeElapsed)};var handleButtonClick=function(event){setIsSplit(true);
studyInterval=setInterval(startStudy,1E3)};return React.createElement("div",dict({}),React.createElement("h1",dict({}),"Studiensimulator"),React.createElement("p",dict({}),"Anzahl der Teilnehmer*innen: "+str(participantCount)),React.createElement("input",dict({"type":"range","min":"0","max":"1000","value":str(participantCount),"onChange":handleParticipantChange})),React.createElement("p",dict({}),"Split-Verh\u00e4ltnis: "+str(splitRatio)),React.createElement("input",dict({"type":"range","min":"0",
"max":"1","step":"0.01","value":str(splitRatio),"onChange":handleSplitChange})),React.createElement("p",dict({}),"Studiendauer: "+str(studyDuration)),React.createElement("input",dict({"type":"range","min":"0","max":"100","value":str(studyDuration),"onChange":handleDurationChange})),React.createElement("p",dict({}),"Zeit vergangen: "+str(timeElapsed)),React.createElement("p",dict({}),emoji_string),React.createElement("button",dict({"onClick":handleButtonClick}),"Studie starten"),React.createElement("p",
dict({}),isSplit?"Kopfschmerzereignisse in Gruppe A: "+str(sum(painEventsA.py_values())):""),React.createElement("div",dict({}),isSplit?groupA:emoji_string),React.createElement("p",dict({}),isSplit?"Kopfschmerzereignisse in Gruppe B: "+str(sum(painEventsB.py_values())):""),React.createElement("div",dict({}),isSplit?groupB:""))};export var react_element=React.createElement(Studie,dict({}));ReactDOM.render(react_element,document.getElementById("content"));

//# sourceMappingURL=studie.map