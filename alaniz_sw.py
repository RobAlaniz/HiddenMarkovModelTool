from collections import OrderedDict
import math


def State_File_Start_Probabilities(t, s):
    move_to_next_line = "null"

    starting_state_per_line = ""
    adjusted_starting_states = ""

    input_state_sequence = open('set160_state_sequences.txt', 'r')
    for line in input_state_sequence:
        if move_to_next_line == "yes":
                starting_state_per_line = starting_state_per_line + line[0]
        if line[0] == ">":
                
            if move_to_next_line == "null":
                move_to_next_line = "yes"
    count = 0

    for i in starting_state_per_line:
        
        if i == ">":
            adjusted_starting_states = adjusted_starting_states + starting_state_per_line[count+1]

    total_count = 0
    t_count = 0
    s_count = 0
    for i in adjusted_starting_states:
        if i == "T":
            t_count += 1
        if i == "S":
            s_count += 1
        total_count += 1
        
    for i in adjusted_starting_states:
        if i == "S":
            s_count += 1
            total_count += 1
        elif i == "T":
            t_count += 1
            total_count += 1
    t = float(format((float(t_count)/total_count), ".3f"))

    s = float(format((float(s_count)/total_count), ".3f"))
    st_list = []
    st_list.append(t)
    st_list.append(s)
    input_state_sequence.close()
    return st_list






def State_File_Emissions():
    input_state_sequence = open('set160_state_sequences.txt', 'r')
    state_string = ""
    adjusted_state_string = ""

    for line in input_state_sequence:
        if line[0] == ">":
            skipped = "skipped line"
        else:
            adjusted_state_string = adjusted_state_string + str(line)



    for i in adjusted_state_string:
        if i != "S" or i != "T":
            skipped = "skipped"
        if i == "S" or i == "T":
            state_string = state_string + str(i)
            
    end_index = 1
    digram_dictionary = {}
    total_count = 0
    total_count_s = 0
    total_count_t = 0
    while end_index < int(len(state_string)):
        if (state_string[end_index-1] + state_string[end_index]) not in digram_dictionary:
            digram_dictionary[(state_string[end_index-1] + state_string[end_index])] = 1
            if (state_string[end_index-1] + state_string[end_index]) == "SS":
                total_count_s = total_count_s + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "ST":
                  total_count_s = total_count_s + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "TT":
                  total_count_t = total_count_t + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "TS":
                  total_count_t = total_count_t + 1
            total_count += 1
        else:
            digram_dictionary[(state_string[end_index-1] + state_string[end_index])] +=1
            if (state_string[end_index-1] + state_string[end_index]) == "SS":
                total_count_s = total_count_s + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "ST":
                  total_count_s = total_count_s + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "TT":
                  total_count_t = total_count_t + 1
            elif (state_string[end_index-1] + state_string[end_index]) == "TS":
                  total_count_t = total_count_t + 1
            total_count += 1
        end_index += 1
                
    for i in digram_dictionary:

        if i == "SS":
            digram_dictionary[i] = format(((digram_dictionary[i]/ int(total_count_s))), ".3f")
        elif i == "ST":
            digram_dictionary[i] = format(((digram_dictionary[i]/ int(total_count_s))), ".3f")
        elif i == "TT":
            digram_dictionary[i] = format(((digram_dictionary[i]/ int(total_count_t))), ".3f")
        elif i == "TS":
            digram_dictionary[i] = format(((digram_dictionary[i]/ int(total_count_t))), ".3f")
            

    input_state_sequence.close()
    return digram_dictionary





