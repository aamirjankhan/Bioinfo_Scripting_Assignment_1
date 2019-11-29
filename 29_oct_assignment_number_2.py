import random #importing random method to choose random elements from a list of A,T,C,G
import re
nucleotides=['a','t','c','g'] #list of nucleotides
print("ttcacctatgaantggactgtccccaaagaagtanggacccactaatgcagnatcctgtg")
strr=list(input('please enter a valid nucleotide sequence: ')) #taking input from the user and converting it to list
n=0 #flag variable
while(n!=len(strr)): #while loop 
    if(strr[n]!='a' and strr[n]!='t' and strr[n]!='c' and strr[n]!='g'): #if a residue is other then A G C T
        neut=random.choice(nucleotides) #replacing nucleotides
        print(strr[n]+' changed to '+neut) 
        strr[n]=neut
        print('non nucleotide occurance is on index: '+str(n)) #displaying the non nucleotide occurance
    n+=1 #additive operator
print(''.join(strr)) #converting it back to the string
frr=open("sequences.txt","r") #opening the file containing the sequences
line=frr.readline()
sequences,sequence1,sequence_rev,ids,poly_A,lenght,start,end,score=[],[],[],[],[],[],[],[],[]
#lists of id's, poly A tails, poly A start, poly A end, length of the sequences, and a score list
while(line):
    sequences.append(line.rstrip()) #appending sequences for further operations
    line=frr.readline()
while "" in sequences:
        sequences.remove("") #removing extra empty indexes from the list

def func1(lst,lst1): #function to get the sequences and appending to another list
    for i in range(len(lst)):
        if ">" not in lst[i]:
            lst1.append(lst[i])
func1(sequences,sequence1)

def func2(lst,lst1): #function to reverse the sequences for our ease, inorder to get the poly A tail 
    for i in range(len(lst)):
        seq=lst[i]
        lst1.append(seq[::-1]) #appending into an other list for further ease
func2(sequence1,sequence_rev)

def func3(lst,lst1,lst2): #function to retreive the sequence id's
    pattern=re.compile(r"\w+\.\d+") #pattern
    for i in range(len(lst)):
        match=pattern.findall(lst[i])
        lst1.extend(match)
    for i in range(len(lst)):
       if not ">" in lst[i]:
           lst2.append(len(lst[i]))
    while [] in lst1:
        lst1.remove([]) #removing empty indexes of a list
func3(sequences,ids,lenght)

def func4(lst,lst1,lst2,start,end): #function to get the poly A tail, its start, its end, whilst allowing one mismatch at a time
    pattern=re.compile(r"^[A]{3,10}[CTG]{0,1}[A]+[CTG]{0,1}[A]+") #pattern for allowing one mismatch at a time
    for i in range(len(lst)):
        match=pattern.findall(lst[i])
        lst1.extend(match)
    while [] in lst1:
        lst1.remove([])
    for j in range(len(lst)):
        start.append(len(lst[j])-len(lst1[j]))
        end.append(len(lst[j]))

    
def func5(lst1,lst2): #function to get the percentage identity of the poly A tail
    for i in range(len(lst1)):
        seq=lst1[i]
        match=0
        mismatch=0
        for s in seq:
            if s is "A":
                match+=1 #counting the number of mismatches and matches
            else:
                mismatch+=1
        lst2.append((match/(match+mismatch))*100)  #applying the formula         
func4(sequence_rev,poly_A,sequences,start,end)

func5(poly_A,score)


def func6(lst1,lst2,lst3,lst4,lst5): #function to display all the results in the given format by sir Nadeem
    for i in range(5):
        print("Sequence_ID\t\tlength\tStart\tEnd\tPercentage identity")
        print("{}\t{}\t{}\t{}\t\t{}".format(lst1[i],lst2[i],lst3[i],lst4[i],lst5[i]))
print(func6(ids,lenght,start,end,score))
            
        