def Soluble_File_Emissions():
    input_soluble_sequence = open('set160_soluble.txt', 'r')
    soluble_string = ""
    for line in input_soluble_sequence:
        for i in line:
            if i != "\n":
                soluble_string = soluble_string + i
    
    input_soluble_sequence.close()

    soluble_acids = {}

    other_values_present = 0
    for i in soluble_string:
        if i in soluble_acids:
            soluble_acids[i] += 1
        elif i.isalpha() == True:
            soluble_acids[str(i)] = 1
        else:
            other_values_present = 0


    alphabetical_soluble_acids_Dict = OrderedDict(sorted(soluble_acids.items(), key=lambda t: t[0]))

    for i in alphabetical_soluble_acids_Dict:
        alphabetical_soluble_acids_Dict[i] = format((alphabetical_soluble_acids_Dict[i]/int(len(soluble_string))), ".3f")
    
    soluble_emissions = {}

    for i in alphabetical_soluble_acids_Dict:
        soluble_emissions[i] = alphabetical_soluble_acids_Dict[i]
    
    return soluble_emissions




def Trans_File_Emissions():
    input_trans_sequence = open('set160_membrane.txt', 'r')

    trans_string = ""

    for line in input_trans_sequence:
        for i in line:
            if i != "\n":
                trans_string = trans_string + i
        
    input_trans_sequence.close()

    input_trans_sequence = open('set160_membrane.txt', 'r')
    trans_acids = {}

    for line in input_trans_sequence:
        for i in line:
            if i.isalpha() == True:
                if i not in trans_acids:
                    trans_acids[i] = 1
                else:
                    
                    trans_acids[i] += 1


    #print(other_values_present)


    alphabetical_trans_acids_Dict = OrderedDict(sorted(trans_acids.items(), key=lambda t: t[0]))

    for i in alphabetical_trans_acids_Dict:
        alphabetical_trans_acids_Dict[i] = format((alphabetical_trans_acids_Dict[i]/int(len(trans_string))), ".3f")

    input_trans_sequence.close()
    membrane_emissions = {}
    for i in alphabetical_trans_acids_Dict:
        membrane_emissions[i] = alphabetical_trans_acids_Dict[i]
    
    return membrane_emissions



#   The Virterbi_Matrix is created and each time a path is chosen the Predicted State Sequence is updated with the chosen state
#   This is where I score the matrix based on the previous S and T transition values based on both S-->T, S--S, T-->S, and T-->S
#   What I did here was generate a 2 x N matrix where N is the number of States the predicted sequence is predicting.


def Virterbi_Matrix(t, s, digram_dictionary, alphabetical_soluble_acids_computed, alphabetical_trans_acids_computed):
    virterbi_matrix = {"S": [], "T": [], "Predicted State Sequence" : ""}
    list_s = []
    list_t = []
    test_string = "KNSFFFFFFFLIII"

    predictive_state_seq = ""
    highest_scored_total = 0


    if s > t:
        predictive_state_seq = predictive_state_seq + "S"
        highest_scored_total = float(s)


    else:
        predictive_state_seq = predictive_state_seq + "T"
        highest_scored_total = float(t)


    count = 0
    for i in test_string:
    #   This is where I score the matrix based on the previous S and T transition values based on both S-->T, S--S, T-->S, and T-->S
    #   What I did here was generate a 2 x N matrix where N is the number of States the predicted sequence is predicting.

        
        if count >= 1 and count < int(len(test_string)):

            if predictive_state_seq[count-1] == "S":
                if (highest_scored_total + float(digram_dictionary["SS"]) + float(alphabetical_soluble_acids_computed[i])) > (highest_scored_total + float(digram_dictionary["ST"]) + float(alphabetical_soluble_acids_computed[i])):
                    alt_scored_total = 0.0
                    alt_scored_total = highest_scored_total + float(digram_dictionary["ST"]) + float(alphabetical_trans_acids_computed[i])
                    highest_scored_total = (highest_scored_total + float(digram_dictionary["SS"]) + float(alphabetical_soluble_acids_computed[i]))
                    predictive_state_seq = predictive_state_seq + "S"
                    list_s.append(format(highest_scored_total, ".3f"))


                    list_t.append(format(alt_scored_total, ".3f"))
                    

                    virterbi_matrix["S"] = list_s
                    virterbi_matrix["T"] = list_t

                    
                elif (highest_scored_total + float(digram_dictionary["ST"]) + float(alphabetical_soluble_acids_computed[i])) > (highest_scored_total + float(digram_dictionary["SS"]) + float(alphabetical_soluble_acids_computed[i])):
                    highest_scored_total = highest_scored_total + float(digram_dictionary["ST"]) + float(alphabetical_soluble_acids_computed[i])
                    predictive_state_seq = predictive_state_seq + "T"
                    list_t.append(format(highest_scored_total, ".3f"))
                    string = str(format(highest_scored_total, ".3f"))

                    virterbi_matrix["S"] = list_s
                    virterbi_matrix["T"] = list_t
                    
            elif predictive_state_seq[(count-1)] == "T":
                if (highest_scored_total + float(digram_dictionary["TT"]) + float(alphabetical_soluble_acids_computed[i])) > (float(highest_scored_total) + float(digram_dictionary["TS"]) + float(alphabetical_soluble_acids_computed[i])):
                    highest_scored_total = highest_scored_total + float(digram_dictionary["TT"]) + float(alphabetical_soluble_acids_computed[i])
                    predictive_state_seq = predictive_state_seq + "T"
                    list_t.append(format(highest_scored_total, ".3f"))
                    string = str(format(highest_scored_total, ".3f"))

                    list_t.append(zero)
                    virterbi_matrix["S"] = list_s
                    virterbi_matrix["T"] = list_t
                    
                elif (highest_scored_total + float(digram_dictionary["TS"]) + float(alphabetical_soluble_acids_computed[i])) > (float(highest_scored_total) + float(digram_dictionary["TT"]) + float(alphabetical_soluble_acids_computed[i])):
                    highest_scored_total = highest_scored_total + float(digram_dictionary["TS"]) + float(alphabetical_soluble_acids_computed[i])
                    predictive_state_seq = predictive_state_seq + "S"
                    list_s.append(format(highest_scored_total, ".3f"))
                    string = str(format(highest_scored_total, ".3f"))

                    virterbi_matrix["S"] = list_s
                    virterbi_matrix["T"] = list_t
        else:

            if float(alphabetical_soluble_acids_computed[i]) > float(alphabetical_trans_acids_computed[i]):
                highest_scored_total = highest_scored_total + float(alphabetical_soluble_acids_computed[i])
                list_s.append(format(highest_scored_total, ".3f"))
                zero = ""
                string = str(highest_scored_total)
                alt_scored_total = 0.0
                alt_scored_total = t + float(alphabetical_trans_acids_computed[i])
                list_t.append(format(alt_scored_total, ".3f"))
                virterbi_matrix["S"] = list_s
                virterbi_matrix["T"] = list_t
            else:
                highest_scored_total = highest_scored_total + float(alphabetical_trans_acids_computed[i])
                list_t.append(format(highest_scored_total, ".3f"))
                virterbi_matrix["T"] = list_t
                        
        count +=1
    virterbi_matrix["Predicted State Sequence"] = predictive_state_seq  
    return virterbi_matrix 


if __name__ == '__main__':

    
    t = 0.0
    s = 0.0
    Start_Probabilities = {}
    State_Emissions = {}
    Soluble_Emissions = {}
    Membrane_Emissions = {}
    
    Start_Probabilities = State_File_Start_Probabilities(t, s)
    t = Start_Probabilities[0]
    s = Start_Probabilities[1]
    
    State_Emissions = State_File_Emissions()
    Soluble_Emissions = Soluble_File_Emissions()
    Membrane_Emissions = Trans_File_Emissions()

    print("\nVirterbi Matrix: \n")
    Virterbi_Matrix = Virterbi_Matrix(t, s, State_Emissions, Soluble_Emissions, Membrane_Emissions)

    
    for i in Virterbi_Matrix:
        print(i, Virterbi_Matrix[i], "\n")

        
    print("\nState File: State Emissions")
    for v in State_Emissions:
        print(v, State_Emissions[v])

        
    print("\nSoluble File: Amino Acid Emissions")        
    for d in Soluble_Emissions:
        print(d, Soluble_Emissions[d])

        
    print("\nMembrane File: Amino Acid Emissions")       
    for e in Membrane_Emissions:
        print(e, Membrane_Emissions[e])
        
    
    
     




